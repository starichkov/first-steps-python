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
