# https://adventofcode.com/2021/day/1
# https://adventofcode.com/2021/day/1#part2

import os

def solve_part_one(file='../solutions/inputs/1.in'):
    readings = load_file(file)
    changes = [readings[i+1] > readings[i] for i in range(len(readings)-1)]

    count_increasing_changes = changes.count(True)

    return count_increasing_changes

def solve_part_two(file='../solutions/inputs/1.in'):
    readings = load_file(file)
    changes = [readings[i+3] + readings[i+2] + readings[i+1] > readings[i+2] + readings[i+1] + readings[i] for i in range(len(readings)-3)]

    count_increasing_changes = changes.count(True)

    return count_increasing_changes

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = [int(a) for a in input.read().splitlines()]
    return lines