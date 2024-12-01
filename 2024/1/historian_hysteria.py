#--- Day 1: Historian Hysteria ---
import pandas as pd

df = pd.read_csv('input.txt', sep='   ', header=None)

left = df[0].tolist()
left.sort()
right = df[1].tolist()
right.sort()

diff = [abs(x - y) for x, y in zip(left, right)]
print(sum(diff))

# --- Part Two --- 

sim = [x * right.count(x) for x, y in zip(left, right) if x in right]
print(sum(sim))

