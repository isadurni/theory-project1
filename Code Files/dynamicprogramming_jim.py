#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter
import sys

def gen_solution(jar: List[int], target: int) -> Optional[List[int]]:
    coins = set(jar)
    jar.sort()
    coin_count = Counter(jar)
    table = [None] * (target + 1)
    table[0] = []

    coin_usage = [Counter() for _ in range(target + 1)]

    for i in range(target + 1):
        if table[i] is not None:
            for coin in coins:
                if i + coin <= target:
                    if coin_usage[i][coin] < coin_count[coin]:
                        new_combo = table[i] + [coin]

                        if table[i + coin] is None or len(table[i + coin]) > len(new_combo):
                            table[i + coin] = new_combo
                            coin_usage[i + coin] = coin_usage[i].copy()
                            coin_usage[i + coin][coin] += 1

    return table[-1]

def main():
    target = int(sys.stdin.readline().rstrip())
    jar = [int(n) for n in sys.stdin.readline().rstrip().split(', ')]
    result = gen_solution(jar, target)
    print(f"Target: {target}")
    if result:
        print(f"{result}")
    else:
        print("No possible combination.")
    
if __name__ == '__main__':
    main()
