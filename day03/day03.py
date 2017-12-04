def drop_present(vec):
    world[vec.__str__()] = world.get(vec.__str__(), 0) + 1


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __str__(self):
        return "%d,%d" % (self.x, self.y)

moves = {
    "^": Vector(0, 1),
    "v": Vector(0, -1),
    "<": Vector(-1, 0),
    ">": Vector(1, 0),
}

world = {}
santa = Vector(0, 0)

with open('day03_input.txt') as f:
    # one present is dropped before Santa starts moving
    drop_present(santa)

    for char in f.read():
        santa.add(moves[char])
        drop_present(santa)

print("Part one: %d houses received at least one present" % len(world.keys()))

world = {}
santa = Vector(0, 0)
robo_santa = Vector(0, 0)

with open('day03_input.txt') as f:
    # one present is dropped before Santa starts moving
    # (assumed the same for robo santa too, but we don't care about quantity)
    drop_present(santa)
    is_robo_turn = False

    for char in f.read():
        actor = robo_santa if is_robo_turn else santa
        actor.add(moves[char])
        drop_present(actor)
        is_robo_turn = not is_robo_turn

print("Part two: %d houses received at least one present" % len(world.keys()))
