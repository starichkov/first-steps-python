import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

pattern = r"[ab][bf]"

if re.search(pattern, "abba"):
    print("Match 1")

if re.search(pattern, "afka"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")

# using ranges
pattern = r"[a-eA-E][0-9]"
if re.search(pattern, "E0"):
    print("Match 1")

if re.search(pattern, "F1"):
    print("Match 2")

# using ^ to invert condition
pattern = r"[^a-eA-E][0-9]"
if re.search(pattern, "E0"):
    print("Match 1")

if re.search(pattern, "F1"):
    print("Match 2")
