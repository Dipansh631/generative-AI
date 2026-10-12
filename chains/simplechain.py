from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  
from langchain_core.output_parsers import StrOutputParser
load_dotenv() 
prompt=PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person',
    input_variables=['place'])
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.2)
parser = StrOutputParser()
chain=prompt| model| parser
result=chain.invoke({'place':'sri lankan'})
print(result)
chain.get_graph().print_ascii()