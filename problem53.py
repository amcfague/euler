import gmpy

counter = 0

for n in xrange(1, 101):
    for r in range(1, n + 1):
        c = gmpy.comb(n, r)
        if c > 1000000:
            counter += 1

print counter
