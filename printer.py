def solution(priorities, location):
    answer = 0
    stack = [priorities[0]]
    i = 1
    for priority in priorities[1:]:
        if stack[-1] >= priority:
            stack.append(priority)
        else:
            j = i
            while stack[-j] > priority:
                j -= 1
                if j == 0:
                    break
            stack.insert(-2, priority)
        i += 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
