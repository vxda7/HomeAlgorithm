def solution(strings, n):
    answer = {}
    for string in strings:
        if string[n] not in answer:
            answer[string[n]] = [string]
        else:
            answer[string[n]].append(string)
    order = sorted(list(answer))
    result = []
    for i in order:
        result.extend(sorted(answer[i]))
    return result


print(solution(['sun', 'bed', 'car'],	1))
