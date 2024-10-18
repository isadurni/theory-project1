#!/usr/bin/env python3

import random

def make_case(min_coins: int, max_coins: int, min_target: int, max_target: int):
    # Randomly generate 4 coin denominations, one small coin between 1 and 3, one medium coin between 4 and 10, ... , one large coin, etc.
    vals = [random.randint(1, 3), random.randint(4, 10), random.randint(11, 25), random.randint(26, 50)]
    
    bag = []
    # For every denomination, generate a random number of coins to add to the bag
    for val in vals:
        bag.append((val, random.randint(min_coins, max_coins)))
    # bag = [(denomination1, number of coins), (denomination2, numebr of coins), ... , (denominationN, number of coins)]
    
    jar = []
    # To 
    for value, count in bag:
        jar.extend([value] * count)
    # jar = [coin1, coin2, coin3, ..., coinN]

    random.shuffle(jar) # shuffle list of coins
    
    return [random.randint(min_target, max_target), jar] # return random target and jar of coins

def main():
    # Generate list of 5 test cases for small medium and large with appropriate parameters for min/max coins and target
    small_cases = [make_case(0, 5, 1, 50) for _ in range(5)]
    med_cases = [make_case(5, 10, 10, 500) for _ in range(5)]
    large_cases =[make_case(10, 20, 100, 1000) for _ in range(5)]

    # Output randomly generated test cases
    print('Small Cases:')
    for case in small_cases:
        print(case)
    print('Medium Cases:')
    for case in med_cases:
        print(case)
    print('Large Cases:')
    for case in large_cases:
        print(case)
    
if __name__ == '__main__':
    main()
