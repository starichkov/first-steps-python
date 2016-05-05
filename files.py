# Module for working with files

file_name = "meow.txt"
string = "Meow meow meow!\n"

# 1. Open file to append
try:
    f = open(file_name, "a")  # also 'w', 'a' and 'b' modes available
    size = f.write(string)
    assert size == len(string)
finally:
    f.close()
    print("Bytes written: " + str(size))

# 2. Open file in read mode

# this is the same as 'try-with-resources' in Java 7
with open(file_name, "r") as f:
    text = f.read()
    print(text)
