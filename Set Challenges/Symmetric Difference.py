# Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
# Solve by : .intersection(), .union(), difference() or ^ operator


if __name__ == '__main__':
    # Input
    N = int(input())
    N_list = set(map(int,input().split()))
    M = int(input())
    M_list = set(map(int,input().split()))
    # Process
    result_list = (list(N_list ^ M_list))
    result_list.sort()
    # Output
    for i in result_list:
        print(i)

