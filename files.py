# Module for working with files

# 1. Open file
file_name = "log.txt"
try:
    text_file = open(file_name)
    text_file.close()
except FileNotFoundError:
    print("File Not Found Error: " + file_name)

# 2. Open file in write mode
text_file = open(file_name, "w")  # also 'r', 'a' and 'b' modes available
text_file.close()
