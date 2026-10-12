from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()
model1=ChatGoogleGenerativeAI(model='gemini-3.5-flash', temperature=0.2)
parser = StrOutputParser()
parser2 = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give The sentiment of the feedback")
parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback as positive or negative: {feedback}\n{format_instructions}',
                            input_variables=['feedback'],
                            partial_variables={'format_instructions': parser2.get_format_instructions()}
)
classifier_chain = prompt1 | model1 | parser2
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model1 | parser),
    RunnableLambda(lambda _: "could not find sentiment")
)
chain = classifier_chain | branch_chain
print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()