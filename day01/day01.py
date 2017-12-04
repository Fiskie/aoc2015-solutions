match_chars = {'(': 1, ')': -1}


def find_floor(chars, on_found_basement):
    found_basement = False
    current_floor = 0
    pos = 0

    for char in chars:
        pos += 1
        current_floor += match_chars[char]

        if not found_basement and current_floor < 0:
            on_found_basement(pos)
            found_basement = True

    return current_floor


def announce_basement(pos):
    print("basement is reached on char %d" % pos)

with open("day01_input.txt") as f:
    floor = find_floor(f.read(), announce_basement)
    print("final floor is %d" % floor)

