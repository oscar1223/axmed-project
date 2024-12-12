# Axmed Medication SKU Catalogue

## Description

Axmed is a platform designed to accelerate access to healthcare and pharmaceuticals in low- and middle-income countries (LMICs). This application allows the management of a medication SKU catalogue, enabling CRUD operations and bulk data uploads.

## Features

- **SKU CRUD**: Create, read, update, and delete medication SKUs.
- **Bulk Upload**: Upload multiple SKUs through a dedicated endpoint.
- **Uniqueness Validation**: Ensures no duplicate SKUs exist, even with similar INN names.
- **Monitoring**: Integration with Prometheus and Grafana for metrics monitoring.
- **Asynchronous Tasks**: Automatic email sending every 24 hours using Celery.
- **Deployment**: Dockerized and deployed in the cloud (AWS ECR, AWS AppRunner).

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite
- **Asynchronous Tasks**: Celery
- **Monitoring**: Prometheus, Grafana
- **Containerization**: Docker, Docker Compose
- **Deployment**: AWS + GitHub Actions

## Local Installation

### **Requirements**

- Docker and Docker Compose installed.
- An email account for configuring email sending.

### **Steps**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your_user/axmed_catalogue.git
   cd axmed_catalogue
   ```

2. **Create the `.env`** file:

   Create a `.env` file in the root of the project with the following variables:

   ```env
   # Secret Key
   DJANGO_SECRET_KEY=your_secret_key_here

   # Debug Mode
   DEBUG=True

   # Allowed Hosts
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Email Configuration
   EMAIL_HOST_USER=tu_email@gmail.com
   EMAIL_HOST_PASSWORD=your_password
   DEFAULT_FROM_EMAIL=tu_email@gmail.com

   # Celery Configuration
   CELERY_BROKER_URL=redis://redis:6379/0
   ```

   > **Note**: Replace the values with your own settings.

3. **Build and Run Containers**:

   ```bash
   docker-compose up --build
   ```

4. **Apply Migrations and Create Superuser**:

   In another terminal, run:

   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the Application**:

   - **API**: `http://localhost:8000/api/`
   - Admin\*\*: `http://localhost:8000/admin/`
   - **Swagger**: `http://localhost:8000/swagger/`
   - **Redoc**: `http://localhost:8000/redoc/`
   - **Grafana**: `http://localhost:3000`
   - **Prometheus**: `http://localhost:9090`
   - **Autentication**: `http://localhost:8000/token/`

   > **Note**: To make an API request, please check the file: [JSON POSTMAN](axmed.postman_collection.json).

## Testing

Run the tests with `pytest`:

```bash
docker-compose exec web pytest
```

## Bonus

In addition to the additional points that you highlight in the pdf of the technical test, I have added several features to the API to make it more robust and scalable.

1. **JWT**

   I have added Json Web Token for user authentication when using the API, for this you must create a superuser in Django.

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

2. **Swagger && Redoc**

   I have added Swagger to improve the backend development and presentation of the api, along with Redoc.

   - **Swagger**: `http://localhost:8000/swagger/`
   - **Redoc**: `http://localhost:8000/redoc/`

3. **Prometheus && Grafana**

   I have also added monitoring applications for debugging, maintenance and real-time API statistics.

   - **Grafana**: `http://localhost:3000`
   - **Prometheus**: `http://localhost:9090`
