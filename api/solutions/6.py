# https://adventofcode.com/2021/day/6
# https://adventofcode.com/2021/day/6#part2

import os
import pprint
from collections import Counter

pp = pprint.PrettyPrinter(indent=4)

def solve_part_one(file='../solutions/inputs/6.in'):

    return get_population_after(file, 80)

def solve_part_two(file='../solutions/inputs/6.in'):
    return get_population_after(file, 256)

def get_population_after(file, days):
    fish = load_file(file)

    fish_countdown = [0 for i in range(9)]

    keys = Counter(fish).keys()
    values = Counter(fish).values()
    for i in range(len(keys)):
        fish_countdown[keys[i]] = values[i]

    for day in range(days):
        new_fish = fish_countdown.pop(0)
        fish_countdown[6] += new_fish
        fish_countdown.append(new_fish) 

    return sum(fish_countdown)

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    fish = [int(x) for x in input.read().split(',')]

    return fish
