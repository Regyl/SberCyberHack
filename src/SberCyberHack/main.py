from src.SberCyberHack.agent1_port_scan import PortScanAgent
from src.SberCyberHack.agent2_log_analyzer import LogAnalyzerAgent
from src.SberCyberHack.agent3_process_checker import ProcessCheckerAgent
from coordinator import CoordinatorAgent

def main():
    print("Running agents...")
    agent1 = PortScanAgent().run()
    agent2 = LogAnalyzerAgent().run()
    agent3 = ProcessCheckerAgent().run()

    coordinator = CoordinatorAgent()
    final_report = coordinator.run([agent1, agent2, agent3])

    print("\n===== FINAL THREAT REPORT =====")
    print(final_report)

if __name__ == "__main__":
    main()
