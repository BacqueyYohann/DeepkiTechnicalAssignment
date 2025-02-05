# Use an official lightweight Python image
FROM python:3.10-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    cmake \
    swig \
    g++ \
    libssl-dev \
    python3-dev \
    protobuf-compiler \
    build-essential \
    libgeos-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Force a manual installation of s2geometry from PyPI
#RUN pip install --no-cache-dir --force-reinstall --no-binary :all: s2geometry==0.9.0


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to include the directory with the .so files
#ENV LD_LIBRARY_PATH=/usr/local/lib/python3.10/site-packages/s2geometry:$LD_LIBRARY_PATH

# Command to run your project (modify as needed)
CMD ["python", "main.py"]