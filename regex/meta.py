import re

# Dot "." meta character means "any symbol"
print("Testing '.' meta character:")
pattern = r"Gr.y"

if re.search(pattern, "Sasha Grey"):
    print("Match 1")

if re.search(pattern, "Sasha Gray"):
    print("Match 2")

if re.search(pattern, "Sasha Gr*y"):
    print("Match 3")

if re.search(pattern, "Sasha Rose"):
    print("Match 4")

# Carrot "^" meta character means "match the start of a string"
print("Testing '^' meta character:")
pattern = r"^Sasha.Gr.y"

if re.search(pattern, "Sasha#Grey"):
    print("Match 1")

if re.search(pattern, "Sasha_Grey"):
    print("Match 2")

if re.search(pattern, "_Sasha!Gr*y"):
    print("Match 3")

if re.search(pattern, "Sasha Rose"):
    print("Match 4")

# Dollar "$" meta character means "match the end of a string"
print("Testing '$' meta character:")
pattern = r"^Sasha....y$"

if re.search(pattern, "Sasha Grey"):
    print("Match 1")

if re.search(pattern, "Sasha Gray"):
    print("Match 2")

if re.search(pattern, "Sasha Grei"):
    print("Match 3")

if re.search(pattern, "Sasha Rosy"):
    print("Match 4")

# "|" meta character means "or"
print("Testing '|' meta character:")
pattern = r"^Sasha.Gr(a|e)y"

if re.search(pattern, "Sasha#Gray"):
    print("Match 1")

if re.search(pattern, "Sasha_Grey"):
    print("Match 2")

if re.search(pattern, "Sasha Gr*y"):
    print("Match 3")

# Asterisk "*" meta character means "zero or more occurrences of previous thing"
print("Testing '*' meta character:")
pattern = r"Cat(meow)*"

if re.search(pattern, "Cat meow!"):
    print("Match 1")

if re.search(pattern, "Cat meow meow!"):
    print("Match 2")

if re.search(pattern, "Cat mmeows!"):
    print("Match 3")

if re.search(pattern, "meow!"):
    print("Match 4")

# Plus "+" meta character means "one or more occurrences of previous thing"
print("Testing '+' meta character:")
pattern = r"Cat (meow)+"

if re.search(pattern, "Cat meow!"):
    print("Match 1")

if re.search(pattern, "Cat meow meow!"):
    print("Match 2")

if re.search(pattern, "Cat mmeows!"):
    print("Match 3")

if re.search(pattern, "Cat!"):
    print("Match 4")

# Question "?" meta character means "zero ore one occurrences of previous thing"
print("Testing '?' meta character:")
pattern = r"Cat (meow)?"

if re.search(pattern, "Cat meow!"):
    print("Match 1")

if re.search(pattern, "Cat meow meow!"):
    print("Match 2")

if re.search(pattern, "Cat mmeows!"):
    print("Match 3")

if re.search(pattern, "Cat!"):
    print("Match 4")

# Curly Braces "{x, y}" meta character means "between x and y repetitions of something"
print("Testing '{x, y}' meta character:")
pattern = r"meow{1,3}$"

if re.search(pattern, "Cat meow"):
    print("Match 1")

if re.search(pattern, "Cat meow meow"):
    print("Match 2")

if re.search(pattern, "Cat meow meow meow"):
    print("Match 3")

if re.search(pattern, "Cat "):
    print("Match 4")

pattern = r"[01]+0$"
if re.search(pattern, "01010"):
    print("Match A")

pattern = r"(4{5,6})\1"
if re.search(pattern, "4444444444"):
    print("Match A1")

if re.search(pattern, "444444444444"):
    print("Match A2")

if re.search(pattern, "444444444"):
    print("Match A3")
