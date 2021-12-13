# https://adventofcode.com/2021/day/12
# https://adventofcode.com/2021/day/12#part2

import os
from collections import Counter

def solve_part_one(file='../solutions/inputs/12.in'):
    edges = load_file(file)
    complete_paths = []
    graph = build_graph(edges)

    explore_caves(graph, 'start', [], complete_paths, 1, 10)

    return len(complete_paths)

def solve_part_two(file='../solutions/inputs/12.in'):
    edges = load_file(file)
    complete_paths = []
    graph = build_graph(edges)

    explore_caves(graph, 'start', [], complete_paths, 2, 1)

    return len(complete_paths)

def build_graph(edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph.keys():
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])

        if edge[1] not in graph.keys():
            graph[edge[1]] = []
        graph[edge[1]].append(edge[0])
    return graph

def is_large_cave(cave):
    return cave == cave.upper()

def explore_caves(graph, current, path, complete_paths, max_small_cave_visits, max_count_duplicates):
    path = path + [current]
    if current == 'end':
        complete_paths.append(path)
    elif len(path) == 1 or current != 'start': 
        for dest in graph[current]:
            if is_large_cave(dest) or (path.count(dest) < max_small_cave_visits and count_small_duplicates(path, max_small_cave_visits) <= max_count_duplicates):
                explore_caves(graph, dest, path, complete_paths, max_small_cave_visits, max_count_duplicates)

def count_small_duplicates(path, max_small_cave_visits):
    stats = Counter(path)
    return sum([1 if not is_large_cave(k) and stats[k] == max_small_cave_visits else 0 for k in stats.keys()])

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    return [(l.split('-')[0], l.split('-')[1]) for l in input.read().splitlines()]
