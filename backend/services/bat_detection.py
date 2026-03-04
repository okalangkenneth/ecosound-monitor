import librosa
import numpy as np
from typing import List, Dict
import random

class BatDetectionService:
    """
    Simplified bat detection service for MVP demo
    In production, this would use BatDetect2 or similar ML models
    """
    
    # Common European bat species for demo
    BAT_SPECIES = [
        {'scientific': 'Pipistrellus pipistrellus', 'common': 'Common Pipistrelle'},
        {'scientific': 'Myotis daubentonii', 'common': "Daubenton's Bat"},
        {'scientific': 'Eptesicus serotinus', 'common': 'Serotine Bat'},
        {'scientific': 'Nyctalus noctula', 'common': 'Common Noctule'},
        {'scientific': 'Plecotus auritus', 'common': 'Brown Long-eared Bat'},
    ]
    
    def __init__(self):
        pass
    
    def analyze_audio(self, audio_path: str, min_confidence: float = 0.3) -> List[Dict]:
        """
        Analyze audio for bat echolocation calls
        This is a simplified demo version that simulates detections
        """
        try:
            # Load audio to get duration
            y, sr = librosa.load(audio_path, sr=None)
            duration = librosa.get_duration(y=y, sr=sr)
            
            # For demo: simulate bat detections based on high-frequency content
            detections = []
            
            # Check if audio has high-frequency content (potential bat calls)
            if sr >= 44100:  # Need high sample rate for bat calls
                # Simulate 2-5 detections for demo
                num_detections = random.randint(2, 5)
                
                for i in range(num_detections):
                    species = random.choice(self.BAT_SPECIES)
                    timestamp = random.uniform(0, duration)
                    confidence = random.uniform(min_confidence, 0.95)
                    
                    detections.append({
                        'species_name': species['scientific'],
                        'common_name': species['common'],
                        'confidence': confidence,
                        'timestamp': timestamp,
                        'detection_type': 'bat'
                    })
            
            return sorted(detections, key=lambda x: x['timestamp'])
            
        except Exception as e:
            print(f"Error analyzing audio for bats: {str(e)}")
            return []
