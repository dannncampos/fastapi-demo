# FastAPI Demo

- Version: 0.1
- Author: Daniel Campos
- Date: 14/06/2021

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## What we are going to test?

- **Get and Post** => The basic calls of an API.
- **Data Validation** => Using Pydantic we can build base models to validate inputs and outputs
- **Asynchronous** => Uvicorn has ASGI (Asynchronous Server Gateway Interface), that is a successor to WSGI. We will yeild a large expense of data to test the async function.
- **Swagger Documentation** => FastAPI supports Swagger documentation as native.
- **Redoc Documentation** => FastAPI supports Redoc documentation as native.


## Disclaimer

This project is based on how to use the Fast API and test its features over DJango and Flask.

### Build Server

    docker-compose build && docker-compose up -d

### Testing FastAPI

After building the docker image and creating the container, access the address in your browser for Swagger documentations: http://127.0.0.1/docs and for Redoc documentations: http://127.0.0.1/redoc

### Load Tests

$ pytest {arquivo}