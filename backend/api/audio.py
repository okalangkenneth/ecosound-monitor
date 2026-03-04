from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import os
import librosa
from datetime import datetime

from models.database import AudioRecording, Detection, get_db
from ml_models.birdnet_detector import detect_birds

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload and process an audio file"""
    
    # Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Get audio metadata
    try:
        y, sr = librosa.load(file_path, sr=None)
        duration = librosa.get_duration(y=y, sr=sr)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing audio: {str(e)}")
    
    # Create database record
    recording = AudioRecording(
        filename=file.filename,
        file_size=len(content),
        duration=duration,
        sample_rate=sr,
        file_metadata={"format": file.content_type}  # Updated to use file_metadata
    )
    db.add(recording)
    db.commit()
    db.refresh(recording)
    
    # Run bird detection
    try:
        detections = detect_birds(file_path)
        
        # Save detections to database
        for det in detections:
            detection = Detection(
                recording_id=recording.id,
                species_name=det["species"],
                common_name=det["common_name"],
                scientific_name=det["scientific_name"],
                confidence=det["confidence"],
                start_time=det["start_time"],
                end_time=det["end_time"],
                detection_type="bird"
            )
            db.add(detection)
        
        db.commit()
    except Exception as e:
        print(f"Detection error: {e}")
        # Continue even if detection fails
    
    return {
        "id": recording.id,
        "filename": recording.filename,
        "duration": recording.duration,
        "detections": len(detections) if 'detections' in locals() else 0
    }

@router.get("/recordings")
def get_recordings(db: Session = Depends(get_db)):
    """Get all recordings"""
    recordings = db.query(AudioRecording).all()
    
    results = []
    for rec in recordings:
        detection_count = len(rec.detections)
        species_count = len(set(d.species_name for d in rec.detections))
        
        results.append({
            "id": rec.id,
            "filename": rec.filename,
            "duration": rec.duration,
            "created_at": rec.created_at.isoformat(),
            "detection_count": detection_count,
            "species_count": species_count
        })
    
    return results

@router.get("/recordings/{recording_id}")
def get_recording_detail(recording_id: int, db: Session = Depends(get_db)):
    """Get detailed information about a recording"""
    recording = db.query(AudioRecording).filter(AudioRecording.id == recording_id).first()
    
    if not recording:
        raise HTTPException(status_code=404, detail="Recording not found")
    
    detections = []
    for det in recording.detections:
        detections.append({
            "id": det.id,
            "species": det.species_name,
            "common_name": det.common_name,
            "scientific_name": det.scientific_name,
            "confidence": det.confidence,
            "start_time": det.start_time,
            "end_time": det.end_time,
            "type": det.detection_type
        })
    
    return {
        "id": recording.id,
        "filename": recording.filename,
        "duration": recording.duration,
        "sample_rate": recording.sample_rate,
        "created_at": recording.created_at.isoformat(),
        "detections": detections
    }

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    """Get overall statistics"""
    total_recordings = db.query(AudioRecording).count()
    total_detections = db.query(Detection).count()
    
    # Get bird and bat counts
    bird_detections = db.query(Detection).filter(Detection.detection_type == "bird").count()
    bat_detections = db.query(Detection).filter(Detection.detection_type == "bat").count()
    
    # Get unique species
    unique_species = db.query(Detection.species_name).distinct().all()
    species_count = len(unique_species)
    
    # Get species frequency
    species_freq = {}
    for species_name in unique_species:
        count = db.query(Detection).filter(Detection.species_name == species_name[0]).count()
        species_freq[species_name[0]] = count
    
    return {
        "total_recordings": total_recordings,
        "total_detections": total_detections,
        "bird_detections": bird_detections,
        "bat_detections": bat_detections,
        "unique_species": species_count,
        "species_frequency": species_freq
    }
