from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    timeout=60,
    max_new_tokens=256,
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template=(
        "Give 3 facts about {topic}. Return exactly this JSON shape with no "
        "markdown:\n"
        '{{"fact_1": "first fact", "fact_2": "second fact", '
        '"fact_3": "third fact"}}\n'
        "{format_instruction}"
    ),
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result, flush=True)