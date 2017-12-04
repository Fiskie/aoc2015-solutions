import json


def sum_up(blob, ignore_red=False):
    sum = 0

    if isinstance(blob, list):
        for item in blob:
            sum += sum_up(item, ignore_red)
    elif isinstance(blob, dict):
        for item in blob.values():
            if ignore_red and item == "red":
                return 0

            sum += sum_up(item, ignore_red)
    elif isinstance(blob, int):
        sum += blob

    return sum


with open('day12_input.json', 'r') as f:
    data = json.loads(f.read())
    print("Part 1: sum is %d" % sum_up(data))
    print("Part 2: sum is %d" % sum_up(data, True))
