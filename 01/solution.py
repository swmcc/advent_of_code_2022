#!/usr/bin/env python3

def most_calories():
    return max(TTL_CALORIES)


def total_top_three_calories():
    return sum(TTL_CALORIES[:3])


if __name__ == "__main__":
    TTL_CALORIES = sorted([sum(list(map(int, bp.splitlines()))) for bp in open('input.txt').read().split('\n\n')], reverse=1)
    print("Most calories an elf is carrying: %d" % most_calories())
    print("Top three calories together total: %d" % total_top_three_calories())
