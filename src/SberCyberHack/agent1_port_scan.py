from llm_provider import get_llm
from utils import run_command
from langchain.schema import HumanMessage


class PortScanAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self):
        ports = run_command("netstat -tuln")[:300]
        messages = [
            HumanMessage(content=f"Analyze this port scan output and detect threats:\n{ports}")
        ]
        result = self.llm(messages)
        return result.content
