#!/usr/bin/env python3

from typing import List, Generator, Optional
import random

coins = [1, 5, 10, 25]

#dynamic programming
def gen_solution(jar: List[int], target: int) -> Generator:
    jar.sort()
    table = [[n for n in range(len(jar))]] * target
    table[0] = [1]
    for i in range(target-1):
        for coin in coins:
            if i+coin < target:
                if (len(table[i])+coin) < len(table[i+coin]):
                    table[i+coin] = table[i] + [coin]
    return table[-1]

def main():
    jar = [
    5, 10, 1, 25, 5, 10, 1, 1, 25, 10,
    5, 25, 10, 5, 1, 25, 1, 10, 5, 25,
    10, 1, 5, 25, 10, 1, 5, 10, 25, 1,
    5, 10, 25, 5, 1, 10, 25, 1, 5, 10,
    25, 1, 25, 10, 5, 1, 25, 10, 5, 1
    ]
    print(gen_solution(jar, 27))
    
if __name__ == '__main__':
    main()
