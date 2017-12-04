import re

# todo: write string increment func, got all the validation logic done.

bad_letters = re.compile('[iol]')


def get_pair_count(string):
    positions = {}

    for i in range(0, len(string) - 1):
        if string[i+1] == string[i]:
            if not positions.get(i-1):
                positions[i] = True

    return len(positions.keys())


def has_straight(string):
    for i in range(0, len(string) - 2):
        if (
            string[i+2] == chr(ord(string[i])+2) and
            string[i+1] == chr(ord(string[i])+1)
        ):
            return True

    return False


def contains_bad_letter(string):
    return True if bad_letters.search(string) else False


def is_valid(string):
    return get_pair_count(string) >= 2 and has_straight(string) and not contains_bad_letter(string)


input = "cqjxjnds"
