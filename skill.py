def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        learn = list(skill)
        for one_skill in skill_tree:
            if learn != []:
                if one_skill == learn[0]:
                    learn.pop(0)
                elif one_skill in learn:
                    break
            if skill_tree[-1] == one_skill:
                answer += 1
    return answer


print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))
