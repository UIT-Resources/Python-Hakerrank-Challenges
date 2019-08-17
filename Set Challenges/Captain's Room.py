# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Solve By: Formula
# -> Captain's Room = (Sum(roomNumList)-K.Sum(roomNumSet)) // (1-k)

import time

if __name__ == '__main__':

    # ----------- Main Code Here ---------------
    # Input
    N = int(input())
    roomNumList = list(map(int, input().split()))
    # --------- Measure execution time -----------
    startTime = time.time()
    print("Program's running")

    # Process
    roomNumSet = set(roomNumList)
    print("%d"%((sum(roomNumList)-N*sum(roomNumSet)) // (1-N)))

    # --------- Measure execute time -----------
    endTime = time.time()
    print("Exexute time: %.3f (seconds)" % (endTime - startTime))
