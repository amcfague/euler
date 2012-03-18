from math import factorial

GRID_SIZE = 20

def binomial_distribution(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print binomial_distribution(2 * GRID_SIZE, GRID_SIZE)
