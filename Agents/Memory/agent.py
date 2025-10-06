from Config.llm import llm
from Agents.Memory.tools import search_memory, add_memory
from langgraph.prebuilt.chat_agent_executor import create_react_agent
from Agents.Memory.prompt import retriever_agent_prompt
from langgraph.prebuilt import ToolNode
tools_list = [add_memory, search_memory]

memory_agent = create_react_agent(
    model=llm,
    tools=ToolNode(tools_list),
    name="Memory_Agent",
    prompt= retriever_agent_prompt 
)