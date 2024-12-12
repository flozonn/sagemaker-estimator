# Use a lightweight Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /opt/ml/code

# Copy the training script
COPY hello.py /opt/ml/code/hello.py

# Environment variables for SageMaker
ENV SAGEMAKER_PROGRAM=hello.py

ENTRYPOINT ["python", "/opt/ml/code/hello.py"]