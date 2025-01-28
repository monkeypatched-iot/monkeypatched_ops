
# Planning LLM 
llm used to plan and execute the workflow

# build  deepseek using ollama
sudo docker build -t deepseek-llm . 

# run deepseek llm using ollama
sudo docker run  --network host -d -p 11434:11434 deepseek-llm
