import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(name="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=1536
)