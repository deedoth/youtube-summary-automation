FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app.py .

# Install Python deps
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
