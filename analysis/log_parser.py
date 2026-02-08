# log_parser.py
# Parses raw behavior logs into structured data

import json
from collections import defaultdict

def parse_log(file_path):
    records = []
    with open(file_path, "r") as f:
        for line in f:
            try:
                records.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
    return records

def group_by_pid(records):
    grouped = defaultdict(list)
    for r in records:
        pid = r.get("pid")
        if pid is not None:
            grouped[pid].append(r)
    return grouped
