from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnableSequence,
    RunnablePassthrough,
    RunnableBranch
)
load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-3.8-flash', temperature=0.2)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic'],
)
prompt2=PromptTemplate(
    template='summarize the following report in bullet points: {text}',
    input_variables=['text'],
)
report_gen_chain=RunnableSequence(prompt1, model, parser)
summarize_chain=RunnableSequence(
    RunnableParallel({'text': RunnablePassthrough()}),
    prompt2,
    model,
    parser,
)
branch=RunnableBranch(
    (lambda x: len(x.split()) > 500, summarize_chain),
    RunnablePassthrough()
    )

final_chain=RunnableSequence(report_gen_chain, branch)
print(final_chain.invoke({'topic':'the impact of climate change on global agriculture'}))