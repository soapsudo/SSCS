#!/bin/bash

# $1 is the name of the image that needs to be deleted
CONTAINER_NAME=$1 
IMAGE_NAME=$1          

# Check if the container is running
if [ "$(docker ps --filter name=^/${CONTAINER_NAME}$ --format '{{.Names}}')" == "$CONTAINER_NAME" ]; then
    echo "Container '$CONTAINER_NAME' is running. Stopping it..."
    sudo docker stop "$CONTAINER_NAME"
fi

# Check if the container exists before removing
if [ "$(docker ps -a --filter name=^/${CONTAINER_NAME}$ --format '{{.Names}}')" == "$CONTAINER_NAME" ]; then
    echo "Removing container '$CONTAINER_NAME'..."
    sudo docker rm "$CONTAINER_NAME" --force
else
    echo "Container '$CONTAINER_NAME' does not exist."
fi

# Check if the image exists before removing
if [ "$(docker images -q $IMAGE_NAME)" ]; then
    echo "Removing image '$IMAGE_NAME'..."
    sudo docker rmi "$IMAGE_NAME" --force
else
    echo "Image '$IMAGE_NAME' does not exist."
fi

cd ..

sudo rm -r $1