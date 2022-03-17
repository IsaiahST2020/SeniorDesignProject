# syntax=docker/dockerfile:1
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-alpine

# Exposing port
EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Creating environment variables
ENV OCTOPRINT_URL=http://0.0.0.0:80
ENV OCTOPRINT_APIKEY=ABCD1234

# Installing required libraries
RUN apk add gcc libffi-dev libc-dev cargo libressl-dev
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Removing alpine packages that are no longer needed
RUN apk del gcc libffi-dev libc-dev cargo libressl-dev

# The directory for our code will be in /app
WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Mounting spaces with data we prefer to keep
VOLUME [ "/app/data", "/app/uploads", "/app/cert" ]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "python3", "manage.py", "runserver_plus", "--cert-file", "cert/cert.pem", "--key-file", "cert/key.pem", "0.0.0.0:8000" ]
