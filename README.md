# Docker Flask MongoDB Tutorial

A comprehensive Docker tutorial for setting up a Flask web application with MongoDB and Mongo Express on Docker Compose.

## Overview

This project demonstrates how to containerize a Flask application with MongoDB using Docker and Docker Compose. It provides a complete development environment with:

- **Flask**: A lightweight Python web framework
- **MongoDB**: A NoSQL document database
- **Mongo Express**: A web-based MongoDB admin interface

## Prerequisites

- Debian 12 (Bookworm)
- Docker and Docker Compose installed

## Quick Start

1. Clone this repository:
```bash
git clone https://github.com/shahinabdi/Docker-DockerCompose.git
cd Docker-DockerCompose
```

2. Build and start the containers:
```bash
docker compose build
docker compose up -d
```

3. Access the applications:
   - Flask App: http://localhost:5000
   - Mongo Express: http://localhost:8081 (username: admin, password: pass)

## Features

- Complete Docker setup for local development
- Flask REST API with MongoDB integration
- Web-based MongoDB management interface
- Connection retry logic for service dependencies
- Health checks for all services
- Volume persistence for MongoDB data

## API Endpoints

- `GET /`: Welcome message
- `GET /todos`: List all todo items
- `POST /todos`: Create a new todo item (JSON payload: `{"task": "Task description"}`)

## Project Structure

```
.
├── app.py                  # Flask application
├── Dockerfile              # Flask container definition
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Services definition
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Shahin ABDI - [GitHub](https://github.com/shahinabdi)