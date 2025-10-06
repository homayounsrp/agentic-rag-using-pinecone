from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os
from Config.llm import llm, embedding_model
import uuid
from Config.pinecone_cfg import get_pinecone
# Pinecone client & index
pc = get_pinecone()
index = pc.Index(host=os.getenv("PINECONE_HOST"))

def process_and_upsert_files(data: str):
    vectors = []

    embedding = embedding_model.embed_query(data)
    print(embedding)
    vectors.append((
        str(uuid.uuid4()), 
        embedding,        
        {"text": data}  
    ))

    # Upsert all vectors for this file into Pinecone
    index.upsert(vectors)
   
    return f"✅ Inserted {len(vectors)} chunks from {data}"
