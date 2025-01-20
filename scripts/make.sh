#!/bin/bash

# $1 is the type of the container
# $2 is the name of the container

cd ..

sudo mkdir $1

cd $1

touch Dockerfile



docker build -t $1:1.0 .