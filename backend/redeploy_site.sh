#!/bin/bash

echo "fetching most recent repository changes..."
cd /home/opc/newhacks-2022/backend
git pull

echo "Spinning down existing containers to conserve memory..."
sudo docker container stop linkhack 
sudo docker container rm linkhack
sudo docker image build -t linkhack_image .

rm -rf build
cd ../frontend
npm run build
mv build ../backend/build

echo "Re-building and spinning up application..."
sudo docker run --name linkhack -p 5001:5000 -d linkhack_image
sudo docker run -d --name linkhack_frontend -it --rm -v ${PWD}:/app -v /app/node_modules -p 3000:3000 -e CHOKIDAR_USEPOLLING=true linkhack_image_frontend
