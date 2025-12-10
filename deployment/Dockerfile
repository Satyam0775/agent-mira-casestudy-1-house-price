# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies (if needed for pandas / numpy)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r deployment/requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run API server
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
