
# Planning LLM 
llm used to plan and execute the workflow

# build  deepseek using ollama
sudo docker build -t monkeypatched/deepseek-llm:latest . --no-cache

# run deepseek llm using ollama
sudo docker run  --network host -d -p 11434:11434 monkeypatched/deepseek-llm:latest

# tag container
sudo docker tag  monkeypatched/deepseek-llm:latest monkeypatched.azurecr.io/llm/deepseek-r1:latest

# push contaner
sudo docker push monkeypatched.azurecr.io/llm/deepseek-r1:latest



sudo az login
sudo az acr login --name monkeypatched