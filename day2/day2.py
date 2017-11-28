def find_shortest_distance_around_sides(l, w, h):
    return min(l*2 + w*2, w*2 + h*2, l*2 + h*2)


def find_volume(l, w, h):
    return l*w*h


def find_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l


def find_smallest_side(l, w, h):
    return min(l*w, w*h, l*h)

total_wrap = 0
total_ribbon = 0

with open('day2_input.txt') as f:
    for line in f:
        vals = map(lambda x: int(x), line.split('x'))
        total_wrap += find_surface_area(*vals) + find_smallest_side(*vals)
        total_ribbon += find_shortest_distance_around_sides(*vals) + find_volume(*vals)

print("Total wrapping paper required is %d sq. ft" % total_wrap)
print("Total ribbon required is %d ft" % total_ribbon)