def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2
    num_primes = 0

    while True:
        if num_primes == 100000:
            break
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            num_primes += 1
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def is_truncatable(number):
    if number < 10:
        return False

    n = number
    num_nums = 0
    while n > 0:
        if n in primes:
            num_nums += 1
            n /= 10
        else:
            return False

    n = number
    tens = 10 ** num_nums
    while n > 0:
        if n in primes:
            tens /= 10
            n %= tens
        else:
            return False

    return True

# Generate a million primes?
primes = frozenset(gen_primes())

print sum([prime for prime in primes if is_truncatable(prime)])
