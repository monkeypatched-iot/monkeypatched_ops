docker pull nats

sudo docker run --name nats --network host --rm -p 4222:4222 -p 8222:8222 nats --http_port 8222 

sudo docker tag  nats monkeypatched.azurecr.io/middleware/nats:latest

az login

sudo az acr login --name monkeypatched

sudo docker push monkeypatched.azurecr.io/middleware/nats:latest