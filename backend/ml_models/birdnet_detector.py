"""
BirdNET detector module for audio-based bird species detection
For MVP: Returns mock data. Can be replaced with actual BirdNET model integration.
"""

import librosa
import numpy as np
from typing import List, Dict

def detect_birds(audio_path: str) -> List[Dict]:
    """
    Detect bird species from audio file
    
    For MVP: Returns mock detections based on audio duration
    TODO: Integrate actual BirdNET model from https://github.com/kahst/BirdNET-Analyzer
    
    Args:
        audio_path: Path to audio file
        
    Returns:
        List of detection dictionaries with species info
    """
    
    try:
        # Load audio to get duration
        y, sr = librosa.load(audio_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        
        # Mock detections for demo purposes
        # In production, this would use BirdNET model
        mock_species = [
            {
                "species": "Common Chaffinch",
                "common_name": "Chaffinch", 
                "scientific_name": "Fringilla coelebs",
                "confidence": 0.92,
                "start_time": 2.3,
                "end_time": 5.1
            },
            {
                "species": "European Robin",
                "common_name": "Robin",
                "scientific_name": "Erithacus rubecula", 
                "confidence": 0.87,
                "start_time": 8.5,
                "end_time": 12.2
            },
            {
                "species": "Great Tit",
                "common_name": "Great Tit",
                "scientific_name": "Parus major",
                "confidence": 0.78,
                "start_time": 15.0,
                "end_time": 18.5
            },
            {
                "species": "Eurasian Blue Tit",
                "common_name": "Blue Tit",
                "scientific_name": "Cyanistes caeruleus",
                "confidence": 0.85,
                "start_time": 22.1,
                "end_time": 25.7
            },
            {
                "species": "Common Blackbird",
                "common_name": "Blackbird",
                "scientific_name": "Turdus merula",
                "confidence": 0.81,
                "start_time": 30.2,
                "end_time": 34.8
            }
        ]
        
        # Return only detections that fit within audio duration
        valid_detections = [
            det for det in mock_species 
            if det["start_time"] < duration
        ]
        
        # Adjust end times if needed
        for det in valid_detections:
            if det["end_time"] > duration:
                det["end_time"] = duration
        
        return valid_detections
        
    except Exception as e:
        print(f"Error in bird detection: {e}")
        return []


def detect_bats(audio_path: str) -> List[Dict]:
    """
    Detect bat species from audio file
    
    For MVP: Returns mock detections
    TODO: Integrate BatDetect2 or similar model
    
    Args:
        audio_path: Path to audio file
        
    Returns:
        List of detection dictionaries with species info
    """
    
    try:
        # Load audio
        y, sr = librosa.load(audio_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
        
        # Mock bat detections for demo
        mock_bats = [
            {
                "species": "Pipistrellus pipistrellus",
                "common_name": "Common Pipistrelle",
                "scientific_name": "Pipistrellus pipistrellus",
                "confidence": 0.89,
                "start_time": 1.2,
                "end_time": 1.8
            },
            {
                "species": "Myotis daubentonii",
                "common_name": "Daubenton's Bat",
                "scientific_name": "Myotis daubentonii",
                "confidence": 0.76,
                "start_time": 5.5,
                "end_time": 6.2
            },
            {
                "species": "Eptesicus serotinus",
                "common_name": "Serotine",
                "scientific_name": "Eptesicus serotinus",
                "confidence": 0.82,
                "start_time": 10.3,
                "end_time": 11.1
            }
        ]
        
        # Return only detections within duration
        valid_detections = [
            det for det in mock_bats
            if det["start_time"] < duration
        ]
        
        for det in valid_detections:
            if det["end_time"] > duration:
                det["end_time"] = duration
                
        return valid_detections
        
    except Exception as e:
        print(f"Error in bat detection: {e}")
        return []


# Future integration notes:
"""
To integrate real BirdNET model:

1. Install BirdNET:
   pip install birdnetlib

2. Replace detect_birds function with:
   from birdnetlib import Recording
   from birdnetlib.analyzer import Analyzer
   
   analyzer = Analyzer()
   recording = Recording(
       analyzer,
       audio_path,
       lat=59.33,  # Stockholm coordinates
       lon=18.07,
       min_conf=0.7
   )
   recording.analyze()
   return recording.detections

3. For BatDetect2:
   Follow: https://github.com/macaodha/batdetect2
"""
