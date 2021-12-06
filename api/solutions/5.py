# https://adventofcode.com/2021/day/5
# https://adventofcode.com/2021/day/5#part2

import os
import pprint
pp = pprint.PrettyPrinter(indent=4)

def solve_part_one(file='../solutions/inputs/5.in'):
    vents = load_file(file)
    locations = [[0 for j in range(1000)] for i in range(1000)]

    for vent in vents:
        x1 = vent['start']['x']
        y1 = vent['start']['y']
        x2 = vent['end']['x']
        y2 = vent['end']['y']
        if x1 == x2:
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                locations[x1][y] += 1
        elif y1 == y2:
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                locations[x][y1] += 1

    count_two_more = sum(sum([1 if r > 1 else 0 for r in c]) for c in locations)
    return count_two_more

def solve_part_two(file='../solutions/inputs/5.in'):
    vents = load_file(file)
    locations = [[0 for j in range(1000)] for i in range(1000)]

    for vent in vents:
        x1 = vent['start']['x']
        y1 = vent['start']['y']
        x2 = vent['end']['x']
        y2 = vent['end']['y']
        if x1 == x2:
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                locations[x1][y] += 1
        elif y1 == y2:
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                locations[x][y1] += 1
        else:
            if x2 - x1 == y2 - y1:
                if x2 - x1 > 0:
                    for i in range(x2-x1+1):
                        locations[x1 + i][y1 + i] += 1
                else:
                    for i in range(x1-x2+1):
                        locations[x2 + i][y2 + i] += 1
            else:
                if x2 - x1 > 0:
                    for i in range(x2-x1+1):
                        locations[x1 + i][y1 - i] += 1
                else:
                    for i in range(x1-x2+1):
                        locations[x2 + i][y2 - i] += 1

    count_two_more = sum(sum([1 if r > 1 else 0 for r in c]) for c in locations)
    return count_two_more

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    vents = [{'start': {'x': int(l.split(' -> ')[0].split(",")[0]), 'y': int(l.split(' -> ')[0].split(",")[1])}, 'end': {'x': int(l.split(' -> ')[1].split(",")[0]), 'y': int(l.split(' -> ')[1].split(",")[1])}} for l in input.read().splitlines()]

    return vents
