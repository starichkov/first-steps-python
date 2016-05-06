# Tuple is an immutable list
words = ("foo", "bar")
print(words)

# read-only, TypeError will be raised
try:
    words[2] = "!"
except TypeError:
    print("Type Error raised")

words1 = "foo", "bar"
print(words1)

empty_words = ()
print(empty_words)

# tuple unpacking
print("Tuple unpacking:")
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

print("Tuple unpacking:")
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
