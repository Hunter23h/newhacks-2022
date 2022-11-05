#!/bin/bash

echo "fetching most recent repository changes..."
cd /home/opc/newhacks-2022/backend
git pull

echo "Spinning down existing containers to conserve memory..."
sudo docker container stop linkhack 
sudo docker container rm linkhack
sudo docker image build -t linkhack_image .

echo "Re-building and spinning up application..."
sudo docker run --name linkhack -p 5001:5000 -d linkhack_image
