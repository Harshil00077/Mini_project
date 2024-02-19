# Use the latest Ubuntu base image
FROM ubuntu:latest

# Install Python
RUN apt-get update && apt-get install -y python3

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY calculator.py /app/calculator.py

# Command to execute the Python script
CMD ["python3", "calculator.py"]
