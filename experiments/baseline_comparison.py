# baseline_comparison.py
# Compares static defense vs evolving defense

from analysis.log_parser import parse_log, group_by_pid
from analysis.intent_signals import extract_intent_signals

from baseline.static_defense import run_static_defense
from evolution_engine.population import DefensePopulation
from feedback_engine.fitness_evaluator import evaluate_defense


def compare_defenses(log_file):
    records = parse_log(log_file)
    grouped = group_by_pid(records)
    intents = extract_intent_signals(grouped)

    # ---- Static Defense ----
    static_responses = run_static_defense(intents)
    static_score = len(static_responses)

    # ---- Evolving Defense ----
    population = DefensePopulation(size=5)
    population.initialize()

    evolving_score = 0
    for pid, intent in intents.items():
        genome = population.get_population()[0]
        feedback = evaluate_defense(intent, genome.actions)
        genome.evaluate_fitness(
            feedback["threat_blocked"],
            feedback["false_positive"]
        )
        evolving_score += genome.fitness

    return static_score, evolving_score


if __name__ == "__main__":
    s, e = compare_defenses("sensors/network/network_behavior.log")

    print("=== BASELINE COMPARISON ===")
    print(f"Static Defense Score:   {s}")
    print(f"Evolving Defense Score: {e:.2f}")
