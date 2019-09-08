# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/itertools-product/problem
# Solve By: itertools.product() ~ Tích

import itertools

if __name__ == '__main__':
    # Input
    listA, listB = list(map(int,input().split())), list(map(int,input().split()))
    # Declare Others Varible

    # Process
    print(set(itertools.product(listA,listB)))
    for i in itertools.product(listA, listB):
        print(i,sep="",end=" ")

