# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3#part2

import os

def solve_part_one(file='../solutions/inputs/3.in'):
    readings = load_file(file)
    sums = map(sum, zip(*readings))
    gamma = [(1 if s > len(readings)/2 else 0) for s in sums]
    epsilon = [(0 if s > len(readings)/2 else 1) for s in sums]

    gamma_ten = bin_to_decimal(gamma)
    epsilon_ten = bin_to_decimal(epsilon)

    return gamma_ten * epsilon_ten

def solve_part_two(file='../solutions/inputs/3.in'):
    readings = load_file(file)
    oxy_reading = []
    co_reading = []

    oxy_cand = readings
    co_cand = readings

    for i in range(len(readings[0])):
        if len(oxy_cand) > 1:
            oxy_sums_i = map(sum, zip(*oxy_cand))
            oxy_i_reading = (1 if 2*oxy_sums_i[i] >= len(oxy_cand) else 0)
            oxy_cand = [cand for cand in oxy_cand if cand[i] == oxy_i_reading]
            oxy_reading.append(oxy_i_reading)
        else:
            oxy_reading.append(oxy_cand[0][i])
        
        if len(co_cand) > 1:
            co_sums_i = map(sum, zip(*co_cand))
            co_i_reading = (1 if 2*co_sums_i[i] < len(co_cand) else 0)
            co_cand = [cand for cand in co_cand if cand[i] == co_i_reading]
            co_reading.append(co_i_reading)
        else:
            co_reading.append(co_cand[0][i])

    oxy = bin_to_decimal(oxy_reading)
    co = bin_to_decimal(co_reading)
    print('oxy:',oxy_reading)
    print('co:',co_reading)
    return co * oxy

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = [[int(x) for x in list(a)] for a in input.read().splitlines()]
    return lines

def bin_to_decimal(bit_list):
    dec = sum([g * (2 ** (len(bit_list)-ind-1)) for ind, g in enumerate(bit_list)])
    return dec
