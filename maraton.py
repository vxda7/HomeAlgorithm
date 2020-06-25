def count(getlist, start):
    temp = start
    for one in getlist:
        try:
            temp[one] += 1
        except:
            temp[one] = 0
    return temp


def solution(participant, completion):
    answer = ''
    diction = count(participant, {})
    diction = count(completion, diction)
    for one in diction.items():
        if one[1] % 2 == 0:
            return one[0]
