# using list slices
list1 = [0, 1, 2, 4, 8, 16, 32, 64]

# 'from' is included, 'to' is excluded
print(list1[0:2])
print(list1[2:4])
print(list1[4:7])

# omit 'from' or 'to'
print(list1[:4])
print(list1[4:])

# stepping when slicing
print(list1[:7:2])

# stepping when slicing - backward
print(list1[::-2])
print(list1[::-1])  # revert list

# if negative index - get value from the end
print(list1[2:-2])

# list comprehensions
list2 = [i ** 2 for i in range(11)]
print(list2)

list3 = [i ** 2 for i in range(11) if i ** 2 % 2 == 0]
print(list3)
