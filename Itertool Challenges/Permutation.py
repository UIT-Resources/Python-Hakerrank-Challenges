# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/itertools-permutations/problem
# Solve By: itertools.permutations() ~ Chỉnh hợp

import itertools

if __name__ == '__main__':
    # Input
    s,k = input().split()

    # Process
    for i in itertools.permutations(sorted(s),int(k)):
        print("".join(i))