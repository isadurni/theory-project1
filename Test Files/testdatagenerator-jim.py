#!/usr/bin/env python3

import random

def make_case(min_coins: int, max_coins: int, min_target: int, max_target: int):
    vals = [random.randint(1, 3), random.randint(4, 10), random.randint(11, 25), random.randint(26, 50)]
    
    bag = []
    for val in vals:
        bag.append((val, random.randint(min_coins, max_coins)))

    jar = []

    for value, count in bag:
        jar.extend([value] * count)

    random.shuffle(jar)
    
    return [random.randint(min_target, max_target), jar]

def main():
    small_cases = [make_case(0, 5, 1, 50) for _ in range(5)]
    med_cases = [make_case(5, 10, 10, 500) for _ in range(5)]
    large_cases =[make_case(10, 20, 100, 1000) for _ in range(5)]
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
