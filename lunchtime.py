t = int(input())
for tc in range(1, t+1):
        N = int(input())
        upstairs = [list(map(int, input().split())) for i in range(N)]

        stairs = []
        mans = []
        for i in range(N):
            for j in range(N):
                if upstairs[i][j] > 1:
                    stairs.append([i, j])
                elif upstairs[i][j] == 1:
                    mans.append([i, j])
        people = len(mans)
        # 입력 받기

        # 정보가공  i번째 사람과 계단 1,2 와의 거리
        infos_first = []
        infos_last = []
        for i in range(people):
            infos_first.append(abs(mans[i][0] - stairs[0][0]) + abs(mans[i][1] - stairs[0][1]))
            infos_last.append(abs(mans[i][0] - stairs[0][1]) + abs(mans[i][1] - stairs[1][1]))

        # 가능성 만들기
        possibles = []
        for i in range(1 << people):
            temp = []
            for j in range(people):
                if i & (1 << j):
                    temp.append(1)
                else:
                    temp.append(0)
            possibles.append(temp[:])
        print(possibles)


        # 만들어진 가능성을 시간에 따라 돌면서 시간선 구축
        for one in possibles:
            timetable_first = [[0]*30 for i in range(people)]
            timetable_last = [[0]*30 for i in range(people)]
            downman = 0
            time = 0
            # 정보복사
            tinfos_first = infos_first[:]
            tinfos_last = infos_last[:]

            # 모든 사람이 내려갔는가?
            while downman != people:
                time += 1   # 1초증가
                for i in range(people):
                    if one[i] == 0:     # i번 사람이 1번 계단을 선택했다면
                        tinfos_first[i] -= 1
                    else:   # 2번
                        tinfos_last[i] -= 1

                    # 1번 계단입구에 도착했다면
                    if tinfos_first[i] == 0:
                        now_in_stair = people - list(map(list, zip(*timetable_first))).count(0)
                        if now_in_stair < 3:
                            timetable_first
                    elif tinfos[i][1] == 0:     # 2번



