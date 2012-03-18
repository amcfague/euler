from itertools import product

NUM_SIDES = 6
NUM_DIE = 5
NUM_HIGH_NUMBERS = 3

all_sums = [sum(sorted(i)[-NUM_HIGH_NUMBERS:])
            for i in product(*[range(1, NUM_SIDES + 1)] * NUM_DIE)]
print all_sums.count(15)
