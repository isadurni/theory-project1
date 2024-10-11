#!/usr/bin/env python3

from typing import List, Generator, Optional
import random

#pruning
def gen_subsets(jar: List[int], subset: List[Optional[int]], ind: int, target: int) -> Generator:
    if ind == len(jar):
        if sum(subset) == target:
            yield subset
        return
    
    elif sum(subset) > target:
        return
            
    else:
        yield from gen_subsets(jar, subset, ind+1, target)
        yield from gen_subsets(jar, subset + [jar[ind]], ind+1, target)

def main():
    jar = [
    5, 10, 1, 25, 5, 10, 1, 1, 25, 10,
    5, 25, 10, 5, 1, 25, 1, 10, 5, 25,
    10, 1, 5, 25, 10, 1, 5, 10, 25, 1,
    5, 10, 25, 5, 1, 10, 25, 1, 5, 10,
    25, 1, 25, 10, 5, 1, 25, 10, 5, 1
    ]
    min = jar
    for result in gen_subsets(jar, [], 0, 27):
        if len(result) < len(min):
            min = result
    print(min)
    
if __name__ == '__main__':
    main()
