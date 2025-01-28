
# Planning LLM 
llm used to plan and execute the workflow

# build mistral 7B using ollama
sudo docker build -t mistral-llm . 

# run mistral llm using ollama
sudo docker run  --network host -d -p 11434:11434 mistral-llm