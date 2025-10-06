from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.store.memory import InMemoryStore
load_dotenv()
from Ingest.pinecone_ingest import process_and_upsert_files
from Retrieve.pinecone_retrieve import search_and_fetch


@tool
def add_memory(query: str):
    """to Save information to Database use this tool"""
    try:
        process_and_upsert_files(query)
        return "Memory Saved succufully"
    except:
        return "There was an issue in saving the memory"
 
@tool
def search_memory(query: str):
    """Retrieve memory."""
    results = search_and_fetch(query_text=query)
    return results
 
