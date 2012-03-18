import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2

# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d

def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)

def triangle_sum_gen():
    i = 1
    sum = 0
    while True:
        sum += i
        yield sum
        i += 1

for triangle_sum in triangle_sum_gen():
    num_divisors = NumberOfDivisors(triangle_sum)
    if num_divisors > 500:
        print triangle_sum, "has", num_divisors, "divisors"
        break
