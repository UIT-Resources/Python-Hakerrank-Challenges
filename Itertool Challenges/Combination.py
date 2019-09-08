# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/itertools-combinations/problem?h_r=next-challenge&h_v=zen
# Solve By: itertools.combinations() ~ Tổ hợp

from itertools import *

if __name__ == '__main__':
    # Input
    s,k = input().split()

    # Process
    for k in range(1,int(k)+1):
        for i in combinations(sorted(s),k):
            print("".join(i))