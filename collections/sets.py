# cannot contain duplicates
numbers = {7, 6, 5, 1, 2, 3, 4, 8, 9, 1}
print(numbers)

# using set.add instead of list.append
numbers.add(6)
print(numbers)

# set.remove method removes specific element
numbers.remove(6)
print(numbers)

# set.pop method removes arbitrary element
numbers.pop()
print(numbers)

print("Operations:")
numbers1 = {1, 2, 3, 4, 5, 6}
numbers2 = {4, 5, 6, 7, 8, 9}
print(numbers1)
print(numbers2)

# union - get items from both sets
print("'|' (union): " + str(numbers1 | numbers2))

# intersection - get items both sets have
print("'&' (intersection): " + str(numbers1 & numbers2))

# difference - get new set that contains unique items for the first set
print("'-' (difference): " + str(numbers1 - numbers2))
print("'-' (difference): " + str(numbers2 - numbers1))

# symmetric difference - get new set that contains unique items for each set
print("'^' (symmetric difference): " + str(numbers1 ^ numbers2))
