# https://adventofcode.com/2021/day/14
# https://adventofcode.com/2021/day/14#part2

import os
from collections import Counter
import pprint
pp = pprint.PrettyPrinter(indent=4)


def solve_part_one(file='../solutions/inputs/14.in'):
    instructions = load_file(file)
    return apply_insertions_dynamic(instructions, 10)

def solve_part_two(file='../solutions/inputs/14.in'):
    instructions = load_file(file)
    return apply_insertions_dynamic(instructions, 40)

def apply_insertions_dynamic(instructions, num_steps):
    polymer_stats = Counter([instructions['template'][i:i+2] for i in range(len(instructions['template'])-1)])
    insertion_rules = instructions['insertion_rules']
    insertion_keys = insertion_rules.keys()

    for step in range(num_steps):
        stats = {}
        for pair in polymer_stats.keys():
            if pair in insertion_keys:
                new_pair_1 = pair[0] + insertion_rules[pair]
                if new_pair_1 not in stats.keys():
                    stats[new_pair_1] = 0
                stats[new_pair_1] += polymer_stats[pair]

                new_pair_2 = insertion_rules[pair] + pair[1]
                if new_pair_2 not in stats.keys():
                    stats[new_pair_2] = 0
                stats[new_pair_2] += polymer_stats[pair]

            else:
                if pair not in stats.keys():
                    stats[pair] = 0
                stats[pair] += polymer_stats[pair]

        polymer_stats = stats

    ind_polymer_stats = split_into_individual_stats(polymer_stats, instructions['template'][0], instructions['template'][-1:])
    
    return (max(ind_polymer_stats.values()) - min(ind_polymer_stats.values())) / 2
            
def split_into_individual_stats(pair_stats, first_char, last_char):
    ind_polymer_stats = {first_char: 1, last_char: 1}
    for pair in pair_stats:
        first = pair[0]
        second = pair[1]
        if first not in ind_polymer_stats.keys():
            ind_polymer_stats[first] = 0
        ind_polymer_stats[first] += pair_stats[pair]

        if second not in ind_polymer_stats.keys():
            ind_polymer_stats[second] = 0
        ind_polymer_stats[second] += pair_stats[pair]
    return ind_polymer_stats

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = input.read().splitlines()

    empty_line_i = lines.index('')
    template = lines[:empty_line_i][0]
    insertion_rules = {}

    for rule in lines[empty_line_i+1:]:
        tokens = rule.split(' -> ')
        insertion_rules[tokens[0]] = tokens[1]

    return {'template': template, 'insertion_rules': insertion_rules}
