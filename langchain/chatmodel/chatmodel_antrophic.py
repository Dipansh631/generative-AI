from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
llm = ChatAnthropic(model='claude-sonnet-4-5',temperature = 0.2)
response=llm.invoke("why are you so smart?")
print(response)
