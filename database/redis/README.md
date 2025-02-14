
# cache 

cache the vectors as key to improve inference 

# build the redis container
docker build -t monkeypatched/redis-vss-image:latest . --no-cache

# run the redis container
docker run --network host -d -p 6379:6379 monkeypatched/redis-vss-image:latest

# tag container
sudo docker tag  monkeypatched/redis-vss-image:latest monkeypatched.azurecr.io/database/redis-vss-image:latest

# push contaner
sudo docker push  monkeypatched.azurecr.io/database/redis-vss-image:latest


az login
sudo az acr login --name monkeypatched

