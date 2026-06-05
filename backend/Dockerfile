# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# Docker Image bilden => docker build -t project-forum-backend .
# STARTEN mit Docker => docker run -p 8000:8000 project-forum-backend
