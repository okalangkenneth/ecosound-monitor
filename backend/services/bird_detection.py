import librosa
import numpy as np
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
import os
from pathlib import Path
from typing import List, Dict

class BirdDetectionService:
    def __init__(self):
        # Initialize BirdNET analyzer with European species focus
        self.analyzer = Analyzer()
        
    def analyze_audio(self, audio_path: str, min_confidence: float = 0.25) -> List[Dict]:
        """
        Analyze audio file for bird species detection
        
        Args:
            audio_path: Path to audio file
            min_confidence: Minimum confidence threshold (0-1)
            
        Returns:
            List of detections with species, confidence, and timestamp
        """
        try:
            recording = Recording(
                self.analyzer,
                audio_path,
                min_conf=min_confidence,
            )
            recording.analyze()
            
            detections = []
            for detection in recording.detections:
                detections.append({
                    'species_name': detection['scientific_name'],
                    'common_name': detection['common_name'],
                    'confidence': detection['confidence'],
                    'timestamp': detection['start_time'],
                    'detection_type': 'bird'
                })
            
            return detections
            
        except Exception as e:
            print(f"Error analyzing audio: {str(e)}")
            return []
    
    def get_audio_info(self, audio_path: str) -> Dict:
        """Get basic audio file information"""
        try:
            y, sr = librosa.load(audio_path, sr=None)
            duration = librosa.get_duration(y=y, sr=sr)
            
            return {
                'duration': duration,
                'sample_rate': sr,
                'channels': 1 if len(y.shape) == 1 else y.shape[0]
            }
        except Exception as e:
            print(f"Error getting audio info: {str(e)}")
            return {}
