from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

print("Loading dotenv...")
load_dotenv()

print("Initializing embeddings model...")
embed_model=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=6)

documents=["what is the capital of pakistan","what is the currency of pakistan","what is the population of pakistan"]   

print("Generating embeddings...")
vectors=embed_model.embed_documents(documents)

print(f"Vector length: {len(vectors)}")
print(vectors)
print("Done!")