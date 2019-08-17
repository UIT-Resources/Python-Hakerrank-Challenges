# Link: https://www.hackerrank.com/challenges/no-idea/problem?h_r=next-challenge&h_v=zen
# Solve by: .difference()

if __name__ == '__main__':
    # Input
    N,M = map(int,input().split())
    n = map(int,input().split()) ; A = set(map(int,input().split())) ; B = set(map(int,input().split()))
    # Process
    A_Diff = A.difference(B)
    B_Diff = B.difference(A)
    happiness = 0
    for i in n:
        if i in A_Diff:
            happiness+=1
            continue
        if i in B_Diff:
            happiness-=1
    # Output
    print(happiness)