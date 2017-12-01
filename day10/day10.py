def get_next(sequence):
    new = ""
    current_digit = None
    current_count = 0

    for char in sequence:
        if not current_digit == char:
            if current_digit:
                new += str(current_count) + current_digit

            current_count = 1
            current_digit = char
        else:
            current_count += 1

    if current_digit:
        new += str(current_count) + current_digit

    return new


def repeat(string, times):
    for i in range(0, times):
        string = get_next(string)

    return string


assert get_next("1") == "11"  # 1 copy of digit 1
assert get_next("11") == "21"  # 2 copies of digit 1
assert get_next("21") == "1211"  # one 2 followed by one 1
assert get_next("1211") == "111221"  # one 1, one 2, and two 1s
assert get_next("111221") == "312211"  # three 1s, two 2s, and one 1

input_string = "3113322113"

print("Part 1: length of the final string is %s" % len(repeat(input_string, 40)))
print("Part 2: length of the final string is %s" % len(repeat(input_string, 50)))
