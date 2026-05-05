# EcoSound Monitor

![CI](https://github.com/okalangkenneth/ecosound-monitor/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)

**Automated Wildlife Compliance Platform for Renewable Energy**

A full-stack application for automated bat and bird monitoring at wind farms using
audio-based ML detection. Helps operators comply with EU wildlife regulations without
costly manual surveys.

## Docker Quick Start

### Standard (Bird detection — recommended for most users, ~800MB)

```bash
git clone https://github.com/okalangkenneth/ecosound-monitor.git
cd ecosound-monitor
docker compose up --build
```

Open http://localhost:3000 — done.

### Full (Bird + Bat detection, ~5.8GB — requires ultrasonic recorder >=192kHz)

```bash
docker compose --profile full up --build
```

Bat detection requires an ultrasonic recorder (e.g. AudioMoth, Pettersson D500X).
Standard microphones will not capture bat echolocation calls.

## Project Overview

- Full-stack Python (FastAPI) + React development
- Machine Learning integration (BirdNET for bird audio classification)
- Real bat detection via BatDetect2 (requires ultrasonic audio >=192kHz)
- Real-time audio processing and species detection
- Interactive data visualization (charts, tables)
- Compliance report generation (PDF)
- Domain expertise in wildlife monitoring for renewable energy

## Architecture

```
ecosound-monitor/
├── backend/           # FastAPI server with ML detection
│   ├── api/          # REST API endpoints
│   ├── models/       # Database models (SQLAlchemy)
│   ├── services/     # BirdNET & BatDetect2 detection services
│   └── tests/        # pytest test suite
├── frontend/         # React dashboard
│   └── src/
│       ├── components/
│       └── App.jsx
└── demo_audio/       # Sample audio sources
```

## Manual Setup

### Prerequisites
- Python 3.10+
- Node.js 18+

### Backend

```bash
cd backend
pip install -r requirements-lite.txt
python main.py
```

Backend: http://localhost:8000 | API docs: http://localhost:8000/docs

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

## Features

### 1. Audio Upload and Processing
- Drag-and-drop audio file upload
- Supports WAV, MP3, FLAC, OGG formats
- Real-time processing feedback

### 2. Automated Species Detection
- BirdNET integration for European bird species
- BatDetect2 for bat echolocation calls (ultrasonic audio required, full image only)
- Confidence scoring for each detection
- Timestamp tracking

### 3. Interactive Dashboard
- Real-time statistics (recordings, detections, unique species)
- Species frequency charts (top 10 detected species)
- Bird vs. Bat distribution pie chart
- Detailed detections table with sorting and filtering

### 4. Compliance Reports
- PDF generation with detection summary
- Regulatory compliance format
- Downloadable reports per recording

## Tech Stack

**Backend:** FastAPI · BirdNET (birdnetlib) · BatDetect2 · Librosa · SQLAlchemy · ReportLab

**Frontend:** React 18 · Vite · TailwindCSS · Recharts · Axios

## Use Case: Wind Farm Compliance

Wind farms in EU countries (Sweden, Norway, Denmark, Germany) must monitor wildlife
to comply with environmental regulations. EcoSound Monitor automates this by:

1. Processing acoustic sensor recordings from the field
2. Identifying bird and bat species via ML models
3. Generating regulatory compliance PDF reports

## API Endpoints

- POST /api/audio/upload — Upload and analyze audio
- GET /api/audio/recordings — List all recordings
- GET /api/audio/detections/{id} — Get detections for a recording
- GET /api/audio/stats — Overall statistics
- GET /api/reports/generate/{id} — Generate PDF compliance report

## Running Tests

```bash
pytest backend/tests/ -v
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions and contribution guidelines.

## License

MIT — see [LICENSE](LICENSE)
