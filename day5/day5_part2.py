def is_nice(string):
    has_repeated_char = False
    has_repeated_pair = False

    for i in range(0, len(string)):
        if i >= 2 and string[i - 2] == string[i]:
            has_repeated_char = True

        if i >= 1:
            pos = string.find(string[i - 1] + string[i])

            if not pos == -1 and pos < i - 2:
                has_repeated_pair = True

    return has_repeated_char and has_repeated_pair

# Like with part 1, some more assertion tests
assert is_nice('qjhvhtzxzqqjkmpb')  # nice string
assert is_nice("xxyxx")  # nice string, with overlapping rules
assert not is_nice("uurcxstgmygtbstg")  # no repeated letter
assert not is_nice("ieodomkazucvgmuy")  # no pair appearing twice

nice_count = 0

with open('day5_input.txt', 'r') as f:
    for line in f:
        if is_nice(line):
            nice_count += 1

print("%d strings are nice!" % nice_count)
