# Container image that runs your code
FROM python:3.11-alpine

RUN pip install openai

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY src/ /app/

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "/app/main.py"]
