# EcoSound Monitor - Backend

## Setup Instructions

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: http://localhost:8000

### 3. API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Audio Processing
- `POST /api/audio/upload` - Upload and analyze audio file
- `GET /api/audio/recordings` - Get all recordings
- `GET /api/audio/detections/{recording_id}` - Get detections for a recording
- `GET /api/audio/stats` - Get overall statistics

### Reports
- `GET /api/reports/generate/{recording_id}` - Generate PDF compliance report

## Technologies Used

- **FastAPI** - Modern Python web framework
- **BirdNET** - Bird species detection
- **Librosa** - Audio processing
- **SQLAlchemy** - Database ORM
- **ReportLab** - PDF generation
