# Link : https://www.hackerrank.com/challenges/the-minion-game/problem
# Medium Challenge
# Solve by :
# + Count the score by Rule not by create group then count them --> So slow

import re
import time

def minion_game(string):
    string=string.upper()
    kevinScore=evaluateScore(string,findVowelIndex(string))
    stuartScore=evaluateScore(string,findConsonantIndex(string))
    if kevinScore > stuartScore :
        print('Kevin',kevinScore)
    elif kevinScore < stuartScore :
        print('Stuart',stuartScore)
    else :
        print('Draw')

# Return list index of vowel in string , except duplicate index, vowel : aeiou
def findVowelIndex(string):
    start=time.time()
    result=[]
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            result.append(i)
    end=time.time()
    # print("Find vowel index - Execute time : "+str(end-start))
    return result

# Return list index of Consonant in string , except duplicate index
def findConsonantIndex(string) :
    start = time.time()
    result = []
    for i in range(len(string)):
        if string[i] not in ['A','E','I','O','U']:
            result.append(i)
    end = time.time()
    # print("Find consonant index - Execute time : " + str(end - start))
    return result

# Evaluate score base on index list, Return score
def evaluateScore(string, indexList):
    start=time.time()
    # Create Words
    # wordSet=set()
    # # # Method 1
    # # for i in indexList:
    # #     wordSet.append(set(string[i:j+1] for j in range(i,len(string))))
    # # print(wordSet,type(wordSet))
    #
    # # Method 2
    # for i in range(indexList[0], len(string)):
    #     wordSet.add(string[indexList[0]:i + 1])
    #     for j in indexList[1:]:
    #         if (i >= j):
    #             wordSet.add(string[j:i + 1])
    #
    # Get Score
    score=0
    # Use follow code for Method 1 & 2
    # for i in wordSet:
    #     match = re.findall('(?='+i+')',string)
    #     score +=len(match)

    # Method 3 : Focus Decrease Excute Time .
    for i in indexList:
        score+=len(string)-i

    end = time.time()
    # print("Evaluate Score - Execute time : " + str(end - start))
    return score


if __name__ == '__main__':
    s = input()
    start = time.time()
    minion_game(s)
    end = time.time()
    excuteTime = end-start
    # print('Excute tim    for i in indexList:
    #         score+=len(string)-i
    #
    #     end = time.time()
    #     print("Evaluate Score - Execute time : " + str(end - start))
    #     return scoree : '+str(excuteTime)+'s')