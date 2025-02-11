#!/bin/bash

# Start the Ollama server
echo "Starting Ollama server..."
ollama serve &

# Get the process ID of the Ollama server
OLLAMA_PID=$!

# Wait for the server to initialize properly
echo "Waiting for Ollama server to initialize..."
for i in {1..30}; do  # Retry for up to 30 seconds
  if curl -f http://localhost:11434 >/dev/null 2>&1; then
    echo "Ollama server is running successfully. Ready for requests!"
    break
  fi
  echo "Waiting for Ollama server..."
  sleep 1
done

# If the server isn't responding after 30 seconds, exit with error
if ! curl -f http://localhost:11434 >/dev/null 2>&1; then
  echo "Failed to connect to Ollama server after multiple attempts."
  exit 1
fi

# Ensure the Deepseek model is pulled
echo "Pulling Deepseek model..."
ollama pull deepseek-r1:8b

# Run the Deepseek model
echo "Running Deepseek model..."
ollama run deepseek-r1:8b

# Keep the container alive and wait for the Ollama server process
wait $OLLAMA_PID
