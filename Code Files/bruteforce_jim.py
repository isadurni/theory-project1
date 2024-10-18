#!/usr/bin/env python3

from typing import List, Generator, Optional
import sys

# Generates subsets of 'jar' and checks if their sum equals the target
def gen_subsets(jar: List[int], subset: List[Optional[int]], ind: int, target: int) -> Generator:
    # Base case
    if ind == len(jar):
        if sum(subset) == target:
            yield subset
        return
            
    else:
        # Recursive call
        yield from gen_subsets(jar, subset, ind+1, target)
        # Recursive call with current element included
        yield from gen_subsets(jar, subset + [jar[ind]], ind+1, target)

def main():
    # Read from input
    target = int(sys.stdin.readline().rstrip())
    jar = [int(n) for n in sys.stdin.readline().rstrip().split(', ')]
    min_subset = None
    print(f'Target: {target}')
    gen = gen_subsets(jar, [], 0, target)

    # Flag to check if any coin combination has been found
    found = False  
    # Loop through each subset
    for result in gen:
        found = True
        # Update if it' the first combination or smaller than the previous combination
        if min_subset is None or len(result) < len(min_subset):
            min_subset = result
    
    if not found:
        print('No possible combination.')
    else:
        print(min_subset)
    
if __name__ == '__main__':
    main()
