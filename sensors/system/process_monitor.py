# process_monitor.py
# Collects basic process behavior

import psutil
import time
import json
from datetime import datetime, timezone


LOG_FILE = "process_behavior.log"

def collect_process_data():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu": proc.info['cpu_percent'],
                "memory": proc.info['memory_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def monitor(interval=5):
    while True:
        data = collect_process_data()
        with open(LOG_FILE, "a") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")
        time.sleep(interval)

if __name__ == "__main__":
    monitor()
