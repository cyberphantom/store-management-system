# Store Management System
## Overview

The Store Management System is a web-based application designed for efficiently managing inventory, purchases, and item insertion for a store. It utilizes FastAPI for the backend, featuring a responsive front-end design suitable for handling store operations. The application is containerized using Docker, simplifying deployment and scaling.

## Prerequisites

Before setting up the application, ensure you have Docker and Docker Compose installed:

   - Docker: Get Docker
   - Docker Compose: Install Docker Compose

## Installation and Running the App
### 1. Clone the Repository

To get started, clone this repository to your local machine:

bash
```
git clone [URL of your repository]
cd store-management-system
```

2. Build and Run with Docker Compose

From the project's root directory, execute:

bash

docker-compose up --build

This command builds the Docker image and starts the containers as per the configuration in docker-compose.yml.
3. Accessing the Application

Once the containers are up and running, the application can be accessed at:

arduino

http://localhost:8000

4. Stopping the Application

To stop and remove the containers and networks, use:

bash

docker-compose down

Application Structure

    app/: Contains the FastAPI application code and route definitions.
    data/: Directory for JSON data files.
    templates/: HTML templates for the frontend UI.
    static/: Static files such as CSS and JavaScript.
    Dockerfile: Docker image specifications.
    docker-compose.yml: Docker Compose configuration.
    requirements.txt: List of Python dependencies.

Contributing

Your contributions are welcome! Please read the contributing guidelines before submitting pull requests to the project.
License

This project is licensed under the MIT License - see the LICENSE file for details.
