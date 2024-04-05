import os
from openai import AzureOpenAI

client = AzureOpenAI(

  azure_endpoint = "https://d-analytics-eus-oai-chatbots.openai.azure.com/", 

  api_key=os.getenv("INPUT_OPENAI_API_KEY"),  

  api_version="2024-02-15-preview"

)

# Read env variable
env_var = os.environ.get('INPUT_WHO-TO-GREET')
print('Hello ' + env_var)

message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."}]


completion = client.chat.completions.create(

  model="chatbot-innovation-india", # model = "deployment_name"

  messages = message_text,

  temperature=0.7,

  max_tokens=800,

  top_p=0.95,

  frequency_penalty=0,

  presence_penalty=0,

  stop=None

)