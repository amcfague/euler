from fractions import Fraction


three_sevenths = Fraction(3, 7)
closest_fraction = Fraction(1, 7)

for i in xrange(1, 1000000):
    for j in xrange(1000000, i, -1):
        frac = Fraction(i, j)
        print i, j, frac
        if frac >= three_sevenths:
            break

        if frac > closest_fraction:
            closest_fraction = frac

print closest_fraction
