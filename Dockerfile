# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Start the app with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
