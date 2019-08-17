# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Solve by : .remove(), .discard(),.pop(), .sum()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command=input()
    if command.split()[0] == "pop":
        s.pop()
        continue
    if command.split()[0] == "discard":
        s.discard(int(command.split()[1]))
        continue
    if command.split()[0] == "remove":
        s.remove(int(command.split()[1]))
# Output
print(sum(s))
