# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-set-union/problem?h_r=next-challenge&h_v=zen
# Solve By: .union()

if __name__ == '__main__':
    # Input
    E = int(input()) ; eSet = set(map(int,input().split()))
    F = int(input()) ; fSet = set(map(int,input().split()))

    # Process
    e_fSet = eSet.union(fSet)

    # Output
    print(len(e_fSet))
