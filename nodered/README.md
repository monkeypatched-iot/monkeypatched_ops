sudo docker build -t monkeypatched/node-red:latest . --no-cache

sudo docker run  --network host -d -p 1880:1880 monkeypatched/node-red:latest

sudo docker tag  monkeypatched/node-red:latest monkeypatched.azurecr.io/middleware/node-red:latest

az login

sudo az acr login --name monkeypatched

sudo docker push monkeypatched.azurecr.io/middleware/node-red:latest