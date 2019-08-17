# Link : https://www.hackerrank.com/challenges/string-validators/problem
# Solve by : strVar.isalnum() ; .isalpha() ; .isdigit() ; .islower() ; .isupper()

if __name__ == '__main__':
    s = input()
    hasAnyAlnum = False
    hasAnyAlpha = False
    hasAnyDigit = False
    if (s.isalnum()):
        hasAnyAlnum = True
        if (s.isdigit() == False):
            hasAnyAlpha = True
        else:
            hasAnyAlpha = False

        if (s.isalpha() == False):
            hasAnyDigit = True
        else:
            hasAnyDigit = False
    else:
        temp = s.upper()  # Tranfer to all upper case
        for i in range(65, 91):  # A->Z
            if (temp.find(chr(i)) != -1):
                hasAnyAlnum = True
                hasAnyAlpha = True
                break
        for i in range(48, 58):  # 0 -> 9
            if (temp.find(chr(i)) != -1):
                hasAnyAlnum = True
                hasAnyDigit = True
                break
    print(hasAnyAlnum)
    print(hasAnyAlpha)
    print(hasAnyDigit)

    if (hasAnyAlpha):
        if (s.isupper() == False):
            print("True")
        else:
            print("False")

        if (s.islower() == False):
            print("True")
        else:
            print("False")
    else:

        print("False")
        print("False")

