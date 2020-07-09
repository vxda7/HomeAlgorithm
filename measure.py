def solution(n):
    answer = 0
    for one in range(1, n // 2 + 1):

        if n % one == 0:
            answer += one
    return answer + n


print(solution(12), 'answer')
print(solution(5), 'answer')
