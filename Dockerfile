# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el código
COPY . /app/

# Exponer el puerto
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "axmed_catalogue.wsgi:application", "--bind", "0.0.0.0:8000"]
