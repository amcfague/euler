def digital_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

hundred = range(0, 101)
max_sum = 0

for a in hundred:
    for b in hundred:
        sum = digital_sum(a ** b)
        if sum > max_sum:
            max_sum = sum

print max_sum
