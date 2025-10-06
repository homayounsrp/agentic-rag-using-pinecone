# supervisor.py

from langgraph_supervisor import create_supervisor
from Config.llm import llm
from Agents.Supervisor.prompt import supervisor_agent_prompt

from Agents.Memory.agent import memory_agent
from Agents.Researcher.agent import research_agent

supervisor = create_supervisor(
        agents=[research_agent, memory_agent],
        model=llm,
        prompt=supervisor_agent_prompt,
        output_mode="full_history",
    )

supervisor_agent = supervisor.compile()
