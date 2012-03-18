perfect_squares = [n**2 for n in xrange(1,1000000)]

def check_values(x, y, z):
    nums = [x+y, x-y, x+z, z-x, y+z, y-z]
    for num in nums:
        if num ** 2 not in perfect_squares:
            return False
    return True

for (z_i, z) in enumerate(perfect_squares):
    for (y_i, y) in enumerate(perfect_squares[z_i+1:]):
        for (x_i, x) in enumerate(perfect_squares[y_i+1:]):
            if check_values(x, y, z):
                print "x =", x
                print "y =", y
                print "z =", z
