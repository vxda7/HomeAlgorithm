from itertools import permutations
from collections import deque

def solution(expression):
    operator, number = deque(), deque()
    for e in expression:
        if e in ['+', '-', '*']:
            operator.append(e)

    tempnum, extemp = 0, expression
    while tempnum < len(extemp):
        if extemp[tempnum] in ['+', '-', '*']:
            number.append(int(extemp[:tempnum]))
            extemp = extemp[tempnum + 1:]
            tempnum = 0
        else:
            tempnum += 1
    number.append(int(extemp))

    ans, ranks = 0, list(permutations(set(operator)))
    for rank in ranks:
        op, num = operator.copy(), number.copy()
        for r in rank:
            j = 0
            while j < len(op):
                if op[j] == r:
                    del op[j]
                    if r == '+':
                        num[j] = num[j] + num[j + 1]
                    elif r == '-':
                        num[j] = num[j] - num[j + 1]
                    else:
                        num[j] = num[j] * num[j + 1]
                    del num[j + 1]
                    j = 0
                else:
                    j += 1
        ans = max(ans, abs(num[0]))
    return ans