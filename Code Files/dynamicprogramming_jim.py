#!/usr/bin/env python3

from typing import List, Optional
from collections import Counter
import sys

#dynamic programming function that returns the set with the least amount of coins needed to reach the goal
def gen_solution(jar: List[int], target: int) -> Optional[List[int]]:
    #generate coins to remove duplacites in the jar and sort it
    coins = set(jar)
    jar.sort()
    coin_count = Counter(jar)
    #create empty table the size of target used to store values
    table = [None] * (target + 1)
    table[0] = []

    coin_usage = [Counter() for _ in range(target + 1)]

    #loop to iterate through each index of the table
    for i in range(target + 1):
        if table[i] is not None:
            #add coins to the index
            for coin in coins:
                if i + coin <= target:
                    if coin_usage[i][coin] < coin_count[coin]:
                        new_combo = table[i] + [coin]

                        if table[i + coin] is None or len(table[i + coin]) > len(new_combo):
                            table[i + coin] = new_combo
                            coin_usage[i + coin] = coin_usage[i].copy()
                            coin_usage[i + coin][coin] += 1

    #return last element of the table which contains the list to generate the target, returns None if not possible
    return table[-1]

def main():
    #parse input
    target = int(sys.stdin.readline().rstrip())
    jar = [int(n) for n in sys.stdin.readline().rstrip().split(', ')]
    #get result from function
    result = gen_solution(jar, target)
    print(f"Target: {target}")
    #check if result exists and prints it
    if result:
        print(f"{result}")
    else:
        print("No possible combination.")
    
if __name__ == '__main__':
    main()
