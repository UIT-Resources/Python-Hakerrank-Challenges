# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/compress-the-string/problem?h_r=next-challenge&h_v=zen
# Solve By: 

from itertools import *

if __name__ == '__main__':
    # Input
    s = input()

    # Process
    for k, g in groupby(s):
        print('(' +str(len(list(g)))+', '+str(k)+')',end=" ")
