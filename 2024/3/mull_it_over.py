#--- Day 3: Mull It Over ---
import operator 
import re

with open('input.txt', 'r') as file:
    memory = file.read()

matches = re.findall("mul\(\d{1,3},\d{1,3}\)", memory)
multipled = [eval(f"operator.{x}") for x in matches]

print(sum(multipled))

# --- Part Two --- 

matches = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", memory)

enabled = 1
filtered_matches = []
for instruction in matches:
    if instruction == "don't()":
        enabled = 0
        continue
    elif instruction == "do()":
        enabled = 1
        continue
    elif enabled: 
        filtered_matches.append(instruction)
multipled = [eval(f"operator.{x}") for x in filtered_matches]
print(sum(multipled))

