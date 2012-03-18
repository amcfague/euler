zeroed_list = [0] * 10

def count_numbers(n):
    number_list = list(zeroed_list)
    while n > 0:
        number_list[n % 10] += 1
        n /= 10
    return number_list

for n in xrange(1, 10 ** 10):
    orig_count = count_numbers(n)
    for i in range(2, 7):
        if orig_count != count_numbers(n * i):
            break
    else:
        print "SUCCESS:", n
        break
