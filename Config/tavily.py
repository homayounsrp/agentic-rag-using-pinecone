from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
load_dotenv()




api_key = os.getenv("TAVILY_API_KEY")


search_engine = TavilySearch(
    api_key=api_key,
    max_results=10,   # bump to 10 so you see more
    search_depth="advanced",                   
    time_range="year",               # a wider window
    semantic_configuration="default",    # use semantic ranking
    reranker="cross-encoder/ms-marco-MiniLM-L-6-v2",  # stronger reranking
    filters={"language": "en"},          # only English results
)
