# https://adventofcode.com/2021/day/14
# https://adventofcode.com/2021/day/14#part2

import os, sys
from collections import defaultdict
import pprint
import math
pp = pprint.PrettyPrinter(indent=4)


def solve_part_one(file):
    x_range, y_range = load_file(file)
    x_cands = []
    
    x_cands = find_x_cands(x_range)
    max_y = 0

    for x_i in x_cands:
        y_cands = find_y_cands(x_i, x_range, y_range)
        for y_i in y_cands:
            x_sim = 0
            y_sim = 0
            y_max_sim = 0
            x_vel = x_i
            y_vel = y_i
            lands_in_range = False
            
            while y_sim > y_range[0]:
                x_sim += x_vel
                y_sim += y_vel
                y_max_sim = max([y_sim, y_max_sim])

                x_vel -= abs(x_vel) / x_vel if x_vel != 0 else 0
                y_vel -= 1

                if x_range[0] <= x_sim <= x_range[1] and y_range[0] <= y_sim <= y_range[1]:
                    lands_in_range = True
            
            if lands_in_range:
                print('('+str(x_i)+', '+str(y_i)+') lands in range')
                max_y = max([y_max_sim, max_y]) 

    return max_y

def solve_part_two(file):
    x_range, y_range = load_file(file)
    successful_combos = []

    for x_i in range(min([0, x_range[0]]), max(x_range[1], 0) + 1):
        for y_i in range(min([0, y_range[0]]), max(y_range[1], 0, -y_range[0], -y_range[1]) + 1):
            x_sim = 0
            y_sim = 0
            x_vel = x_i
            y_vel = y_i
            lands_in_range = False
            
            while y_sim > y_range[0]:
                x_sim += x_vel
                y_sim += y_vel

                x_vel -= abs(x_vel) / x_vel if x_vel != 0 else 0
                y_vel -= 1

                if x_range[0] <= x_sim <= x_range[1] and y_range[0] <= y_sim <= y_range[1]:
                    lands_in_range = True
            
            if lands_in_range:
                successful_combos.append((x_i, y_i))

    pp.pprint(successful_combos)
    return len(successful_combos)

def find_x_cands(x_range):
    x_cands = []
    x_i = 1
    abs_x_min = abs(x_range[0])
    abs_x_max = abs(x_range[1])
    x_min_sign = 0 if x_range[0] == 0 else x_range[0] / abs_x_min 
    x_max_sign = 0 if x_range[1] == 0 else x_range[1] / abs_x_max

    for x_i in range(int(math.ceil(x_min_sign*(-1 + math.sqrt(1 + 8*abs_x_min))/ 2)), int(math.ceil(x_max_sign*(-1 + math.sqrt(1 + 8*abs_x_max))/ 2))): 
        abs_x_i = abs(x_i)
        x_i_sign = 0 if x_i == 0 else x_i / abs_x_i 
        sum_up_to_x_i = x_i_sign * x_i * (x_i + x_i_sign) / 2
        print (sum_up_to_x_i)
        if x_range[0] <= sum_up_to_x_i and sum_up_to_x_i <= x_range[1]:
            x_cands.append(x_i)

    return x_cands

def find_y_cands(x_i, x_range, y_range):
    return range(0, 1000)

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    line = input.read()
    line = line[13:]
    x_range = [int(x) for x in line.split(', ')[0].split('=')[1].split('..')]
    y_range = [int(y) for y in line.split(', ')[1].split('=')[1].split('..')]

    return x_range, y_range
