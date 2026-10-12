from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    timeout=60,
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)
template1 = PromptTemplate(
    template="Write a detailed report about {topic}.",
    input_variables=["topic"],
)
template2 = PromptTemplate(
    template="Write a five-line summary of the following text:\n{text}",
    input_variables=["text"],
)

parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser

print("Generating report and summary...", flush=True)
result = chain.invoke(
    {"topic": "The impact of climate change on global agriculture."}
)
print(result, flush=True)