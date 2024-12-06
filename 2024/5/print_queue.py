#--- Day 5: Print Queue ---

section = 1
rules = {}
to_check = []
with open('input.txt', 'r') as file:
    for line in file:
        if line == "\n":
            section = 2
            continue
        if section == 1:
            y,x = line.strip().split("|")
            try:
                a = rules[y] 
            except:
                a = [] 
            a.append(x)
            rules[y] = a
        else:
            to_check.append(line.strip())

updates_to_check = []
for checking in to_check:
    updates_to_check.append(checking.split(","))

good_list = []
for update_to_check in updates_to_check:
    checked = []
    currently_good = True
    for update in update_to_check:
        if str(update) in rules:
            for check in checked:
                if str(check) in rules[str(update)]:
                    currently_good = False
        checked.append(update)
    if currently_good:
        good_list.append(update_to_check)

middle_list = [int(update[int((len(update) - 1)/2)]) for update in good_list]
print(sum(middle_list))


