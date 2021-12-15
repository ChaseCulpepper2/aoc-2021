# https://adventofcode.com/2021/day/14
# https://adventofcode.com/2021/day/14#part2

import os, sys
from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)
from heapq import *


def solve_part_one(file='../solutions/inputs/14.in'):
    graph = load_file(file)
    start = (0,0)
    end = (len(graph[0])-1, len(graph)-1)
    return get_shortest_path_heap(graph, start, end)

def solve_part_two(file='../solutions/inputs/14.in'):
    tile = load_file(file)
    graph = expand_tile(tile)
    start = (0,0)
    end = (len(graph[0])-1, len(graph)-1)
    return get_shortest_path_heap(graph, start, end)

def get_shortest_path(graph, start, end):
    dist = [[sys.maxint for j in range(len(graph[i]))] for i in range(len(graph))]
    dist[start[1]][start[0]] = 0
    num_points = sum([len(l) for l in graph])
    discovered = [[False for j in range(len(graph[i]))] for i in range(len(graph))]

    for step in range(num_points):
        if step % 100 == 0:
            print('step', step)
        vert = min_dist(dist, discovered)
        x = vert[0]
        y = vert[1]
        discovered[y][x] = True

        if vert == end:
            break

        if x > 0 and not discovered[y][x-1] and dist[y][x-1] > dist[y][x] + graph[y][x-1]:
            dist[y][x-1] = dist[y][x] + graph[y][x-1]

        if x < len(graph[y])-1 and not discovered[y][x+1] and dist[y][x+1] > dist[y][x] + graph[y][x+1]:
            dist[y][x+1] = dist[y][x] + graph[y][x+1]
        
        if y > 0 and not discovered[y-1][x] and dist[y-1][x] > dist[y][x] + graph[y-1][x]:
            dist[y-1][x] = dist[y][x] + graph[y-1][x]
                
        if y < len(graph)-1 and not discovered[y+1][x] and dist[y+1][x] > dist[y][x] + graph[y+1][x]:
            dist[y+1][x] = dist[y][x] + graph[y+1][x]

    return dist[end[1]][end[0]]

def min_dist(dist, discovered):
    min = sys.maxint
    min_point = (-1, -1)

    for j in range(len(dist)):
        for i in range(len(dist[j])):
            if dist[j][i] < min and not discovered[j][i]:
                min = dist[j][i]
                min_point = (i, j)

    return min_point

def get_shortest_path_heap(graph, start, end):
    graph_map = defaultdict(list)
    start_key = str(start[1])+'_'+str(start[0])
    end_key = str(end[1])+'_'+str(end[0])

    for j in range(len(graph)):
        for i in range(len(graph[j])):
            cur_key = str(j)+'_'+str(i)
            if i > 0:
                graph_map[cur_key].append((graph[j][i-1], str(j)+'_'+str(i-1)))

            if i < len(graph[j])-1:
                graph_map[cur_key].append((graph[j][i+1], str(j)+'_'+str(i+1)))
            
            if j > 0:
                graph_map[cur_key].append((graph[j-1][i], str(j-1)+'_'+str(i)))
                    
            if j < len(graph)-1:
                graph_map[cur_key].append((graph[j+1][i], str(j+1)+'_'+str(i)))

    to_be_processed = [(0, start_key)]
    discovered = set()
    mins = {start_key: 0}

    while to_be_processed:
        (total_risk, current) = heappop(to_be_processed)
        if current not in discovered:
            discovered.add(current)
            if current == end_key:
                return total_risk
            
            for risk, neighbor in graph_map.get(current, ()):
                if neighbor not in discovered:
                    neighbor_current_min = mins.get(neighbor, None)
                    neighbor_cost = total_risk + risk
                    if neighbor_current_min is None or neighbor_current_min < neighbor_cost:
                        mins[neighbor] = neighbor_cost
                        heappush(to_be_processed, (neighbor_cost, neighbor))

    
    return mins[end[1]][end[0]]

def expand_tile(tile):
    graph = [[0 for i in range(5*len(tile[0]))] for j in range(5*len(tile))]

    for tile_j in range(5):
        for tile_i in range(5):
            to_add = tile_i + tile_j

            for j in range(len(tile)):
                for i in range(len(tile[j])):
                    graph_j = tile_j * len(tile) + j
                    graph_i = tile_i * len(tile[j]) + i
                    graph[graph_j][graph_i] = tile[j][i] + to_add
                    while graph[graph_j][graph_i] > 9:
                        graph[graph_j][graph_i] -= 9

    return graph

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = input.read().splitlines()

    return [[int(c) for c in l] for l in lines]
