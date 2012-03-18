from itertools import product

class memoize(object):
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

@memoize
def A(m, n):
    print m, n
    if m == 0:
        return n + 1
    if m == 1:
        return n + 2
    if m == 2:
        return 2 * n + 3
    if m == 3:
        return 2 ** (n + 3) - 3
    if m > 0 and n == 0:
        return A(m-1, 1)
    if m > 0 and n > 0:
        return A(m-1, A(m, n-1))


vals = product([0,1,2,3,4,5], [0,1,2,3,4,5])
print A(5, 1)
