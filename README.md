# Axmed Medication SKU Catalogue

## Descripción

Axmed es una plataforma destinada a acelerar el acceso a la atención médica y farmacéutica en países de ingresos bajos y medianos (LMICs). Esta aplicación permite gestionar un catálogo de SKUs de medicamentos, facilitando operaciones CRUD y carga masiva de datos.

## Funcionalidades

- **CRUD de SKUs**: Crear, leer, actualizar y eliminar SKUs de medicamentos.
- **Carga Masiva**: Subir múltiples SKUs a través de un endpoint dedicado.
- **Validación de Unicidad**: Asegura que no existan SKUs duplicados, incluso con nombres INN similares.
- **Monitoreo**: Integración con Prometheus y Grafana para monitoreo de métricas.
- **Tareas Asíncronas**: Envío automático de correos electrónicos cada 24 horas utilizando Celery.
- **Despliegue**: Dockerización y despliegue en la nube (Heroku).

## Tecnologías Utilizadas

- **Backend**: Django, Django REST Framework
- **Base de Datos**: PostgreSQL
- **Tareas Asíncronas**: Celery
- **Monitoreo**: Prometheus, Grafana
- **Contenerización**: Docker, Docker Compose
- **Despliegue**: Heroku

## Instalación Local

### **Requisitos**

- Docker y Docker Compose instalados.
- Cuenta de correo para configurar el envío de emails.

### **Pasos**

1. **Clonar el Repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/axmed_catalogue.git
   cd axmed_catalogue
   ```

2. **Crear el Archivo `.env`**:

   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```env
   # Secret Key
   DJANGO_SECRET_KEY=tu_clave_secreta_aqui

   # Debug Mode
   DEBUG=True

   # Allowed Hosts
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Database Configuration
   DB_NAME=axmed_db
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
   DB_HOST=db
   DB_PORT=5432

   # Email Configuration
   EMAIL_HOST_USER=tu_email@gmail.com
   EMAIL_HOST_PASSWORD=tu_contraseña
   DEFAULT_FROM_EMAIL=tu_email@gmail.com

   # Celery Configuration
   CELERY_BROKER_URL=redis://redis:6379/0
   ```

   > **Nota**: Reemplaza los valores con tus propias configuraciones.

3. **Construir y Ejecutar los Contenedores**:

   ```bash
   docker-compose up --build
   ```

4. **Aplicar Migraciones y Crear Superusuario**:

   En otra terminal, ejecuta:

   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Acceder a la Aplicación**:

   - **API**: `http://localhost:8000/api/`
   - **Admin**: `http://localhost:8000/admin/`
   - **Metrics**: `http://localhost:8000/metrics/`

## Pruebas

Ejecutar las pruebas con `pytest`:

```bash
docker-compose exec web pytest
```
