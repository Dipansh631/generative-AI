from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
llm = OpenAI(model='openai-community/gpt2')
response=llm.invoke("why are you so smart?")
print(response)
