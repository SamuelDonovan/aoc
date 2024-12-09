# --- Day 6: Guard Gallivant ---

# From the python standard library
import os
import sys

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = UP

    def rotate_right(self):
        if self.direction == DOWN:
            self.direction = LEFT
        elif self.direction == RIGHT:
            self.direction = DOWN
        elif self.direction == UP:
            self.direction = RIGHT
        elif self.direction == LEFT:
            self.direction = UP
        else:
            print("Failed to rotate player")
            sys.exit(1)

    def move(self):
        self.x = self.x + self.direction[0]
        self.y = self.y + self.direction[1]


class PlayerMap:
    def __init__(self, guard):
        self.full_map = []
        self.guard = guard
        self.obstacles = 0 
        self.tiles = 0 
        with open("input.txt", "r") as file:
            for y, row in enumerate(file):
                if "^" in row:
                    self.guard.x = row.find("^")
                    self.guard.y = y
                this_row = [pos for pos in row if pos != "\n"]
                self.tiles += len(this_row)
                self.obstacles += this_row.count("#")
                self.full_map.append(this_row)

    def show(self):
        for row in self.full_map:
            print(row)

    def write(self):
        with open("output.txt", "w") as file:
            for row in self.full_map:
                for position in row:
                    file.write(position)
                file.write("\n")

    def clear(self):
        os.system("clear")

    def move_guard(self):
        if (guard.y + guard.direction[1] < 0):
            raise Exception("Out of bounds") 
        if (guard.x + guard.direction[1] < 0):
            raise Exception("Out of bounds") 
        if (self.full_map[guard.y + guard.direction[1]][guard.x + guard.direction[0]] == "#"):
            self.guard.rotate_right()
            return
        self.full_map[guard.y][guard.x] = "X"
        self.guard.move()
        if guard.direction == UP:
            self.full_map[guard.y][guard.x] = "^"
        elif guard.direction == DOWN:
            self.full_map[guard.y][guard.x] = "v"
        elif guard.direction == LEFT:
            self.full_map[guard.y][guard.x] = "<"
        elif guard.direction == RIGHT:
            self.full_map[guard.y][guard.x] = ">"
        else:
            print("Failed to move gaurd")
            sys.exit(1)

    def get_traveled(self):
        traveled = 0
        for row in self.full_map:
            for position in row:
                if position == "X":
                    traveled = traveled + 1
        # Traveled + 1 to account for where the player is currently
        return traveled + 1

    def get_avalible_spaces(self):
        return self.tiles - self.obstacles


if __name__ == "__main__":
    guard = Player()
    player_map = PlayerMap(guard)

    while(True):
        try:
            player_map.move_guard()
        except:
            print(f"Traveled = {player_map.get_traveled()}")
            break
    player_map.write()
