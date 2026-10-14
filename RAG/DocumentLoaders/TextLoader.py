from pathlib import Path

from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.2)
prompt = PromptTemplate(
    template="write a summary of the following text:\n{text}\n\n",
    input_variables=["text"],
)
parser = StrOutputParser()
text_path = Path(__file__).with_name("cricket.txt")
docs = [
    Document(
        page_content=text_path.read_text(encoding="utf-8"),
        metadata={"source": str(text_path)},
    )
]
chain = prompt | model | parser
result = chain.invoke(docs[0].page_content)
print(result)
