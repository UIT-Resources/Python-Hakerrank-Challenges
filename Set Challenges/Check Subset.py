# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-check-subset/problem
# Solve By: .issubset() or <=
import time

if __name__ == '__main__':
    # Input & Process
    nTestCase = int(input())
    for i in range(nTestCase):
        nA, setA = int(input()),set(map(int,input().split()))
        nB, setB = int(input()),set(map(int,input().split()))
        print(setA<=(setB))