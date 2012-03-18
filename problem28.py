#!/usr/bin/env python
dimension = 1001

def seq1(n):
    return 4 * (n ** 2) - 4 * n + 1
def seq2(n):
    return 4 * (n ** 2) - 10 * n + 7
def seq3(n):
    return 4 * (n ** 2) - 8 * n + 5
def seq4(n):
    return 4 * (n ** 2) - 6 * n + 3

def sum_(seq_func):
    return sum([seq_func(i) for i in range(2, dimension / 2 + 2)])

# Always include the center
sum = 1 + sum_(seq1) + sum_(seq2) + sum_(seq3) + sum_(seq4)
print sum
