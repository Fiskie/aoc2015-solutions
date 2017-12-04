# This solution works by creating a bit map corresponding to the container list.
# This will be used to iterate over every possible combination (2**20).
# In theory this method will work with up to 64 container sizes. Not sure how to improve that.


def create_bit_map(size):
    bitset = []
    bit = 1

    for i in range(0, size):
        bitset.append(bit)
        bit *= 2

    return list(reversed(bitset))

with open("day17_input.txt", 'r') as f:
    containers = list(map(lambda val: int(val), f.read().split('\n')))

size = len(containers)
bit_map = create_bit_map(size)
total = 0

totals = {}

for i in range(0, 2**size):
    litres = 0
    used = 0

    for bit in range(0, size):
        if i > bit_map[bit]:
            i -= bit_map[bit]
            litres += containers[bit]
            used += 1

    if litres == 150:
        totals[used] = totals.get(used, 0) + 1

print("Part 1: %d combinations.", sum(totals.values()))
print("Part 2: See below.")

for key, value in totals.items():
    print("%d containers: %d combinations." % (key, value))