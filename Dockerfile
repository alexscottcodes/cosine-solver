# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Add label to link image to repository (important for GHCR)
LABEL org.opencontainers.image.source=https://github.com/alexscottcodes/cosine-solver
LABEL org.opencontainers.image.description="Law of Cosines Triangle Solver with Gradio"
LABEL org.opencontainers.image.licenses=Apache-2.0

# Set working directory
WORKDIR /app

# Install system dependencies required for matplotlib
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the default Gradio port
EXPOSE 7860

# Set environment variable to prevent matplotlib from trying to open display
ENV MPLBACKEND=Agg

# Run the application
CMD ["python", "app.py"]