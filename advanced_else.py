# Using 'else' in for/while loops
# execute code in else section only if loop finished normally
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

# Using 'else' in try-except blocks
# execute code in else section only if no error occurs in the try statement
try:
    print("Try 1")
except ZeroDivisionError:
    print("Catch 1")
else:
    print("Else 1")

try:
    print("Try 2")
    print(1 / 0)
except ZeroDivisionError:
    print("Catch 2")
else:
    print("Else 2")
