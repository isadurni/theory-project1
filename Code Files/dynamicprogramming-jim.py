#!/usr/bin/env python3

from typing import List
from collections import Counter

coins = [1, 5, 10, 25]

# Dynamic programming solution
def gen_solution(jar: List[int], target: int) -> List[int]:
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

    return table[target] if table[target] is not None else []

def main():
    jar = [
        5, 10, 1, 25, 5, 10, 1, 1, 25, 10,
        5, 25, 10, 5, 1, 25, 1, 10, 5, 25,
        10, 1, 5, 25, 10, 1, 5, 10, 25, 1,
        5, 10, 25, 5, 1, 10, 25, 1, 5, 10,
        25, 1, 25, 10, 5, 1, 25, 10, 5, 1
    ]
    jar = [1, 1, 10, 5, 10]  # Provided jar that should make 27
    result = gen_solution(jar, 27)
    if result:
        print(f"Solution found: {result}")
    else:
        print("No solution found with available coins.")
    
if __name__ == '__main__':
    main()
