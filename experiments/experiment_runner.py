# experiment_runner.py
# Runs controlled evolution experiments

from persistence_engine.genome_store import load_population, save_population
from evolution_engine.population import DefensePopulation
from experiments.metrics import (
    defense_effectiveness,
    defense_diversity,
    max_fitness
)

import csv


def run_experiment(generations=10):
    results = []

    population = DefensePopulation(size=5, genomes=load_population())
    population.initialize()

    for gen in range(generations):
        survivors = population.select_top()
        population.reproduce(survivors)

        avg_fit = defense_effectiveness(population.get_population())
        best_fit = max_fitness(population.get_population())
        diversity = defense_diversity(population.get_population())

        results.append({
            "generation": gen,
            "avg_fitness": avg_fit,
            "best_fitness": best_fit,
            "diversity": diversity
        })

        print(
            f"Gen {gen}: avg={avg_fit:.2f}, best={best_fit:.2f}, diversity={diversity}"
        )

    save_population(population.get_population())
    return results


def save_results(results, path="experiments/results.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["generation", "avg_fitness", "best_fitness", "diversity"]
        )
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    res = run_experiment(generations=15)
    save_results(res)
