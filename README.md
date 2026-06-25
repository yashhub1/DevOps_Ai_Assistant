# DevOps AI Assistant

An AI-powered chatbot built with Python and OpenAI API.

## Features
- AI chatbot using OpenAI API
- Dockerized application
- GitHub Actions CI pipeline
- Automatic Docker Hub image push
- AWS EC2 deployment

## Technologies Used
- Python
- OpenAI API
- Docker
- GitHub Actions
- Docker Hub
- AWS EC2
- Linux

## Run Locally

```bash
docker build -t aiassistant .
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY aiassistant
```

## CI Pipeline

Every push to the `main` branch:
- Builds the Docker image
- Pushes the image to Docker Hub automatically

## Author

Yash
