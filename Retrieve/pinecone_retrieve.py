
from Config.llm import embedding_model
from Config.pinecone_cfg import get_pinecone
import os 
# Pinecone client & index
pc = get_pinecone()
index = pc.Index(host=os.getenv("PINECONE_HOST"))



def search_and_fetch( query_text: str, top_k: int = 3):
    # 1. Create embedding for the query
    query_embedding = embedding_model.embed_query(query_text)

    # 2. Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return results


