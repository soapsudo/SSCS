#!/bin/bash

# $1 is the name of the container that needs to be stopped

CONTAINER_NAME=$1  # Change this to your container name

# Check if the container is running
if [ "$(docker ps --filter name=^/${CONTAINER_NAME}$ --format '{{.Names}}')" == "$CONTAINER_NAME" ]; then
    echo "Container '$CONTAINER_NAME' is running. Stopping it..."
    sudo docker stop "$CONTAINER_NAME"
else
    echo "Container not started"
fi
