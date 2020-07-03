import math
import time


def solution(w, h):
    answer = w*h
    white = 0
    inclination = w/h
    if w == 1 or h == 1:
        return 0
    for y in range(h):
        up_x = int(inclination * y)
        down_x = math.ceil(inclination * (y + 1))
        white += down_x - up_x
        if up_x == down_x:
            white = white * (h//y)
            break

    return answer - white


start = time.time()
print(solution(2, 100000000))

print(time.time() - start)
# print(int(3.999999999999999999999999999999))
