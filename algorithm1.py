#!/usr/bin/env python3

from typing import List, Generator, Optional


def gen_subsets(jar: List[int], subset: List[Optional[int]], ind: int, target: int) -> Generator:
    if ind == len(jar):
        if sum(subset) == target:
            yield subset
        return
            
    else:
        yield from gen_subsets(jar, subset, ind+1, target)
        yield from gen_subsets(jar, subset + [jar[ind]], ind+1, target)

def main():
    jar = ([1] * 5) + ([5] * 3) + ([10] * 4) + ([25] * 2)
    min = jar
    for result in gen_subsets(jar, [], 0, 27):
        if len(result) < len(min):
            min = result
    print(min)
    
if __name__ == '__main__':
    main()
