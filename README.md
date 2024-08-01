# tracking_numbers
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

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vickramapandian/tracking_numbers.git
   cd tracking_numbers

Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

bash
Copy code
python -m venv env
Activate the Virtual Environment

Windows:

bash
Copy code
.\env\Scripts\activate
macOS/Linux:

bash
Copy code
source env/bin/activate
Install the Requirements

Install the project dependencies using pip:

bash
Copy code
pip install -r requirements.txt

Apply Migrations
Run the following command to apply the migrations:

bash
Copy code
python manage.py migrate

Start the Development Server
Launch the Django development server:

bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

2. Deploy using Docker
Build the Docker Image

Navigate to the project directory and build the Docker image:

Deployment using docker
Build the Docker Image: Run the following command from the root of your project (where your Dockerfile is located):
docker build -t tracking_system .

Run the Docker Container: Once the image is built, run the container using:
docker run -p 8000:8000 tracking_system
This will start the application in a Docker container accessible at http://127.0.0.1:8000/.

Configuration
Environment Variables: Configure the application using environment variables. Use a .env file or pass them directly when running the Docker container.
Database: The default setup uses SQLite for development. You can configure other databases (e.g., PostgreSQL, MySQL) in settings.py for production use.
