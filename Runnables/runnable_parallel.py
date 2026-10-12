from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel,RunnableSequence
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash', temperature=0.2)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='generate a tweet about{topic}',
    input_variables=['topic'],
)
prompt2=PromptTemplate(
    template='generate a post about {topic}',
    input_variables=['topic'],
)

chain=RunnableParallel(
    {'tweet': RunnableSequence(prompt1,model,parser),
     'post': RunnableSequence(prompt2,model,parser)}
)
print(chain.invoke({'topic':'StarLink'}))