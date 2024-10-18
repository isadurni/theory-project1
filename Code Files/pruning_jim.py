#!/usr/bin/env python3

from typing import List, Generator, Optional
import random
import sys

def gen_subsets(jar: List[int], subset: List[Optional[int]], ind: int, target: int) -> Generator:
    if ind == len(jar):
        if sum(subset) == target:
            yield subset
        return
    
    elif sum(subset) > target:
        return
            
    else:
        yield from gen_subsets(jar, subset, ind + 1, target)
        yield from gen_subsets(jar, subset + [jar[ind]], ind + 1, target)

def main():
    target = int(sys.stdin.readline().rstrip())
    jar = [int(n) for n in sys.stdin.readline().rstrip().split(', ')]
    min_subset = None  # Initialize to None to track the smallest valid subset
    print(f'Target: {target}')
    
    gen = gen_subsets(jar, [], 0, target)
    
    found = False
    for result in gen:
        found = True
        if min_subset is None or len(result) < len(min_subset):
            min_subset = result  # Keep track of the smallest valid subset
    
    if not found:
        print('No possible combination.')
    else:
        print(min_subset)
    
if __name__ == '__main__':
    main()
