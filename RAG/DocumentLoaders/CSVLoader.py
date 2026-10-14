from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='D:\dowl\projects\langchain\RAG\DocumentLoaders\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])