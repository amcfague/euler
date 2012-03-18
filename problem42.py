def value_of(word):
    return sum((
        alphabet[char]
        for char in word))
        


def t(n):
    return .5 * n * (n + 1)

alphabet = dict([(v, k + 1) for (k, v) in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")])
words = [word.strip("\"") for word in open("words.txt", "r").read().split(',')]
triangle_numbers = [t(n+1) for n in range(10000)]

triangle_words = [word for word in words if value_of(word) in triangle_numbers]
print len(triangle_words)
