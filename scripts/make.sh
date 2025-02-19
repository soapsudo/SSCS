#!/bin/bash

# $1 is the type of the container
# $2 is the name of the container

cd ..

sudo mkdir $2

cd $2

sudo touch Dockerfile

sudo chmod 777 Dockerfile

cd ..

sudo cat images/$1.txt > $2/Dockerfile

cd $2

sudo docker build -t $2 .