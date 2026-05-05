import os
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

BAT_DETECTION_ENABLED = os.getenv("BAT_DETECTION_ENABLED", "false").lower() == "true"


class BatDetectionService:
    """
    Bat detection service using BatDetect2 ML model.

    Enabled only when BAT_DETECTION_ENABLED=true (full Docker image).

    NOTE: BatDetect2 requires ultrasonic audio recordings (>=192kHz sample rate).
    Standard audio files at 44.1kHz/48kHz will not produce bat detections as bat
    echolocation calls occur at 20-120kHz, above standard microphone range.
    Use an ultrasonic recorder (e.g. AudioMoth, Pettersson D500X) for real detections.
    """

    def __init__(self):
        self._bd2 = None
        if BAT_DETECTION_ENABLED:
            self._load_model()

    def _load_model(self):
        try:
            import batdetect2.api as bd2
            self._bd2 = bd2
            logger.info("BatDetect2 model loaded successfully")
        except ImportError:
            logger.warning(
                "batdetect2 not installed. Run with full image: "
                "docker compose --profile full up --build"
            )

    def analyze_audio(self, audio_path: str, min_confidence: float = 0.3) -> List[Dict]:
        """
        Analyze audio for bat echolocation calls using BatDetect2.
        Returns empty list if bat detection is disabled or audio is incompatible.
        """
        if not BAT_DETECTION_ENABLED or self._bd2 is None:
            return []

        try:
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
            logger.error(f"BatDetect2 error analyzing {audio_path}: {e}")
            return []
