# Use an official Python runtime as a parent image
FROM python:3.9-slim as builder

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set build directory
WORKDIR /install

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Set the working directory
WORKDIR /processing

# Copy requirements.txt
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start a new, final image to keep it clean of build-deps
FROM python:3.9-slim

# Make sure we use the non-root user so that it's less likely to get hacked
RUN useradd app
USER app

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /processing

# Copy the dependencies
COPY --from=builder /install /usr/local

# Copy the content of the local src directory to the working directory
COPY ./processing .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run langchain_integration.py when the container launches
CMD ["python", "langchain_integration.py"]
