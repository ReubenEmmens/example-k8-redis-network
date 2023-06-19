# Use an official Python runtime as the base image
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Install Redis Server
RUN apt update && apt upgrade -y

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the working directory
COPY main.py .

# Run the Python script when the container starts
CMD ["python", "main.py"]
