# Use an official Python slim image
FROM python:3.10-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama CLI
RUN curl -fsSL https://ollama.com/install.sh | bash

# Expose the Ollama server's default port
EXPOSE 11434

# Copy the rest of your local code into the container
COPY . /workspace

# Set up working directory
WORKDIR /workspace

# Copy the shell script into the container
COPY run_ollama.sh /workspace/run_ollama.sh

# Make the shell script executable
RUN chmod +x /workspace/run_ollama.sh

# Set up environment variable directly in Dockerfile
ENV OLLAMA_HOST=0.0.0.0:11434

# Default command to execute the shell script
CMD ["/workspace/run_ollama.sh"]
