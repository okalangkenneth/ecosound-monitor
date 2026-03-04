from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from pathlib import Path
from datetime import datetime
import json

from api.audio import router as audio_router
from api.reports import router as reports_router
from models.database import init_db, get_db

app = FastAPI(
    title="EcoSound Monitor API",
    description="Automated Wildlife Compliance Platform for Renewable Energy",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Include routers
app.include_router(audio_router, prefix="/api/audio", tags=["audio"])
app.include_router(reports_router, prefix="/api/reports", tags=["reports"])

@app.get("/")
async def root():
    return {
        "message": "EcoSound Monitor API",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
