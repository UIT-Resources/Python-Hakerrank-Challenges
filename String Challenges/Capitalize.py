# Link : https://www.hackerrank.com/challenges/capitalize/problem
# Solve by : strVar.capitalize() ; strVar.split()
# Note : capitalize() different with title()
# + Ex : '3g'.capitalize() -> '3g' different with '3g'.title() -> '3G'

def solve(s):
    return " ".join(i.capitalize() for i in (s.split(" ")))

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result + '\n')
