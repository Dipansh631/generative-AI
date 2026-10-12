from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
)
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.5-flash', temperature=0.2)
parser=StrOutputParser()
passthrough=RunnablePassthrough()
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic'],
)
prompt2=PromptTemplate(
    template='explain the following joke in detail: {text}',
    input_variables=['text']
)
jokegenchain=RunnableSequence([prompt1,model,parser])
parallelchain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence([
        RunnableParallel({'text':RunnablePassthrough()}),
        prompt2,
        model,
        parser,
    ])
})
final_chain=RunnableSequence([jokegenchain, parallelchain])
print(final_chain.invoke({'topic':'chickens'}))