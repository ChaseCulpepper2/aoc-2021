# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2#part2

import os

def solve_part_one(file='../solutions/inputs/2.in'):
    directions = load_file(file)

    step_changes = [((int(d['distance']) if d['direction'] == 'forward' else 0), ((1 if d['direction'] == 'down' else -1) * int(d['distance']) if d['direction'] in ['up', 'down'] else 0)) for d in directions]

    location = (sum(i[0] for i in step_changes), sum(i[1] for i in step_changes))

    return location[0] * location[1]

def solve_part_two(file='../solutions/inputs/2.in'):
    directions = load_file(file)
    x = 0
    y = 0
    aim = 0

    for d in directions:
        if d['direction'] == 'forward':
            x += int(d['distance'])
            y += int(d['distance']) * aim
        else:
            aim += (1 if d['direction'] == 'down' else -1) * int(d['distance'])
        
    return x * y

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = [{'direction':a.split(' ')[0], 'distance':a.split(' ')[1]} for a in input.read().splitlines()]
    return lines