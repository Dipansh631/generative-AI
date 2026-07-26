from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

print("Loading dotenv...")
load_dotenv()

print("Initializing embeddings model...")
embed_model=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",dimensions=6)

print("Generating embeddings...")
vector=embed_model.embed_query("who is the best player in the world")

print(f"Vector length: {len(vector)}")
print(vector)
print("Done!")