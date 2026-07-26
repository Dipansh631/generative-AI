from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
hf_repo_id = "Qwen/Qwen2.5-7B-Instruct"
hf=HuggingFaceEndpoint(repo_id=hf_repo_id,task="text-generation",temperature=0.8)
llm=ChatHuggingFace(llm=hf)
response=llm.invoke("why are some of people's dicks are very small?")
print(response.content)


