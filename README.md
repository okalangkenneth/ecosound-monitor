# EcoSound Monitor

**Automated Wildlife Compliance Platform for Renewable Energy**

A full-stack demo application showcasing automated bat and bird monitoring for wind farms using audio-based ML detection.

## 🎯 Project Overview

This MVP demonstrates:
- ✅ Full-stack Python (FastAPI) + React development
- ✅ Machine Learning integration (BirdNET for audio classification)
- ✅ Real-time audio processing and species detection
- ✅ Interactive data visualization (charts, tables)
- ✅ Compliance report generation (PDF)
- ✅ Domain expertise in wildlife monitoring for renewable energy

## 🏗️ Architecture

```
ecosound-monitor/
├── backend/           # FastAPI server with ML detection
│   ├── api/          # REST API endpoints
│   ├── models/       # Database models (SQLAlchemy)
│   ├── services/     # BirdNET & bat detection services
│   └── uploads/      # Audio file storage
├── frontend/         # React dashboard
│   └── src/
│       ├── components/
│       └── App.jsx
└── demo_audio/       # Sample audio files
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- pip and npm

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend will run at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at: `http://localhost:3000`

## 📋 Features

### 1. Audio Upload & Processing
- Drag-and-drop audio file upload
- Supports WAV, MP3, FLAC, OGG formats
- Real-time processing feedback

### 2. Automated Species Detection
- **BirdNET** integration for European bird species
- Simulated bat detection (Pipistrellus, Myotis, etc.)
- Confidence scoring for each detection
- Timestamp tracking

### 3. Interactive Dashboard
- Real-time statistics (recordings, detections, unique species)
- Species frequency charts (top 10 detected species)
- Bird vs. Bat distribution pie chart
- Detailed detections table with sorting/filtering

### 4. Compliance Reports
- PDF generation with detection summary
- Regulatory compliance format
- Downloadable reports per recording

## 🔧 Tech Stack

**Backend:**
- FastAPI - Modern Python web framework
- BirdNET - Pre-trained bird audio classification
- Librosa - Audio signal processing
- SQLAlchemy - ORM for SQLite database
- ReportLab - PDF generation

**Frontend:**
- React 18 - UI framework
- Vite - Build tool
- TailwindCSS - Styling
- Recharts - Data visualization
- Axios - HTTP client
- React Dropzone - File uploads

## 📊 Use Case: Wind Farm Compliance

This platform addresses a critical need in the renewable energy sector:

**Problem:** Wind farms in EU countries must monitor wildlife (birds/bats) to comply with environmental regulations. Traditional manual surveys are expensive and time-consuming.

**Solution:** Automated audio-based monitoring using ML to:
1. Deploy acoustic sensors at wind farm sites
2. Continuously record environmental audio
3. Automatically identify species using ML models
4. Generate regulatory compliance reports
5. Alert operators to high-risk periods

**Market:** Sweden, Norway, Denmark, Germany have extensive wind farm development and strict environmental regulations.

## 🎯 Demo Workflow

1. **Upload Audio** - Drop a bird/bat audio recording
2. **Automatic Processing** - BirdNET analyzes for species
3. **View Results** - See detections in dashboard
4. **Generate Report** - Download PDF compliance report

## 📝 API Endpoints

### Audio Processing
- `POST /api/audio/upload` - Upload and analyze audio
- `GET /api/audio/recordings` - List all recordings
- `GET /api/audio/detections/{id}` - Get detections for recording
- `GET /api/audio/stats` - Overall statistics

### Reports
- `GET /api/reports/generate/{id}` - Generate PDF report

## 🔮 Production Roadmap

**Current MVP includes:**
- Basic audio upload and detection
- Simple dashboard and visualization
- PDF report generation

**Production version would add:**
- Real BatDetect2 integration (not simulated)
- Real-time streaming from field sensors
- Advanced audio analytics (spectrograms, sonograms)
- Multi-site management
- User authentication & roles
- Regulatory compliance templates (EU directives)
- Alert system for endangered species
- Integration with wind turbine control systems

- Mobile app for field technicians
- Cloud deployment (AWS/GCP)

## 🧪 Testing the Demo

### Get Sample Audio Files

Download bird audio from Xeno-Canto:
https://xeno-canto.org/

Or use these pre-recorded samples:
- European Robin: https://xeno-canto.org/600000
- Common Pipistrelle (bat): Research datasets

### Expected Results

Upload a bird audio file and you should see:
- Species detections with confidence scores
- Timeline of detections
- Visual charts showing species distribution
- Downloadable PDF report

## 🎓 What This Demonstrates

**Technical Skills:**
- Full-stack web development (Python + React)
- RESTful API design
- Machine Learning model integration
- Audio signal processing
- Data visualization
- PDF generation
- Database design (SQLAlchemy)
- Modern React patterns (hooks, state management)
- Responsive UI design (TailwindCSS)

**Domain Knowledge:**
- Wildlife monitoring regulations
- Renewable energy compliance
- Bioacoustics (audio-based wildlife detection)
- European bat and bird species
- Environmental impact assessment

## 📧 Contact

Built by Kenneth as an MVP demonstration for eco-tech opportunities in wildlife compliance.

---

**Note:** This is a demo/MVP. Bat detection is currently simulated. Production version would integrate BatDetect2 or similar validated models.
