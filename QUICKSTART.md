# EcoSound Monitor - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (First Time Only)

**Option A - Automatic (Windows):**
```bash
# Double-click: install.bat
```

**Option B - Manual:**
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### Step 2: Start the Application

**Option A - Automatic (Windows):**
```bash
# Double-click: start.bat
```

**Option B - Manual:**
```bash
# Terminal 1 - Backend
cd backend
python main.py

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

### Step 3: Open Your Browser

- **Frontend:** http://localhost:3000
- **API Docs:** http://localhost:8000/docs

### Step 4: Test with Sample Audio

1. Go to https://xeno-canto.org/
2. Search for "European Robin"
3. Download any MP3 recording
4. Drag & drop into EcoSound Monitor
5. Watch the magic happen! ✨

## ✅ What to Expect

After uploading audio, you'll see:
- ✅ Automated species detection
- ✅ Confidence scores for each detection
- ✅ Interactive charts and visualizations
- ✅ Downloadable PDF compliance report

## 🎯 Demo This to Jack

See `PRESENTATION_NOTES.md` for talking points!

## 🐛 Troubleshooting

**Backend won't start?**
- Make sure Python 3.9+ is installed
- Try: `pip install --upgrade pip`
- Check: `python --version`

**Frontend won't start?**
- Make sure Node.js 16+ is installed
