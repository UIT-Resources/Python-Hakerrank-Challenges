# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Solve By: .update() or |=, .intersection_update() or &=, .difference_update() or -=,
# .symmetric_difference_update() or ^=

if __name__ == '__main__':
    # Input
    nOriItem = int(input()) ; oriItemSet = set(map(int,input().split()))
    nQuery = int(input()) ;
    # Declare Others Variable

    # Process
    for i in range(nQuery):
        query = input()
        itemQuerySet = set(map(int, input().split()))
        if query.split()[0] == "update":
            oriItemSet.update(itemQuerySet)
        elif query.split()[0] == "intersection_update":
            oriItemSet.intersection_update(itemQuerySet)
        elif query.split()[0] == "difference_update":
            oriItemSet.difference_update(itemQuerySet)
        elif query.split()[0] == "symmetric_difference_update":
            oriItemSet.symmetric_difference_update(itemQuerySet)
        else:
            print("ERROR : Invalid query")
    print(sum(oriItemSet))