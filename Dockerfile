# Flask app ke liye base image
FROM python:3.12-slim

# Work directory set karna
WORKDIR /app

# Dependencies copy karna
COPY requirements.txt .

# Install karna dependencies
RUN pip install --no-cache-dir -r requirements.txt

# App ko copy karna
COPY . .

# Flask app ko expose karna
EXPOSE 5000

# App run karna
CMD ["python", "run.py"]
