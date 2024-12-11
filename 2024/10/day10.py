# --- Day 10: Hoof It ---

possible_directions = []
for i1 in "UDLR":
    for i2 in "UDLR":
        for i3 in "UDLR":
            for i4 in "UDLR":
                for i5 in "UDLR":
                    for i6 in "UDLR":
                        for i7 in "UDLR":
                            for i8 in "UDLR":
                                for i9 in "UDLR":
                                    possible_directions.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 +i8 + i9)

trails = []
with open("input.txt", "r") as file:
    for line in file:
        trails.append(list(line.rstrip()))

def do_it_connect(point1: tuple, point2: tuple, direction: str):
    for idx, udlr in enumerate(list(direction)):
        if udlr == "U":
            if point1[1] + 1 == (idx + 1):
                point1[1] = point1[1] + 1
                continue 
        elif udlr == "D":
            if point1[1] - 1 == (idx + 1):
                point1[1] = point1[1] - 1
                continue 
        if udlr == "R":
            if point1[0] + 1 == (idx + 1):
                point1[0] = point1[0] + 1
                continue 
        elif udlr == "L":
            if point1[0] - 1 == (idx + 1):
                point1[0] = point1[0] - 1
                continue 
        else:
            return false
    return point1 == point2
