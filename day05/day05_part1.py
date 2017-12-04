bad_strings = ["ab", "cd", "pq", "xy"]
vowels = 'aeiou'


def is_nice(string):
    vowel_count = 0
    has_double = False

    for i in range(0, len(string)):
        if string[i] in vowels:
            vowel_count += 1

        if i == 0:  # the next checks require a previous character to exist
            continue

        if string[i-1] == string[i]:
            has_double = True

        if (string[i-1] + string[i]) in bad_strings:
            return False

    return vowel_count >= 3 and has_double

# Sanity test our function with a few asserts based on the example strings given
assert is_nice('ugknbfddgicrmopn')  # nice string
assert not is_nice("jchzalrnumimnmhp")  # no double letter
assert not is_nice("haegwjzuvuyypxyu")  # contains bad string
assert not is_nice("dvszwmarrgswjxmb")  # contains one vowel

nice_count = 0

with open('day05_input.txt', 'r') as f:
    for line in f:
        if is_nice(line):
            nice_count += 1

print("%d strings are nice!" % nice_count)
