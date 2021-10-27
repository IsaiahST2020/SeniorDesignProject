# syntax=docker/dockerfile:1

FROM python:3.9.7-slim-buster
ENV PYTHONUNBUFFERED=1

# The directory for our code will be in /app
WORKDIR /app

# Installing required libraries
COPY requirements.txt .
RUN pip install -r /app/requirements.txt

# Copying over files
COPY . .

# Mounting spaces with data we prefer to keep
VOLUME [ "/app/data", "/app/uploads" ]

# Exposing port
EXPOSE 8000

# RUnning application
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
