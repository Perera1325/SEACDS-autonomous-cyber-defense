# response_loop.py
# Observe → Infer → Respond → Evaluate loop

from analysis.log_parser import parse_log, group_by_pid
from analysis.intent_signals import extract_intent_signals
from evolution_engine.population import DefensePopulation
from response_engine.defense_trigger import should_trigger_defense
from response_engine.defense_executor import execute_defense
from feedback_engine.fitness_evaluator import evaluate_defense


def run_response_cycle(log_file):
    records = parse_log(log_file)
    grouped = group_by_pid(records)
    intent_map = extract_intent_signals(grouped)

    population = DefensePopulation(size=5)
    population.initialize()

    for pid, intent in intent_map.items():
        if should_trigger_defense(intent):
            genome = population.get_population()[0]

            actions = execute_defense(genome, pid)
            feedback = evaluate_defense(intent, actions)

            genome.evaluate_fitness(
                feedback["threat_blocked"],
                feedback["false_positive"]
            )

            print(
                f"[DEFENSE] PID {pid} → {actions} | fitness={genome.fitness:.2f}"
            )


if __name__ == "__main__":
    run_response_cycle("sensors/network/network_behavior.log")
