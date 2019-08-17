# Link : https://www.hackerrank.com/challenges/text-wrap/problem
# Solve by :
# + Library : textwrap - method : textwrap.wrap(string,max_width) or textwrap.fill(string,max_width)

import textwrap

def wrap(string, max_width):
    wrapped_str = textwrap.wrap(string,max_width)
    return "\n".join(wrapped_str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)