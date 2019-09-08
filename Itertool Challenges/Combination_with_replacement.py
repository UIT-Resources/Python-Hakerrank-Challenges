# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# Solve By: itertools.combination_with_replacement() ~ Tổ hợp lặp

import itertools as iter

if __name__ == '__main__':
    # Input
    s,k = input().split()

    # Process
    for i in iter.combinations_with_replacement(sorted(s),int(k)):
        print("".join(i))