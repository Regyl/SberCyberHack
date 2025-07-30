from utils import run_command
from llm_provider import get_llm
from langchain.schema import HumanMessage


class LogAnalyzerAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self):
        logs = run_command("cat /var/log/auth.log | tail -n 100")[:300]
        messages = [
            HumanMessage(content=f"Analyze these Linux auth logs and report any security threats:\n{logs}")
        ]
        result = self.llm(messages)
        return result.content
