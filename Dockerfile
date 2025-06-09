# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the FastAPI port (e.g., 8000)
EXPOSE 8000

# Run your FastAPI app (edit this based on your entry point)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]