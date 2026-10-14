from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("D:\dowl\projects\langchain\RAG\DocumentLoaders\dl-curriculum.pdf")
docs=loader.load()
print(docs[0].page_content)
print(docs[1].metadata)
