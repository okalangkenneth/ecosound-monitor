from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./audio_monitoring.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class AudioRecording(Base):
    __tablename__ = "audio_recordings"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_size = Column(Integer)
    duration = Column(Float)
    sample_rate = Column(Integer)
    file_metadata = Column(JSON)  # Renamed from 'metadata' to avoid SQLAlchemy reserved word conflict
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    detections = relationship("Detection", back_populates="recording")

class Detection(Base):
    __tablename__ = "detections"
    
    id = Column(Integer, primary_key=True, index=True)
    recording_id = Column(Integer, ForeignKey("audio_recordings.id"))
    species_name = Column(String, nullable=False)
    common_name = Column(String)
    scientific_name = Column(String)
    confidence = Column(Float)
    start_time = Column(Float)
    end_time = Column(Float)
    detection_type = Column(String)  # 'bird' or 'bat'
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    recording = relationship("AudioRecording", back_populates="detections")

# Initialize database function
def init_db():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)

# Dependency for database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
