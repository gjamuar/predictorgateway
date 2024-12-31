# Flask Docker Project

## Overview
This project demonstrates how to set up a Flask application with Docker and Gunicorn. It also includes a Poetry-based dependency management system, pytest for testing, and Flake8 for linting.

## Prerequisites
- Python 3.12
- Docker
- Poetry

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd flask_docker_project
```

### 2. Set Up the Virtual Environment
Run the setup script:
```bash
make setup
```
This will:
- Create a virtual environment.
- Install dependencies using Poetry.

Activate the environment:
```bash
source venv/bin/activate
```

### 3. Lint the Code
Run Flake8 to check for code issues:
```bash
make lint
```

### 4. Automatically Fix Lint Issues
Run autopep8 to fix lint issues:
```bash
make lint-fix
```

### 5. Run Tests
Run pytest to test the application:
```bash
make test
```

### 6. Run Locally
Run the Flask application locally:
```bash
python run.py
```
Access the application at `http://127.0.0.1:9900`.

### 7. Run with Docker
#### Build the Docker Image
```bash
make run-docker
```
#### Run with a Custom Port
```bash
docker run -e PORT=8080 -p 8080:8080 flask-docker-project
```
Access the application at `http://127.0.0.1:8080`.

### 8. Check Logs
To view logs from the running Docker container:
```bash
make logs
```

### 9. Clean Up
Remove the virtual environment:
```bash
make clean
```
Remove the Docker image:
```bash
make docker-clean
```

