from langchain_core.tools import tool
from Config.tavily import search_engine
@tool
def SearchEngine(query: str, max_results: int = 10) -> str:
    """
    Fetches top search results via Tavily’s Search API.
    """
   

    if max_results is not None:
        search_engine.max_results = max_results

    # either of the following two will work:
    return search_engine.run(query)   