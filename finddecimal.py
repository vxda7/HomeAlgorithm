def solution(n):
    decimal = [False, False] + [True] * (n - 1)
    for i in range(2, n+1):
        cnt = 0
        if decimal[i] == True:
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1:
                for k in range(2, n//i + 1):
                    decimal[k*i] = False
    return sum(decimal[1:n+1])


print(solution(10))
print(solution(5))
# 에라토스테네스의 체
