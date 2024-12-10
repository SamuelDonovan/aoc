# --- Day 9: Disk Fragmenter ---

from tqdm import tqdm

def show_city(city: list):
    for line in city:
        print(line)
    with open("output.txt", "w") as file:
        for row in city:
            for position in row:
                file.write(position)
            file.write("\n")


            
with open("input.txt", "r") as file:
    disk_map = list(file.read().strip())

is_a_file = True
file_counter = 0
sorted_disk_map = ""
for block in disk_map:
    if is_a_file:
        sorted_disk_map += int(block )* str(file_counter)
        file_counter += 1
    else:
        sorted_disk_map += int(block) * "." 
    is_a_file = not is_a_file


sorted_disk_map = list(sorted_disk_map)
for idx in tqdm(range(len(sorted_disk_map))):
    if sorted_disk_map[idx] == ".":
        for jdx, inverse_block in enumerate(reversed(sorted_disk_map)):
            if inverse_block != ".":
                sorted_disk_map[idx] = inverse_block 
                sorted_disk_map[len(sorted_disk_map) - 1 - jdx] = "." 
                break
sorted_disk_map = "".join(sorted_disk_map)
sorted_disk_map = sorted_disk_map.replace(".", "")

print(sorted_disk_map)

checksum = 0
sorted_disk_map = list(sorted_disk_map)
for idx in tqdm(range(len(sorted_disk_map))):
    checksum += idx * int(sorted_disk_map[idx])

print(checksum)


