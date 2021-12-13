# https://adventofcode.com/2021/day/11
# https://adventofcode.com/2021/day/11#part2

import os

def solve_part_one(file='../solutions/inputs/11.in'):
    octopi = load_file(file)
    steps = 100
    flashes = 0

    for step in range(steps):
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                absorb_energy(octopi, i, j)
        
        flashes += sum([len([x for x in r if x > 9]) for r in octopi])

        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                if octopi[i][j] > 9:
                    octopi[i][j] = 0

    return flashes

def solve_part_two(file='../solutions/inputs/11.in'):
    octopi = load_file(file)
    step = 0
    all_coordinated = False

    while not all_coordinated:
        step += 1
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                absorb_energy(octopi, i, j)
        
        all_coordinated = all([len([x for x in r if x > 9]) == 10 for r in octopi])

        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                if octopi[i][j] > 9:
                    octopi[i][j] = 0

    return step

def absorb_energy(octopi, i, j):
    octopi[i][j] += 1
    if octopi[i][j] == 10:
        if i > 0:
            absorb_energy(octopi, i-1, j)
            if j > 0:
                absorb_energy(octopi, i-1, j-1)
            if j < len(octopi[i-1]) - 1:
                absorb_energy(octopi, i-1, j+1)
        if i < len(octopi) - 1:
            absorb_energy(octopi, i+1, j)
            if j > 0:
                absorb_energy(octopi, i+1, j-1)
            if j < len(octopi[i+1]) - 1:
                absorb_energy(octopi, i+1, j+1)
        if j > 0:
            absorb_energy(octopi, i, j-1)
        if j < len(octopi[i]) - 1:
            absorb_energy(octopi, i, j+1)

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    return [[int(x) for x in l] for l in input.read().splitlines()]
