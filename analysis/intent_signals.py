# intent_signals.py
# Extracts early attacker intent indicators

from collections import Counter

def connection_burst_signal(pid_records, threshold=10):
    """
    Detects sudden burst of network connections
    """
    return len(pid_records) >= threshold

def unique_remote_ips(pid_records, threshold=5):
    """
    Detects scanning / lateral movement behavior
    """
    ips = set()
    for r in pid_records:
        remote = r.get("remote_address")
        if remote:
            ip = remote.split(":")[0]
            ips.add(ip)
    return len(ips) >= threshold

def extract_intent_signals(grouped_records):
    signals = {}

    for pid, records in grouped_records.items():
        signals[pid] = {
            "connection_burst": connection_burst_signal(records),
            "multiple_remote_ips": unique_remote_ips(records)
        }

    return signals
