import asyncio
import logging

from agent1 import Agent
from src.commons import utils
from src.commons.agent0_summariser import Summariser

log = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.INFO)
    asyncEnabled = utils.is_async_enabled()
    os_name = utils.get_os_name()
    log.info(f"asyncEnabled: {asyncEnabled}, os_name: {os_name}")
    log.info('Running agents...')

    if asyncEnabled:
        agents = await asyncio.gather(Agent().run_async())
    else:
        agents = [Agent().run()]

    summariser = Summariser()
    final_report = summariser.run(agents)
    final_report_detailed = summariser.run_detailed(agents)

    utils.write_summary(final_report, 1)
    utils.write_detailed_summery(final_report_detailed, 1)

if __name__ == "__main__":
    asyncio.run(main())
