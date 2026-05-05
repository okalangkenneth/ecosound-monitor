# Contributing to EcoSound Monitor

Thank you for your interest in contributing to EcoSound Monitor — an open source
automated wildlife compliance platform for wind farms and renewable energy projects.

## Ways to Contribute

- **Bug reports** — open an issue with steps to reproduce
- **Feature requests** — open an issue describing the use case
- **Code** — fix bugs, add features, improve ML models
- **Documentation** — improve README, add examples, write guides
- **Testing** — add test cases, test on different audio formats

## Development Setup

### Option A — Docker (Recommended)

```bash
git clone https://github.com/okalangkenneth/ecosound-monitor.git
cd ecosound-monitor
docker compose up --build
```

Open http://localhost:3000. That's it.

### Option B — Manual

**Backend (Python 3.10+):**
```bash
cd backend
pip install -r requirements.txt
python main.py
```
API runs at http://localhost:8000. Docs at http://localhost:8000/docs.

**Frontend (Node 18+):**
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at http://localhost:3000.

## Submitting a Pull Request

1. Fork the repository
2. Create a branch: `feat/my-feature`, `fix/bug-description`, or `docs/update-readme`
3. Make your changes with clear commit messages
4. Run tests: `pytest backend/tests/ -v`
5. Open a PR against `main` — describe what you changed and why

## Adding a New Species Detection Model

Detection services live in `backend/services/`. Each service follows this interface:

```python
class MyDetectionService:
    def analyze_audio(self, audio_path: str, min_confidence: float = 0.3) -> List[Dict]:
        # Returns list of dicts with keys:
        # species_name, common_name, confidence, timestamp, detection_type
        ...
```

To add a new model (e.g. a custom bat species classifier):
1. Create `backend/services/my_detection.py` implementing the interface above
2. Import and call it from `backend/api/audio.py` alongside the existing services
3. Add any new pip dependencies to `backend/requirements.txt`

## Code Style

- **Python:** [black](https://black.readthedocs.io/) + [ruff](https://docs.astral.sh/ruff/)
- **JavaScript/JSX:** [prettier](https://prettier.io/)

## Running Tests

```bash
pytest backend/tests/ -v
```
