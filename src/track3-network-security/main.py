import asyncio
import logging

from agent1_port_scan import PortScanAgent
from agent2_log_analyzer import LogAnalyzerAgent
from agent3_process_checker import ProcessCheckerAgent
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
        agents = await asyncio.gather(PortScanAgent().run_async(), LogAnalyzerAgent().run_async(), ProcessCheckerAgent().run_async())
    else:
        agents = [PortScanAgent().run(), LogAnalyzerAgent().run(), ProcessCheckerAgent().run()]

    summariser = Summariser()
    final_report = summariser.run(agents)
    final_report_detailed = summariser.run_detailed(agents)

    utils.write_summary(final_report, 3)
    utils.write_detailed_summery(final_report_detailed, 3)

if __name__ == "__main__":
    asyncio.run(main())
