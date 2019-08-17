# Link : https://www.hackerrank.com/challenges/merge-the-tools/problem
# Solve by : not in

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s = ""
        for j in range(i,i+k):
            if (j%k==0) :
                s=string[j]
            else:
                if string[j] not in s:
                    s+=string[j]
        print(s)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)