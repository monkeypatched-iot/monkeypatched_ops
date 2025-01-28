# Neo4j database
graph database for knowledge base

# docker build 
sudo docker build -t neo4j-db .

# docker run
docker stop <container_id>
docker rm <container_id>
docker run -p 7474:7474 -p 7687:7687  --network host  -e NEO4J_AUTH=neo4j/neo4j neo4j-db






