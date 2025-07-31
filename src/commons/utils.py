import functools
import logging
import os
import platform
import subprocess
import time
from typing import Final

import yaml
from langchain_openai import ChatOpenAI

log = logging.getLogger(__name__)
MAX_LENGTH = config = yaml.safe_load(open("../resources/config.yaml"))["llm"]["input"]["limit"]
NO_HISTORY_CHAT: Final = ChatOpenAI(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    openai_api_key=os.getenv("GIGACHAT_TOKEN"),
    openai_api_base="https://api.together.xyz/v1",
    max_retries=3,
    timeout=90
)

def get_os_name():
    return platform.system()

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Execution error: {result.stderr}")

    return result.stdout.strip()[:MAX_LENGTH]

def get_threadsafe_llm():
    if os.getenv("GIGACHAT_TOKEN") is not None:
        return NO_HISTORY_CHAT
    else:
        return ChatOpenAI(
            base_url="http://localhost:1235/v1",  # LM Studio OpenAI API endpoint
            api_key="lm-studio",  # Dummy key - LM Studio ignores this field, but langchain requires it
            model_name="deepseek-r1"  # Matches the name of the loaded model in LM Studio
        )

def write_summary(report, track_num):
    with open(f"../resources/results/track{track_num}/final_report.md", "w",
              encoding="UTF-8") as f:  # w means override entire file data
        f.write(report)

def write_detailed_summery(report, track_num):
    with open(f"../resources/results/track{track_num}/final_report_detailed.md", "w",
              encoding="UTF-8") as f:
        f.write(report)

def is_async_enabled():
    with open("../resources/config.yaml") as config_file:
        config = yaml.safe_load(config_file)
        return config["async"]["enabled"]

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        func_name = getattr(func, "__qualname__", getattr(func, "__name__", str(func)))
        log.info(f"Execution time {func_name}: {elapsed_time:.4f} seconds")
        return result
    return wrapper