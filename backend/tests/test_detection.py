import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app
from services.bird_detection import BirdDetectionService
from services.bat_detection import BatDetectionService

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data


def test_bird_detection_service_init():
    service = BirdDetectionService()
    assert service is not None
    assert service.analyzer is not None


def test_bat_detection_service_init():
    service = BatDetectionService()
    assert service is not None


def test_bat_detection_nonexistent_file_returns_empty_list():
    """BatDetectionService must never raise — returns [] on any error."""
    service = BatDetectionService()
    result = service.analyze_audio("/nonexistent/path/audio.wav")
    assert isinstance(result, list)
    assert len(result) == 0


def test_recordings_endpoint_returns_list():
    response = client.get("/api/audio/recordings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
