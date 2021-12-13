# https://adventofcode.com/2021/day/13
# https://adventofcode.com/2021/day/13#part2

import os
import pprint
pp = pprint.PrettyPrinter(indent=4)


def solve_part_one(file='../solutions/inputs/13.in'):
    instructions = load_file(file)

    max_x = 1 + max([p[0] for p in instructions['points']])
    max_y = 1 + max([p[1] for p in instructions['points']])

    paper = [[False for i in range(max_x)] for j in range(max_y)]

    for p in instructions['points']:
        paper[p[1]][p[0]] = True

    for f in instructions['folds'][0:1]:
        axis = f[0]
        axis_val = int(f.split('=')[1])
        
        if axis == 'x':
            new_paper = [[paper[j][i] for i in range(axis_val)] for j in range(len(paper))]
            max_iter_x = len(paper[0]) - axis_val - 1
            
            for i in range(max_iter_x):
                for j in range(len(paper)):
                    new_paper[j][axis_val - i - 1] = new_paper[j][axis_val - i - 1] or paper[j][axis_val + i + 1]

        else:
            new_paper = [[paper[j][i] for i in range(len(paper[j]))] for j in range(axis_val)]
            max_iter_y = len(paper) - axis_val - 1

            for i in range(len(paper[0])):
                for j in range(max_iter_y):
                    new_paper[axis_val - j - 1][i] = new_paper[axis_val - j - 1][i] or paper[axis_val + j + 1][i]

        paper = new_paper
    
    return sum([l.count(True) for l in paper])

def solve_part_two(file='../solutions/inputs/13.in'):
    instructions = load_file(file)

    max_x = 1 + max([p[0] for p in instructions['points']])
    max_y = 1 + max([p[1] for p in instructions['points']])

    paper = [[False for i in range(max_x)] for j in range(max_y)]

    for p in instructions['points']:
        paper[p[1]][p[0]] = True

    for f in instructions['folds']:
        axis = f[0]
        axis_val = int(f.split('=')[1])
        
        if axis == 'x':
            new_paper = [[paper[j][i] for i in range(axis_val)] for j in range(len(paper))]
            max_iter_x = len(paper[0]) - axis_val - 1
            
            for i in range(max_iter_x):
                for j in range(len(paper)):
                    new_paper[j][axis_val - i - 1] = new_paper[j][axis_val - i - 1] or paper[j][axis_val + i + 1]

        else:
            new_paper = [[paper[j][i] for i in range(len(paper[j]))] for j in range(axis_val)]
            max_iter_y = len(paper) - axis_val - 1

            for i in range(len(paper[0])):
                for j in range(max_iter_y):
                    new_paper[axis_val - j - 1][i] = new_paper[axis_val - j - 1][i] or paper[axis_val + j + 1][i]

        paper = new_paper
    
    for c in paper:
        print(''.join(['#' if r else '.' for r in c]))
    return 0

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')
    lines = input.read().splitlines()

    empty_line_i = lines.index('')
    points = lines[:empty_line_i]
    folds = lines[empty_line_i+1:]

    return {'points': [(int(l.split(',')[0]), int(l.split(',')[1])) for l in points], 'folds': [l.split()[-1] for l in folds]}
