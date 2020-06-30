def solution(numbers, hand):
    answer = ''
    rctonum = {"*":[0, 0], "#": [2, 0], 1:[0, 3], 2:[1, 3], 3: [2, 3], 4: [0, 2], 5: [1, 2], 6: [2, 2], 7:[0, 1], 8: [1, 1], 9:[2, 1], 0:[1, 0]}
    nowleft = [0, 0]
    nowright = [2, 0]
    leftdis, rightdis = 0, 0
    for one in numbers:
        if one == 1 or one == 4 or one == 7:
            answer += "L"
            nowleft = rctonum[one]
        elif one == 3 or one == 6 or one == 9:
            answer += "R"
            nowright = rctonum[one]
        else:   # 2, 5, 8, 0 일 때
            leftdis = abs(rctonum[one][0] - nowleft[0]) + abs(rctonum[one][1] - nowleft[1])
            rightdis = abs(rctonum[one][0] - nowright[0]) + abs(rctonum[one][1] - nowright[1])

            if leftdis == rightdis:
                if hand == "right":
                    answer += "R"
                    nowright = rctonum[one]
                else:
                    answer += "L"
                    nowleft = rctonum[one]
            elif leftdis > rightdis:
                answer += "R"
                nowright = rctonum[one]
            elif leftdis < rightdis:
                answer += "L"
                nowleft = rctonum[one]
    return answer


a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(a)