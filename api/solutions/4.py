# https://adventofcode.com/2021/day/4
# https://adventofcode.com/2021/day/4#part2

import os
import pprint
pp = pprint.PrettyPrinter(indent=4)


def solve_part_one(file='../solutions/inputs/4.in'):
    game = load_file(file)
    winning_score = 0

    for num in game['called_numbers']:
        for i in range(len(game['cards'])):
            game['cards'][i] = [[-1 if c == num else c for c in r] for r in game['cards'][i]]
            if is_card_winner(game['cards'][i]):
                return num * sum([sum([c if c > 0 else 0 for c in r]) for r in game['cards'][i]])
        
    return 0

def solve_part_two(file='../solutions/inputs/4.in'):
    game = load_file(file)
    winning_score = 0

    for num in game['called_numbers']:
        winning_cards = []
        for i in range(len(game['cards'])):
            game['cards'][i] = [[-1 if c == num else c for c in r] for r in game['cards'][i]]
            if is_card_winner(game['cards'][i]):
                winning_cards.insert(0, i)                
        
        for w_card_i in winning_cards:
            if w_card_i == 0 and len(game['cards']) == 1:
                winning_score = num * sum([sum([c if c > 0 else 0 for c in r]) for r in game['cards'][0]])
                return winning_score
            else:
                game['cards'].pop(w_card_i)

    return 0

def load_file(file):
    fn = os.path.join(os.path.dirname(__file__), file)
    input = open(fn, 'r')

    lines = input.read().splitlines()
    called_numbers = [int(cn) for cn in lines.pop(0).split(',')]
    cards = []

    while len(lines) > 0:
        lines.pop(0)
        card = []
        for i in range(5):
            card.append([int(x) for x in lines.pop(0).split()])

        cards.append(card)


    return {'cards': cards, 'called_numbers': called_numbers}

def is_card_winner(card):
    is_winner = False
    
    # Check Columns
    transposed_card = map(list, zip(*card))
    is_winner = any([sum(r) == -5 for r in transposed_card])

    # Check Rows
    is_winner = is_winner or any([sum(r) == -5 for r in card])
    return is_winner