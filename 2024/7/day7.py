# --- Day 7: Bridge Repair ---


def get_permutations(size: int):
    operations = []
    for idx in range(2 ** (size - 1)):
        binary = str(format(idx, "b").zfill(size - 1))
        operations.append(binary.replace("0", "+").replace("1", "*"))
    return operations


operations = {}
with open("input.txt", "r") as file:
    for line in file:
        result, operands = line.split(":")
        operations[result] = operands.split()

tested_sum = 0
for key in operations:
    permutations = get_permutations(len(operations[key]))
    for permutation in permutations:
        permutation = list(permutation)
        op_to_test = operations[key].copy()
        op1 = op_to_test.pop(0)
        while True:
            perm = permutation.pop(0)
            op2 = op_to_test.pop(0)
            op1 = eval(f"{op1} {perm} {op2}")
            if len(op_to_test) == 0:
                break
        if key == str(op1):
            tested_sum += int(key)
            break

print(tested_sum)
