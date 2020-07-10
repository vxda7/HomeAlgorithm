def solution(s):
    lens = len(s)
    if lens == 4 or lens == 6:
        try:
            int(s)
            return True
        except:
            return False
    return False


print(solution('a234'))
