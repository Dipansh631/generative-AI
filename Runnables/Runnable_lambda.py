from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
)
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.8-flash', temperature=0.2)
parser=StrOutputParser()

def word_counter(text: str) -> int:
    return len(text.split())

runnable_word_counter=RunnableLambda(word_counter)
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic'],
)
jokegenchain=RunnableSequence(prompt1, model, parser)
parallelchain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':runnable_word_counter
})
final_chain=RunnableSequence(jokegenchain, parallelchain)
print(final_chain.invoke({'topic':'chickens'}))