# network_monitor.py
# Collects basic network behavior

import psutil
import time
import json
from datetime import datetime, timezone

LOG_FILE = "network_behavior.log"

def collect_network_data():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            connections.append({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "pid": conn.pid,
                "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
                "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}",
                "status": conn.status
            })
    return connections

def monitor(interval=5):
    while True:
        data = collect_network_data()
        with open(LOG_FILE, "a") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")
        time.sleep(interval)

if __name__ == "__main__":
    monitor()
