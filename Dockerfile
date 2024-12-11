# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /app

# Installation of dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy code
COPY . /app/

# Exposing the port
EXPOSE 8000

# Default command
CMD ["gunicorn", "axmed_catalogue.wsgi:application", "--bind", "0.0.0.0:8000"]
