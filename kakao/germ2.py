def solution(gems):
    setgems = set(gems)
    numofgems = len(setgems)
    if len(gems) == numofgems:
        return [1, numofgems]
    getgems = []
    sindex = 0
    howlong = numofgems
    while True:
        getgems = gems[sindex:sindex + howlong]

        if set(getgems) == setgems:
            return [sindex + 1, sindex + howlong]
        else:
            sindex += 1
            if sindex - 1 + howlong == numofgems:
                sindex = 0
                howlong += 1
                if numofgems == howlong:
                    return [1, numofgems]


a = solution(["XYZ", "XYZ", "XYZ"])
print(a)