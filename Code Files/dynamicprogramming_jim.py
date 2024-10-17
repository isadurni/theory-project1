#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter
import sys

# Dynamic programming solution
def gen_solution(jar: List[int], target: int) -> Optional[List[int]]:
    coins = set(jar)
    jar.sort()
    coin_count = Counter(jar)  # Keeps track of available coins
    table = [None] * (target + 1)
    table[0] = []

    # We use a separate coin count for each table entry to track usage
    coin_usage = [Counter() for _ in range(target + 1)]

    for i in range(target + 1):
        if table[i] is not None:  # If we can make value `i`
            for coin in coins:
                if i + coin <= target:  # Check within bounds
                    if coin_usage[i][coin] < coin_count[coin]:  # Check if we have enough of this coin
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
        print("No solution found with available coins.")
    
if __name__ == '__main__':
    main()
