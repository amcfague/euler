def probability(x):
    return [(2 - n) / (10 ** 12 - n) for n in xrange(x)]

print probability(15)
