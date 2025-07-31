import logging
from typing import Final

from langchain.schema import SystemMessage, HumanMessage

from src.commons import utils

log = logging.getLogger(__name__)
SYSTEM_PROMPT: Final = "You are a cybersecurity expert, developed to analyse running processes. If answer will be displeased by our coworkers, we will be fired."

class ProcessCheckerAgent:
    def __init__(self):
        self.llm = utils.get_threadsafe_llm()

    @utils.log_execution_time
    def run(self):
        try:
            return self.__private_run()
        except Exception as e:
            log.exception(f"Exception occurred: {e}")
            return None

    async def run_async(self):
        return self.run()

    def __private_run(self):
        os_name = utils.get_os_name()
        if os_name == 'Windows':
            ps_command = [
                "powershell",
                "-Command",
                "Get-Process | Select-Object Name,Id,CPU | Format-Table -HideTableHeaders"
            ]
            processes = utils.run_command(ps_command)
            messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(
                    content=f"Analyze these running processes and report if any look suspicious:\n{processes}")
            ]
            result = self.llm.invoke(messages)
            return result.content
        else:
            processes = utils.run_command("ps aux --sort=-%cpu | head -n 10")
            messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=f"Analyze these running processes and report if any look suspicious:\n{processes}")
            ]
            result = self.llm.invoke(messages)
            return result.content