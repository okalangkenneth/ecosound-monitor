import librosa
import numpy as np
from typing import List, Dict

class BatDetectionService:
    """
    Real bat detection service using BatDetect2 ML model.

    NOTE: BatDetect2 is designed for ultrasonic audio recordings (>=192kHz sample rate).
    Standard audio files recorded at 44.1kHz or 48kHz will not produce bat detections
    as bat echolocation calls occur at 20-120kHz, above the range of standard microphones.
    Use an ultrasonic recorder (e.g. AudioMoth, Pettersson D500X) for real detections.
    """

    def __init__(self):
        self._model = None

    def _load_model(self):
        """Lazy-load BatDetect2 model on first use to keep startup fast."""
        if self._model is None:
            try:
                import batdetect2.api as bd2
                self._bd2 = bd2
            except ImportError:
                raise RuntimeError(
                    "batdetect2 is not installed. Run: pip install batdetect2"
                )

    def analyze_audio(self, audio_path: str, min_confidence: float = 0.3) -> List[Dict]:
        """
        Analyze audio file for bat echolocation calls using BatDetect2.

        Args:
            audio_path: Path to audio file (WAV recommended, >=192kHz for real detections)
            min_confidence: Minimum confidence threshold (0-1), default 0.3

        Returns:
            List of detections with species, confidence, and timestamp.
            Returns empty list if file is incompatible or an error occurs.
        """
        try:
            self._load_model()

            results = self._bd2.process_file(
                audio_path,
                detection_threshold=min_confidence
            )

            detections = []
            annotations = results.get("pred_dict", {}).get("annotation", [])

            for ann in annotations:
                species = ann.get("class", "Unknown bat species")
                confidence = float(ann.get("class_prob", 0.0))
                start_time = float(ann.get("start_time", 0.0))

                if confidence >= min_confidence:
                    detections.append({
                        "species_name": species,
                        "common_name": species,
                        "confidence": confidence,
                        "timestamp": start_time,
                        "detection_type": "bat"
                    })

            return sorted(detections, key=lambda x: x["timestamp"])

        except Exception as e:
            print(f"BatDetect2 error analyzing {audio_path}: {str(e)}")
            return []
