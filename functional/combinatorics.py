import itertools

letters = ("A", "B", "C")
print(letters)

print(list(itertools.product(letters, range(2))))
print(list(itertools.permutations(letters)))
