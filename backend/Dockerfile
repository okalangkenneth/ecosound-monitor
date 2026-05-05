FROM python:3.10-slim

# System dependencies for audio processing and ML
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    libgomp1 \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir batdetect2

# Copy application code
COPY . .

# Create directories for uploads and reports
RUN mkdir -p uploads reports

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
