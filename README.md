# Tracking Number Generator

This project is a Django-based REST API for generating unique tracking numbers, designed to handle high concurrency and ensure scalability. This application can be deployed either using pip for a virtual environment setup or Docker for containerization.

## Features

- **Uniqueness**: Each tracking number is unique.
- **Scalability**: Can handle high concurrency and scale horizontally.
- **Efficiency**: Quick generation without bottlenecks.
- **Fault Tolerance**: Resilient to failures, ensuring no duplicate tracking numbers.

## Prerequisites

- Python 3.8 or higher
- Docker (for Docker deployment)
- Git

## Deployment Options

### 1. Deploy using pip

1.1. **Clone the Repository**

   ```
   git clone https://github.com/vickramapandian/tracking_numbers.git
   cd tracking_numbers
   ```

1.2. **Set Up a Virtual Environment**

It's recommended to use a virtual environment to manage dependencies.

    python -m venv env

    Activate the Virtual Environment

    Windows:

    .\env\Scripts\activate

    macOS/Linux:

    source env/bin/activate

1.3. **Install the Requirements**

Install the project dependencies using pip:

    pip install -r requirements.txt

1.4. **Apply Migrations**

Run the following command to apply the migrations:

    python manage.py migrate


1.5. **Launch the Django development server:**

    python manage.py runserver
    The API will be available at http://127.0.0.1:8000/.

### 2. Deploy using Docker
Build the Docker Image

Navigate to the project directory and build the Docker image:

Deployment using docker
Build the Docker Image: Run the following command from the root of your project (where your Dockerfile is located):

    docker build -t tracking_system .

Run the Docker Container: Once the image is built, run the container using:

    docker run -p 8000:8000 tracking_system

This will start the application in a Docker container accessible at http://127.0.0.1:8000/.

### Configuration
Environment Variables: Configure the application using environment variables. Use a .env file or pass them directly when running the Docker container.
Database: The default setup uses SQLite for development. You can configure other databases (e.g., PostgreSQL, MySQL) in settings.py for production use.

### POST Request

You can test the API endpoint using a tool like curl or Postman:

    curl -X POST http://127.0.0.1:8000/tracking/generate/

This will return a JSON response with the newly generated tracking number:

    {
        "id": 1,
        "uuid": "a unique UUID",
        "created_at": "2024-08-01T12:00:00Z"
    }

### Final Notes
Database: Using a PostgreSQL database with Django ensures that auto-incrementing IDs are unique even under high concurrency.
UUID: Using a UUID field guarantees uniqueness across distributed systems, even if IDs are reset.
DRF: Django REST Framework simplifies the creation of RESTful APIs, providing serializers and views to handle requests and responses efficiently.
This setup creates a scalable and efficient system for generating unique tracking numbers using Django and Django REST Framework. Adjust the configuration and optimize as needed based on your specific scalability and performance requirements.