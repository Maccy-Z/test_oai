FROM python:3.11-slim

WORKDIR /var/task

# Copy your application code
COPY ./api ./api

# Copy and install dependencies (make sure uvicorn is listed in requirements.txt)
COPY requirements.txt .
RUN pip3 install -r requirements.txt -U --no-cache-dir

# Expose the port Uvicorn will listen on
EXPOSE 8000

# Launch Uvicorn instead of the Lambda handler
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
