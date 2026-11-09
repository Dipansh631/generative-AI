from pathlib import Path

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).with_name("dl-curriculum (1).pdf")
loader = PyPDFLoader(str(pdf_path))
docs=loader.load()
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)
result = splitter.split_documents(docs)
print(result)