FROM python:3.11.9-slim
LABEL authors="Jeremias Enriquez"

WORKDIR /code

# Install bash
RUN apt-get update && apt-get install -y bash

# Copy and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the application code
COPY . /code/

# Copy the entrypoint script
COPY entrypoint.sh /code/entrypoint.sh

# Make sure the entrypoint script is executable
RUN chmod +x /code/entrypoint.sh

# Use the entrypoint.sh for starting the container
ENTRYPOINT ["/bin/sh", "/code/entrypoint.sh"]
