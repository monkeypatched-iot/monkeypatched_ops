# Use the official Neo4j image as a base
FROM neo4j:latest

# Set up environment variables
ENV NEO4J_AUTH=neo4j/admin123
ENV NEO4J_ACCEPT_LICENSE_AGREEMENT=yes

# Expose the default Neo4j ports
EXPOSE 7474 7687

# Copy initialization scripts if needed
# ADD ./init-scripts /var/lib/neo4j/import/

# Command to run Neo4j
CMD ["neo4j"]
