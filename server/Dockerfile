# Use the official Python 3.9 image as the base image
FROM python:3.11-slim

# Copy the requirements file into the container and install dependencies
COPY src/ app/
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Expose port 8080 for external access
EXPOSE 8080

# Set the environment variable for the port
ENV PORT 8080

# Define the command to start your application with Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app