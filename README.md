# SberCyberHack

# Multi-Agent Threat Detection System

## Overview

This system uses 3 agents and a coordinator agent to analyze a Linux VM for network threats using LangChain and OpenAI.

### Agents

- **Port Scan Analyzer**: Checks for suspicious open ports.
- **Log File Monitor**: Looks for suspicious activity in logs.
- **Process & Malware Analyzer**: Detects malicious processes.

The **Coordinator Agent** uses OpenAI to summarize the results and determine the severity of threats.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the main script:

```bash
python main.py
```

Make sure you are running this on a Linux environment.

## How to copy on linux machine in docker and run


