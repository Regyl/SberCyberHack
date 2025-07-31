import logging
from typing import Final

from langchain.schema import SystemMessage, HumanMessage

from src.commons import utils

log = logging.getLogger(__name__)
SYSTEM_PROMPT: Final = "You are a cybersecurity expert, developed to analyse authorization logs. If answer will be displeased by our coworkers, we will be fired."

class LogAnalyzerAgent:
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
            log.info('Skip processing')
            return None
        else:
            logs = utils.run_command("cat /var/log/auth.log | tail -n 100")
            messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=f"Analyze these Linux auth logs and report any security threats:\n{logs}")
            ]
            result = self.llm.invoke(messages)
            return result.content