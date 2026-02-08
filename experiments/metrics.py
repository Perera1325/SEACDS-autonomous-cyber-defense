# metrics.py
# Defines evaluation metrics for autonomous cyber defense

def defense_effectiveness(genomes):
    """
    Average fitness of the population
    """
    if not genomes:
        return 0.0
    return sum(g.fitness for g in genomes) / len(genomes)


def defense_diversity(genomes):
    """
    Measures diversity based on action types
    """
    action_sets = set()
    for g in genomes:
        actions = tuple(a["type"] for a in g.actions)
        action_sets.add(actions)
    return len(action_sets)


def max_fitness(genomes):
    """
    Best defense in the population
    """
    if not genomes:
        return 0.0
    return max(g.fitness for g in genomes)
