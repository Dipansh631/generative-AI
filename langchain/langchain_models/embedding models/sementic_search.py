import google.generativeai as genai
import os
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

class SimpleGeminiEmbeddings:
    def __init__(self, model="models/gemini-embedding-001"):
        self.model = model
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    def embed_documents(self, texts):
        res = genai.embed_content(model=self.model, content=texts, task_type="retrieval_document")
        return res['embedding']

    def embed_query(self, text):
        res = genai.embed_content(model=self.model, content=text, task_type="retrieval_query")
        return res['embedding']

embedding = SimpleGeminiEmbeddings(model="models/gemini-embedding-001")
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

import time
doc_embeddings = []
for doc in documents:
    doc_embeddings.append(embedding.embed_query(doc))
    time.sleep(3)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)