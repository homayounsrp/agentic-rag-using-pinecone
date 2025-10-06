from langgraph.graph import StateGraph, START, END
from Agents.Researcher.agent import research_agent
from Agents.Memory.agent import memory_agent
from Agents.Supervisor.agent import supervisor_agent
from langgraph.checkpoint.memory import InMemorySaver
from Agents.state import State




graph_builder = StateGraph(State)
graph_builder.add_node("researcher_agent", research_agent)
graph_builder.add_node("memory_agent", memory_agent)
graph_builder.add_node("supervisor_agent", supervisor_agent)
graph_builder.add_edge(START, "supervisor_agent")

checkpointer = InMemorySaver()
graph = graph_builder.compile(checkpointer=checkpointer)