# https://adventofcode.com/2021/day/9
# https://adventofcode.com/2021/day/9#part2

import os

def solve_part_one(file='../solutions/inputs/9.in'):
    map = load_file(file)
    sinks = []

    for i in range(len(map)):
        for j in  range(len(map[i])):
            if is_sink(map, i, j):
                sinks.append(map[i][j])

    return sum(sinks) + len(sinks)

def solve_part_two(file='../solutions/inputs/9.in'):
    map = load_file(file)
    basins = []

    for i in range(len(map)):
        for j in  range(len(map[i])):
            if is_sink(map, i, j):
                basins.append(find_basin(map, i, j))

    print(basins[-3:])

    prod = 1
    for b in sorted(basins)[-3:]:
        prod *= b

    return prod

def is_sink(map, i, j):
    is_sink = True
    if i > 0:
        is_sink = is_sink and map[i][j] < map[i-1][j]

    if j > 0:
        is_sink = is_sink and map[i][j] < map[i][j-1]

    if i < len(map)-1:
        is_sink = is_sink and map[i][j] < map[i+1][j]

    if j < len(map[i])-1:
        is_sink = is_sink and map[i][j] < map[i][j+1]
    
    return is_sink

def find_basin(map, i, j):
    basin_mem = [(i, j)]
    basin_to_process = get_higher_neighbors(map, i, j)
    while len(basin_to_process) > 0:
        basin_mem_cand = basin_to_process.pop(0)
        higher_neighbors = get_higher_neighbors(map, basin_mem_cand[0], basin_mem_cand[1])
        for n in higher_neighbors:
            if n not in basin_to_process and n not in basin_mem:
                basin_to_process.append(n)
        basin_mem.append(basin_mem_cand)

    return len(basin_mem)

def get_higher_neighbors(map, i, j):
    higher_neighbors = []
    if i > 0 and map[i-1][j] < 9 and map[i][j] < map[i-1][j]:
        higher_neighbors.append((i-1, j))

    if j > 0 and map[i][j-1] < 9 and map[i][j] < map[i][j-1]:
        higher_neighbors.append((i, j-1))

    if i < len(map)-1 and map[i+1][j] < 9 and map[i][j] < map[i+1][j]:
        higher_neighbors.append((i+1, j))

    if j < len(map[i])-1 and map[i][j+1] < 9 and map[i][j] < map[i][j+1]:
        higher_neighbors.append((i, j+1))

    return higher_neighbors

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    map = [[int(c) for c in l if c != ''] for l in input.read().splitlines()]
    return map
