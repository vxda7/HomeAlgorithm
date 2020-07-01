def solution(gems):
    setgems = set(gems)
    numofgems = len(setgems)
    if len(gems) == numofgems:
        return [1, numofgems]
    getgems = []
    sindex = 0
    howlong = numofgems
    # index = 0
    while True:
        getgems = gems[sindex:sindex + howlong]
        # print(getgems)
        # if index == 10:
        #     break
        if set(getgems) == setgems:
            # print(gems[sindex: sindex + howlong])
            return [sindex + 1, sindex + howlong]
        else:
            sindex += 1
            if sindex - 1 + howlong == numofgems:
                sindex = 0
                howlong += 1
                if numofgems == howlong:
                    return [1, numofgems]
        # index += 1


# def solution(gems):
#     setgems = set(gems)
#     numofgems = len(setgems)

#     sindex = 0
#     eindex = len(gems)


#     while True:
#         # 뒤에서부터 간격을 줄이기
#         if set(gems[sindex: eindex - 1]) == setgems:
#             eindex -= 1
#             print(eindex, "e")
#         else:
#             break

#     while True:
#         # 앞에서부터 간격을 줄이기
#         if set(gems[sindex + 1:eindex]) == setgems:
#             sindex += 1
#             print(sindex, "s")
#         else:
#             break

#     return [sindex + 1, eindex]

a = solution(["XYZ", "XYZ", "XYZ"])
print(a)