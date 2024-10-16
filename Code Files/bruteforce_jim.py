#!/usr/bin/env python3

from typing import List, Generator, Optional
import sys

def gen_subsets(jar: List[int], subset: List[Optional[int]], ind: int, target: int) -> Generator:
    if ind == len(jar):
        if sum(subset) == target:
            yield subset
        return
            
    else:
        yield from gen_subsets(jar, subset, ind+1, target)
        yield from gen_subsets(jar, subset + [jar[ind]], ind+1, target)

def main():
    target = int(sys.stdin.readline().rstrip())
    jar = [int(n) for n in sys.stdin.readline().rstrip().split(', ')]
    min = jar
    print(f'Target: {target}')
    gen = gen_subsets(jar, [], 0, target)
    
    if not gen:
        print('No possible combination.')
    else:
        for result in gen:
            if len(result) < len(min):
                min = result
        print(min)
    
if __name__ == '__main__':
    main()
