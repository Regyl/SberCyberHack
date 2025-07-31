# Multi-Agent Threat Detection System
## Overview
This system uses 3 agents and a coordinator agent to analyze Windows/Linux VM for network threats using LangChain and OpenAI.
Agents:
- **Port Scan Analyzer**: Checks for suspicious open ports.
- **Log File Monitor**: Looks for suspicious activity in logs.
- **Process & Malware Analyzer**: Detects malicious processes.

The **Summariser Agent** uses OpenAI to summarize the results and determine the severity of threats.

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the main script:
```bash
python ./src/track3-network-security/main.py
```

## Free LLM
- GigaChat (no)
  - Гигачат поддерживат langchain_openai [лишь частично](https://developers.sber.ru/docs/ru/gigachat/guides/compatible-openai)
- Together.ai https://docs.together.ai/docs/rate-limits
