# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6#part2

import os
import pprint
from collections import Counter

pp = pprint.PrettyPrinter(indent=4)

def solve_part_one(file='../solutions/inputs/7.in'):
    crabs = load_file(file)

    min_movement = 10000000000
    for i in range(max(crabs)+1):
        movement_i = sum([abs(crab - i) for crab in crabs])
        min_movement = min([min_movement, movement_i])
    return min_movement

def solve_part_two(file='../solutions/inputs/7.in'):
    crabs = load_file(file)

    min_fuel = 10000000000
    for i in range(max(crabs)+1):
        movement_i = sum([abs(crab - i) * (1 + abs(crab - i)) for crab in crabs])/2
        min_fuel = min([min_fuel, movement_i])
    return min_fuel

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    crabs = [int(x) for x in input.read().split(',')]

    return crabs
