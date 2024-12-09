# --- Day 8: Resonant Collinearity ---

import string
import itertools 

def sub_points(point1: tuple, point2: tuple) -> tuple:
    return (point1[0] - point2[0], point1[1] - point2[1])

def add_points(point1: tuple, point2: tuple) -> tuple:
    return (point1[0] + point2[0], point1[1] + point2[1])

def negate_point(point: tuple) -> tuple:
    return (-point[0], -point[1])

def check_point(city: list, point: tuple) -> bool:
    if point[0] < 0:
        return False
    if point[1] < 0:
        return False
    if point[0] > len(city[0]) - 1:
        return False
    if point[1] > len(city) - 1:
        return False
    return True

def show_city(city: list):
    for line in city:
        print(line)
    with open("output.txt", "w") as file:
        for row in city:
            for position in row:
                file.write(position)
            file.write("\n")


def count_interence(city: list) -> int:
    count = 0
    for line in city:
        for pos in line:
            if pos == "#":
                count += 1
    return count
            
city = []
with open("input.txt", "r") as file:
    for line in file:
        city.append(list(line.rstrip()))

frequencies = {}
for frequency in list(string.ascii_letters):
    frequencies[frequency] = []
for frequency in list(string.digits):
    frequencies[frequency] = []

y = 0
for line in city:
    for frequency in frequencies:
        for x, pos in enumerate(line):
            if frequency == pos:
                frequencies[frequency].append((x, y))
    y += 1

available_frequencies = []
for frequency in frequencies:
    if frequencies[frequency]:
        available_frequencies.append(frequency)

interference = []
for frequency in available_frequencies:
    for point1, point2 in itertools.combinations(frequencies[frequency], 2):
        distance = sub_points(point1, point2)
        point_to_add = add_points(point1, distance)
        if check_point(city, point_to_add):
            interference.append(point_to_add)
        point_to_add = sub_points(point2, distance)
        if check_point(city, point_to_add):
            interference.append(point_to_add)

for pos in interference:
    city[pos[1]][pos[0]] = "#"

print(count_interence(city))

# --- Part 2 ---

def count_interence(city: list) -> int:
    count = 0
    for line in city:
        for pos in line:
            if pos != ".":
                count += 1
    return count

city = []
with open("input.txt", "r") as file:
    for line in file:
        city.append(list(line.rstrip()))

frequencies = {}
for frequency in list(string.ascii_letters):
    frequencies[frequency] = []
for frequency in list(string.digits):
    frequencies[frequency] = []

y = 0
for line in city:
    for frequency in frequencies:
        for x, pos in enumerate(line):
            if frequency == pos:
                frequencies[frequency].append((x, y))
    y += 1

available_frequencies = []
for frequency in frequencies:
    if frequencies[frequency]:
        available_frequencies.append(frequency)

interference = []
for frequency in available_frequencies:
    for point1, point2 in itertools.combinations(frequencies[frequency], 2):
        distance = sub_points(point1, point2)
        while(True):
            point1 = add_points(point1, distance)
            if check_point(city, point1):
                interference.append(point1)
                continue
            break
        while(True):
            point2 = sub_points(point2, distance)
            if check_point(city, point2):
                interference.append(point2)
                continue
            break

for pos in interference:
    city[pos[1]][pos[0]] = "#"

print(count_interence(city))
