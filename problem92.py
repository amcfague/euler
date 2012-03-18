seen_numbers_1 = set()
seen_numbers_89 = set()

def get_square_of_digits(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n /= 10
    return s

def number_chain(n):
    numbers = []
    while n not in [1, 89]:
        if n in seen_numbers_1:
            return False
        if n in seen_numbers_89:
            return True

        numbers.append(n)
        n = get_square_of_digits(n)

    if n == 1:
        seen_numbers_1.update(numbers)
    else:
        seen_numbers_89.update(numbers)

    return n == 89

s = 0
for x in xrange(1, 10000001):
    if number_chain(x):
        s += 1

print s
