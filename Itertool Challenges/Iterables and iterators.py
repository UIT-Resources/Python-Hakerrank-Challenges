# Github: https://github.com/UIT-Resources/Python-Hakerrank-Challenges
# Author: DNT - Doãn Ngọc Tài
# Link Challenge: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Solve By: itertools.combination(), itertools.groupby()
# Formula :
# - Total combination : C1 = kCn = n! / k!(n-k)!
# - Number of combination (Don't has any 'a') : C2 = kC(n-Na) = (n-Na)!/ k!(n-Na-k)!
# - Number of combination (Ha at least one character 'a') :  Result = C1 - C2
# - Probability = Result = (C1 - C2) / C1

import itertools
import math

if __name__ == '__main__':
    # Input
    N = int(input());
    arr = input().split();
    K = int(input())
    # Process
    Na = arr.count('a')
    result = 0
    # Special Situations : Na = 0 ; N = K
    if Na == 0:
        result = 0
    else:
        if N == K:
            result = 1
        else:
            C1 = math.factorial(N) / (math.factorial(K) * math.factorial(N - K))
            C2 = math.factorial(N - Na) / (math.factorial(K) * math.factorial(N - Na - K))
            result = round((C1 - C2) / C1, 3)
    print(result)
