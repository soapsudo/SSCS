#!/bin/bash
sudo docker build -t apache_image:1.0 .

cd /webserver/

sudo docker build -t nginx_image:1.0 .

cd ..
