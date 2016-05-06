numbers = [i for i in range(11)]
print(numbers)


def pow_2(x):
    return x ** 2


# map function
print(list(map(pow_2, numbers)))
print(list(map(lambda x: x ** 2, numbers)))


def even(x):
    return x % 2 == 0


# filter function
print(list(filter(even, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))
