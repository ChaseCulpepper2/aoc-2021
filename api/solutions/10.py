# https://adventofcode.com/2021/day/10
# https://adventofcode.com/2021/day/10#part2

import os

def solve_part_one(file='../solutions/inputs/10.in'):
    lines = load_file(file)

    close_to_opening = { ')': '(', ']': '[', '}': '{', '>': '<' }
    offenders = []
    offenders_to_score = { ')': 3, ']': 57, '}': 1197, '>': 25137 }

    for line in lines:
        stack = []
        for c in line:
            if c in '({<[':
                stack.append(c)
            else:
                opening = stack.pop()
                if opening != close_to_opening[c]:
                    offenders.append(c)
    return sum([offenders_to_score[o] for o in offenders])

def solve_part_two(file='../solutions/inputs/10.in'):
    lines = load_file(file)

    close_to_opening = { ')': '(', ']': '[', '}': '{', '>': '<' }
    scores = []
    completion_to_score = { '(': 1, '[': 2, '{': 3, '<': 4 }

    for line in lines:
        stack = []
        has_error = False
        for c in line:
            if c in '({<[':
                stack.append(c)
            else:
                opening = stack.pop()
                if opening != close_to_opening[c]:
                    has_error = True
        if not has_error:
            score = 0
            while len(stack) > 0:
                missing = stack.pop()
                score *= 5
                score += completion_to_score[missing]
            scores.append(score)

    return sorted(scores)[int(len(scores)/2):-int(len(scores)/2)][0]

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    return input.read().splitlines()
