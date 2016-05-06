import re

pattern = r"meow"
string = "Cat say meow meow!"

# search for occurrences at the beginning of the string
print("Match") if re.match(pattern, string) else print("No match")

# search for occurrences through whole string
print("Match") if re.search(pattern, string) else print("No match")

# find all occurrences of pattern
print(re.findall(pattern, string))

match = re.search(pattern, string)
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.groups())

# Search & Replace

# replace all occurrences if [max] = 0
new_string = re.sub(pattern, "woof", string)
print(new_string)

# replace [max] occurrences
new_string = re.sub(pattern, "woof", string, 1)
print(new_string)
