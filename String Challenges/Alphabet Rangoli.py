# Link : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Solve by :
# + stringVariable.center(width,fillchar)
# + stringVariable.reverse() ~ stringVariable[::-1]

def print_rangoli(size):
    # ---------------------------METHOD 1---------------------------------------
    width = (size * 2 - 1)*2 - 1
    lastLetter = 97 + size - 1
    # Paint Top & Belt
    # for i in range(1, size+1):  # size-1 = number of top row
    #     rowData = []
    #     for j in range(i):  # add letters of row in array
    #         rowData.append(chr(lastLetter - j))
    #     if (len(rowData) > 1):
    #         tempList=rowData[0:len(rowData) - 1];
    #         tempList.reverse()
    #         rowData.extend(tempList)
    #     # Create Actual Row Format
    #     tempString = "-".join(rowData)
    #     row = tempString.center(width,'-')
    #     print(row)
    #
    # # Paint Bottom
    # for i in range(1, size):  # size-1 = number of top row
    #     rowData = []
    #     for j in range(size-i):  # add letters of row in array
    #         rowData.append(chr(lastLetter - j))
    #     if (len(rowData) > 1):
    #         tempList=rowData[0:len(rowData) - 1];
    #         tempList.reverse()
    #         rowData.extend(tempList)
    #     # Create Actual Row Format
    #     tempString = "-".join(rowData)
    #     row = tempString.center(width,'-')
    #     print(row)
    # -----------------------------METHOD 2------------------------------------
    for i in range(size):
        s = "-".join(chr(ord('a')+size-1-j) for j in range(i+1))
        print((s + s[::-1][1:]).center((size*2-1)*2-1,"-"))
    for i in range(size-1):
        s = "-".join(chr(ord('a')+size-1-j) for j in range(size-1-i))
        print((s + s[::-1][1:]).center((size * 2 - 1) * 2 - 1, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)