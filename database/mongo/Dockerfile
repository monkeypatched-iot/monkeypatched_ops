# Use the official MongoDB image as a base
FROM mongo:latest

# Set up environment variables
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=admin123

# Expose the default MongoDB port
EXPOSE 27017

# Copy initialization scripts if needed
# ADD ./init-scripts /docker-entrypoint-initdb.d/

# Command to run MongoDB
CMD ["mongod"]
