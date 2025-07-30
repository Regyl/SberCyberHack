from utils import run_command
from llm_provider import get_llm
from langchain.schema import HumanMessage


class ProcessCheckerAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self):
        processes = run_command("ps aux --sort=-%cpu | head -n 10")[:300]
        messages = [
            HumanMessage(content=f"Analyze these top running processes and report if any look suspicious:\n{processes}")
        ]
        result = self.llm(messages)
        return result.content
