# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the 'requirements.txt' file first for caching purposes
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app will run on (if it's a web service, e.g., Flask or Django)
EXPOSE 5000

# Set the environment variables for Flask/Django or other app configurations
# For Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# For Django, you can set the Django settings module
# ENV DJANGO_SETTINGS_MODULE=myapp.settings

# Command to run your app (adjust based on how your app is started)
CMD ["flask", "run", "--host=0.0.0.0"]
