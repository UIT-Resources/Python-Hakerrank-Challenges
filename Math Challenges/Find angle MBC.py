# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/find-angle/problem
# Solve By:
# Formula : angle(MBC) = angle(MCB) = arc tan(AB/BC)
# math.atan2(AB,BC) or math.atan(AB/BC) ; math.degrees(radian) ;
# Note : round() NOT math.round()

import math

if __name__ == '__main__':
    # Input
    AB,BC = int(input()),int(input())

    # Process
    print(str(round(math.degrees(math.atan(AB/BC))))+'°')