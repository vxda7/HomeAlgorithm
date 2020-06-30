def solution(board):
    price = 0
    n = len(board[0])
    stack = [[0, 0, 0, []]]
    direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visit = [[100000]*n for i in range(n)]
    before = []
    bestprice = 100000000000
    while True: # 최저가가 나올 때 까지 반복
        if stack == []: # 모든 위치를 다 둘러봄
            break
        now = stack.pop()  # 현재 위치
        visit[now[0]][now[1]] = now[2]   # 현위치까지 사용한 도로 비용
        before = now[3]
        if now == [n - 1, n - 1] and bestprice > visit[n-1][n-1]:   # 현위치가 도착점이라면
            bestprice = visit[n-1][n-1] # 최종가격은 현위치의 가격
        else:
            for one in direction:   # 4방향 모두 확인
                afterx = now[0] + one[0]    # 다음 위치
                aftery = now[1] + one[1]
                if before == one or before == []:   # 시작점이거나 이전과 같은 방향
                    price = visit[now[0]][now[1]] + 100 # 직선도로 100원
                else:   # 커브 500원
                    price = visit[now[0]][now[1]] + 600
                if 0 <= afterx < n and 0 <= aftery < n:
                    # 벽이 없거나 방문할 곳의 가격이 현재 보다 비싸면
                    if board[afterx][aftery] == 0 and visit[afterx][aftery] >= price:
                        stack.append([afterx, aftery, price, one])
    # print(bestprice)
    # print(visit)
    return visit[n-1][n-1]

a = solution([[0, 0, 1, 0, 0],
[1, 0, 0, 1, 0],
[0, 1, 0, 0, 1],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0]])
print(a)