# static_defense.py
# Non-evolving baseline defense

from evolution_engine.genome import DefenseGenome


def create_static_defense():
    """
    Create a fixed defense genome with no mutation or evolution
    """
    conditions = [
        {"metric": "connection_rate", "threshold": 10},
        {"metric": "privilege_change", "threshold": 2}
    ]

    actions = [
        {"type": "block_ip", "severity": "medium"}
    ]

    return DefenseGenome(conditions, actions)


def run_static_defense(intent_signals):
    """
    Simulate static defense response
    """
    genome = create_static_defense()

    responses = []
    for pid, intent in intent_signals.items():
        if intent.get("connection_burst") or intent.get("multiple_remote_ips"):
            responses.append(genome)

    return responses
