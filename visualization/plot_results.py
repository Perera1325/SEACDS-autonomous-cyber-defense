# plot_results.py
# Generates paper-ready plots from experiment results

import csv
import matplotlib.pyplot as plt


def load_results(path="experiments/results.csv"):
    generations = []
    avg_fitness = []
    best_fitness = []
    diversity = []

    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            generations.append(int(row["generation"]))
            avg_fitness.append(float(row["avg_fitness"]))
            best_fitness.append(float(row["best_fitness"]))
            diversity.append(int(row["diversity"]))

    return generations, avg_fitness, best_fitness, diversity


def plot_fitness(gens, avg_fit, best_fit):
    plt.figure()
    plt.plot(gens, avg_fit, label="Average Fitness")
    plt.plot(gens, best_fit, label="Best Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Defense Fitness Evolution Over Generations")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_diversity(gens, diversity):
    plt.figure()
    plt.plot(gens, diversity, label="Defense Diversity")
    plt.xlabel("Generation")
    plt.ylabel("Diversity")
    plt.title("Defense Diversity Over Generations")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    g, avg_f, best_f, div = load_results()
    plot_fitness(g, avg_f, best_f)
    plot_diversity(g, div)
