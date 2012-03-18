cache = {}

def sum_digits(n):
    sum = 0
    while n > 0:
        if n in cache:
            return sum + cache.get(n)
        sum += n % 10
        n /= 10

    return sum

def check_sum(n):
    sum1 = sum_digits(n)
    sum2 = sum_digits(137 * n)

    return sum1 == sum2


num_props = 0
for n in xrange(10 ** 18):
    if check_sum(n):
        num_props += 1

print num_props
