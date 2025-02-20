#!/bin/bash

# $1 is the name of the container that needs to be started 
# $2 is the name of the port that container is going to be running on

CONTAINER_NAME=$1 
IMAGE_NAME=$1          

if [ "$(docker ps -a --filter name=^/${CONTAINER_NAME}$ --format '{{.Names}}')" == "$CONTAINER_NAME" ]; then
    echo "Container '$CONTAINER_NAME' exists. Starting it..."
    sudo docker start "$CONTAINER_NAME"
else
    echo "Container '$CONTAINER_NAME' does not exist. Creating and running it..."
    sudo docker run -d -p $2:80  --name "$CONTAINER_NAME" "$IMAGE_NAME"
fi
