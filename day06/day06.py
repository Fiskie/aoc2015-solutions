import re

command_re = re.compile('([\w ]*) (\d*,\d*) through (\d*,\d*)')


def get_empty_grid(size):
    cols = []

    while len(cols) < size:
        row = []

        while len(row) < size:
            row.append(0)

        cols.append(row)

    return cols


def interpret(string):
    parts = command_re.match(string).groups()
    instruction = parts[0]
    start = list(map(lambda n: int(n), parts[1].split(',')))
    end = list(map(lambda n: int(n), parts[2].split(',')))
    return instruction, start, end


def set_light_part_1(instruction, current_value):
    if instruction == "turn on":
        return 1
    elif instruction == "turn off":
        return 0
    else:
        return 1 if current_value == 0 else 0


def set_light_part_2(instruction, current_value):
    if instruction == "turn on":
        return current_value + 1
    elif instruction == "turn off":
        return max(0, current_value - 1)
    else:
        return current_value + 2


def execute(command, grid, function):
    for x in range(command[1][0], command[2][0] + 1):
        for y in range(command[1][1], command[2][1] + 1):
            grid[x][y] = function(command[0], grid[x][y])


grid_size = 1000
grid = get_empty_grid(grid_size)

with open('day06_input.txt', 'r') as f:
    for line in f:
        execute(interpret(line), grid, set_light_part_1)

print("Part 1: %d lights are on" % sum(map(lambda row: sum(row), grid)))

grid = get_empty_grid(grid_size)

with open('day06_input.txt', 'r') as f:
    for line in f:
        execute(interpret(line), grid, set_light_part_2)

print("Part 2: Total brightness is %d" % sum(map(lambda row: sum(row), grid)))
