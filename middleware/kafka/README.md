# first deploy the zookeeper container

sudo docker pull confluentinc/cp-zookeeper:latest

sudo docker tag  confluentinc/cp-zookeeper:latest monkeypatched.azurecr.io/middleware/cp-zookeeper:latest

az login

sudo az acr login --name monkeypatched

sudo docker push monkeypatched.azurecr.io/middleware/cp-zookeeper:latest

# then deploy the kafka container


sudo docker pull confluentinc/cp-kafka:latest

sudo docker tag  confluentinc/cp-kafka:latest monkeypatched.azurecr.io/middleware/cp-kafka:latest

az login

sudo az acr login --name monkeypatched

sudo docker push monkeypatched.azurecr.io/middleware/cp-kafka:latest