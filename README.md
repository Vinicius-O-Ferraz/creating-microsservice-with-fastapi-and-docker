# To-Do List API with FastAPI and Docker

<div align="center">
  <img src="https://github.com/user-attachments/assets/26aae67a-b12c-4567-903c-58239fa18798" alt="image1" style="display: inline-block; margin-right: 10px;" />
  <img src="https://th.bing.com/th/id/OIP.prk6qAKISi1DadSaKgKZlwHaCq?w=345&h=126&c=7&r=0&o=5&dpr=1.1&pid=1.7" alt="image2" style="display: inline-block; margin-left: 10px;" />
</div>



This repository contains the source code for a To-Do List API built using FastAPI. The application is designed to manage a simple to-do list with functionalities for creating, reading, updating, and deleting tasks (CRUD operations). This API will be transformed into a microservice and deployed using Docker.

# Features
* FastAPI framework for fast and efficient API development.
* CRUD operations for managing tasks.
* Dockerized for easy deployment as a microservice.
* Dependency Injection and modular architecture to allow future extensions.
* Asynchronous capabilities for improved performance.
* Pydantic models for request validation.

# Getting Started
To run the API locally or as a Docker container, follow the instructions below.

# Prerequisites
* Python 3.8+
* Docker

# Running the API Locally
Clone the repository:
`git clone https://github.com/Vinicius-O-Ferraz/creating-microsservice-with-fastapi-and-docker.git`
`cd ./src`

# Install the dependencies:

`pip install -r requirements.txt`

# Run the FastAPI server:

`uvicorn app.main:app --reload`

Access the API documentation: Visit http://127.0.0.1:8000/docs to interact with the API using the Swagger UI.

