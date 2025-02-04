
# cache 

cache the vectors as key to improve inference 

# build the redis container
docker build -t monkeypatched/redis-vss-image:latest . --no-cache

# run the redis container
docker run --network host -d -p 6379:6379 monkeypatched/redis-vss-image:latest

