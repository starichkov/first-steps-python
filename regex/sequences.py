import re

pattern = r"(bla)\1"

if re.match(pattern, "bla"):
    print("Match 1")

if re.match(pattern, "blabla"):
    print("Match 2")

if re.match(pattern, "blablabla"):
    print("Match 3")

if re.match(pattern, "blablablabla"):
    print("Match 4")

# \d, \s, and \w
# \D, \S, and \W
