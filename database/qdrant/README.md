# Neo4j database
vector database for similarity search

# docker build 
docker pull qdrant/qdrant

# docker run
docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant

sudo docker tag qdrant/qdrant:latest monkeypatched.azurecr.io/qdrant:latest
sudo docker push monkeypatched.azurecr.io/qdrant:latest

http://20.121.103.150:6333/dashboard