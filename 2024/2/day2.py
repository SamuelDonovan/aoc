#--- Day 2: Red-Nosed Reports ---

total = 0
with open('input.txt', 'r') as file:
    for reports in file:
        levels_string = reports.split()
        levels = []
        for s in levels_string:
            levels.append(int(s))
        if len(levels) != len(list(set(levels))):
            continue
        ascending_levels = sorted(levels)
        descending_levels = list(reversed(ascending_levels))
        if levels != ascending_levels and levels != descending_levels:
            continue
        to_add = 1
        for idx in range(len(levels) - 1):
            diff = abs(int(ascending_levels[idx + 1]) - int(ascending_levels[idx]))
            if diff > 3:
                to_add = 0
        total = total + to_add
print(total)
