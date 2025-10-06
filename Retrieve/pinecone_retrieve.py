
from Config.llm import embedding_model
from Config.pinecone_cfg import get_pinecone
import os 
# Pinecone client & index
pc = get_pinecone()
index = pc.Index(host=os.getenv("PINECONE_HOST"))



def search_and_fetch( query_text: str, top_k: int = 3):
    """
    Runs a semantic search in Pinecone and fetches related nodes from Neo4j.
    
    Args:
        neo4j_query (str): Cypher query to fetch nodes from Neo4j.
        query_text (str): Natural language query to search embeddings.
        top_k (int): Number of top Pinecone results to return.
    
    Returns:
        list[dict]: A list of search results with Pinecone metadata and Neo4j nodes.
    """
    # 1. Create embedding for the query
    query_embedding = embedding_model.embed_query(query_text)

    # 2. Query Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    return results


