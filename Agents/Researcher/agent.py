from Config.llm import llm
from Agents.Researcher.tools import SearchEngine
from langgraph.prebuilt.chat_agent_executor import create_react_agent
from Agents.Researcher.prompt import search_agent_prompt

tools_list = [SearchEngine]

research_agent = create_react_agent(
    model=llm,
    tools=tools_list,
    name="research_agent",
    prompt=search_agent_prompt
)