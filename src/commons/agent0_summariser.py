import logging
from typing import Final

from langchain.schema import SystemMessage, HumanMessage

from src.commons import utils

log = logging.getLogger(__name__)
SYSTEM_PROMPT: Final = "You are a cybersecurity expert, developed to summarise answers of other AI-agents. If answer will be displeased by our coworkers, we will be fired. Return response in markdown format."

class Summariser:
    def __init__(self):
        self.llm = utils.get_threadsafe_llm()

    @utils.log_execution_time
    def run(self, agent_outputs):
        try:
            return self.__private_run(agent_outputs)
        except Exception as e:
            log.exception(f"Exception occurred: {e}")
            return None

    def __private_run(self, agent_outputs):
        prompt = "Summarize the findings from the following 3 agents and assess the threat level (low, medium, high):\n\n"
        for i, out in enumerate(agent_outputs, 1):
            prompt += f"Agent {i} Report:\n{out}\n\n"

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]
        result = self.llm.invoke(messages)
        return result.content

    def run_detailed(self, agent_outputs):
        prompt = "Group the findings from the following 3 agents and assess the threat level (low, medium, high):\n\n"
        for i, out in enumerate(agent_outputs, 1):
            prompt += f"Agent {i} Report:\n{out}\n\n"

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]
        result = self.llm.invoke(messages)
        return result.content
