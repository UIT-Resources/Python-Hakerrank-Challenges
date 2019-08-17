# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Solve By: symmetric_difference()

if __name__ == '__main__':
    # Input
    E = int(input());
    eSet = set(map(int, input().split()))
    F = int(input());
    fSet = set(map(int, input().split()))

    # Process
    e_fSet = eSet.symmetric_difference(fSet)

    # Output
    print(len(e_fSet))