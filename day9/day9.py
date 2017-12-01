import re

test = re.compile('(\w+) to (\w+) = (\d+)')


def create_table(resource):
    """
    will create a 2d dict that can be queried as [location][location]
    :rtype: dict
    """
    table = {}

    for line in resource:
        params = test.match(line).groups()
        table[params[0]] = table.get(params[0], {})
        table[params[1]] = table.get(params[1], {})
        table[params[0]][params[1]] = int(params[2])
        table[params[1]][params[0]] = int(params[2])

    return table


def shortest_route(attempt, best):
    return not best or attempt < best


def longest_route(attempt, best):
    return not best or attempt > best


def traverse(table, heuristic, targets, starting_point):
    best_score = None
    best_target = None

    # clone list and remove starting point
    targets = targets[:]
    targets.remove(starting_point)

    for target in targets:
        score = table[starting_point][target]

        if heuristic(score, best_score):
            best_score = score
            best_target = target

    if targets:
        # print("%s was the best route to take from %s (dist: %d)" % (best_target, starting_point, best_score))
        return best_score + traverse(table, heuristic, targets, best_target)

    # print("no more targets to take from %s" % starting_point)
    return 0


def find_best_route(table, heuristic):
    best_score = None

    for starting_point in table.keys():
        targets = list(table.keys())
        # print("traversing from %s" % starting_point)
        score = traverse(table, heuristic, targets, starting_point)
        # print("starting from %s got a score of %d" % (starting_point, score))

        if heuristic(score, best_score):
            best_score = score

    return best_score


with open('day9_input.txt', 'r') as f:
    table = create_table(f)
    best_score = find_best_route(table, shortest_route)
    print("Part 1: best route found had a score of %d" % best_score)


with open('day9_input.txt', 'r') as f:
    table = create_table(f)
    best_score = find_best_route(table, longest_route)
    print("Part 2: best route found had a score of %d" % best_score)
