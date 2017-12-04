# todo: part 2 - is there an easy way or am i breaking out the regex

with open('day08_input.txt', 'r') as f:
    total_literal_len = 0
    total_char_len = 0

    for line in f:
        total_literal_len += len(line)
        total_char_len += len(line.decode('string_escape')) - 2
    pass

    print("Part 1: Diff is %d (%d - %d)" % (total_literal_len - total_char_len, total_literal_len, total_char_len))

