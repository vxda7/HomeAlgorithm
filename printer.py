def solution(priorities, location):
    answer = 1
    idx = 0
    while True:
        most_priority = max(priorities)
        idx_most_priority = priorities.index(most_priority)
        for _ in range(len(priorities)):
            if priorities[idx] == most_priority:
                if idx == location:
                    return answer
                else:
                    priorities[idx] = 0
                    answer += 1
                break
            idx += 1
            if idx == len(priorities):
                idx = 0
# [2 1 3 2] 2
# [2 1 0 2] 2
#
# [1 1 9 1 1 1] 0
# [1 1 0 1 1 1] 0
# [1 1 0 0 1 1] 0
#
#

# def solution(priorities, location):
#     answer = 0
#     idx = 0
#     orders = {}
#     for priority in priorities:
#         orders[idx] = priority
#         idx += 1
#     for order in orders.items():
#         print(order)
#     return answer


print('answer1 :', solution([2, 1, 3, 2], 2))
print('answer2 :', solution([1, 1, 9, 1, 1, 1], 0))
# this = [1, 2, 3]
# print(this.index(2))
# ha = {}
# ha.items()
