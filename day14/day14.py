import re

class Reindeer(object):
    distance_traveled = 0
    state_ticks = 0
    ticks = 0
    points = 0

    def __init__(self, name, fly_speed, fly_time, rest_time):
        self.name = name
        self.fly_speed = fly_speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.state = "flying"

    def simulate(self):
        if self.state == "flying":
            self.distance_traveled += self.fly_speed

        self.state_ticks += 1

        if self.state == "flying" and self.state_ticks == self.fly_time:
            self.state_ticks = 0
            self.state = "resting"
        elif self.state == "resting" and self.state_ticks == self.rest_time:
            self.state_ticks = 0
            self.state = "flying"


reindeer_re = re.compile('(\w*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.')
reindeers = []

with open("day14_input.txt", 'r') as f:
    for line in f:
        matches = reindeer_re.match(line).groups()
        reindeers.append(Reindeer(matches[0], int(matches[1]), int(matches[2]), int(matches[3])))

comet = Reindeer(name="Comet", fly_speed=14, fly_time=10, rest_time=127)
dancer = Reindeer(name="Dancer", fly_speed=16, fly_time=11, rest_time=162)


def get_top_distance(reindeers):
    top_distance = 0

    for reindeer in reindeers:
        top_distance = max(top_distance, reindeer.distance_traveled)

    return top_distance


for i in range(0, 2503):
    for reindeer in reindeers:
        reindeer.simulate()

    # because multiple reindeer may be leading at one time
    top_dist = get_top_distance(reindeers)

    for reindeer in reindeers:
        if reindeer.distance_traveled == top_dist:
            reindeer.points += 1


for reindeer in reindeers:
    print("%7s stats: distance %.4d, points %.4d" % (reindeer.name, reindeer.distance_traveled, reindeer.points))
