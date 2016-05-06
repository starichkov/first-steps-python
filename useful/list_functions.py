numbers = [i for i in range(-5, 16)]

print(all([i > 0 for i in numbers]))
print(any([i > 0 for i in numbers]))

# iterate through values and indices simultaneously
for e in enumerate(numbers):
    print(e)
