
# cache 

cache the vectors as key to improve inference 

# build the redis container
docker build -t redis-vss-image .

# run the redis container
docker run -d --name redis-vss-container -p 6379:6379 redis-vss-image

