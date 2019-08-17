# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge:https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen
# Solve By: .intersection()

if __name__ == '__main__':
    # Input
    E = int(input());
    eSet = set(map(int, input().split()))
    F = int(input());
    fSet = set(map(int, input().split()))

    # Process
    e_fSet = eSet.intersection(fSet)

    # Output
    print(len(e_fSet))