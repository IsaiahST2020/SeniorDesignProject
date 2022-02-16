# syntax=docker/dockerfile:1

FROM python:3.9-alpine
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

# Creating environment variables
ENV OCTOPRINT_URL=http://0.0.0.0:80
ENV OCTOPRINT_APIKEY=ABCD1234

# Ensure that the database is properly migrated
RUN python3 manage.py migrate

# RUnning application
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
