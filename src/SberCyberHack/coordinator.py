from src.SberCyberHack.llm_provider import get_llm
from langchain.schema import SystemMessage, HumanMessage


class CoordinatorAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, agent_outputs):
        prompt = "You are a cybersecurity expert. Summarize the findings from the following 3 agents and assess the threat level (low, medium, high):\n\n"
        for i, out in enumerate(agent_outputs, 1):
            prompt += f"Agent {i} Report:\n{out}\n\n"

        messages = [
            SystemMessage(content="You summarize security reports from agents."),
            HumanMessage(content=prompt)
        ]
        response = self.llm(messages)
        return response.content
