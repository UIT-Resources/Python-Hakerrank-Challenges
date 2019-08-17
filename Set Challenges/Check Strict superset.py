# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Solve By: .issubset() or <= and len()

if __name__ == '__main__':
    # Input
    setA = set(map(int, input().split()))
    n = int(input())
    flag = True
    for i in range(n):
        otherSet = set(map(int, input().split()))
        if otherSet.issubset(setA) is False or len(setA) <= len(otherSet):
            flag = False
            break
    print(flag)
