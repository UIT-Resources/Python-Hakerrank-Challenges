# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/polar-coordinates/problem
# Solve By: cmath.phase(complex)

import time
import math
import cmath

if __name__ == '__main__':
    # Input
    cp = complex(input())
    # Declare Others Varible

    # Process
    r = math.sqrt(math.pow(cp.real,2)+math.pow(cp.imag,2))
    angel = cmath.phase(cp)

    # Output
    print(r,angel,sep="\n")