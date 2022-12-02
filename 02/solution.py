#!/usr/bin/env python3

def get_input():
    with open('input.txt') as file:
        return [line.replace(" ", "") for line in file.read().strip().split("\n")]

def first_game():
    STRATEGY = {
        'AX': 4, 'AY': 8, 'AZ': 3,
        'BX': 1, 'BY': 5, 'BZ': 9,
        'CX': 7, 'CY': 2, 'CZ': 6
    }

    total_score = 0
    for round in rounds:
        total_score += STRATEGY[round]

    return total_score

def second_game():
    STRATEGY = {
        'AX': 3, 'AY': 4, 'AZ': 8,
        'BX': 1, 'BY': 5, 'BZ': 9,
        'CX': 2, 'CY': 6, 'CZ': 7
    }

    total_score = 0
    for round in rounds:
        total_score += STRATEGY[round]

    return total_score

if __name__ == "__main__":
    rounds = get_input()
    print("Total score: ", first_game())
    print("Total score: ", second_game())
