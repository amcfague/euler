from decimal import *

def digital_total(d_str):
    (num1, _, num2) = d_str.rpartition('.')
    num = num1 + num2
    num = num[:100]
    print len(num)
    return sum([int(n) for n in num])

getcontext().prec = 102

total = 0
for i in range(1, 101):
    d = Decimal(i).sqrt()
    d_str = d.to_eng_string()
    if "." in d_str:
        dtotal = digital_total(d_str)
        total += dtotal

print total
