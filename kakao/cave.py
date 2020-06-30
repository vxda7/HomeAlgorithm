def solution(n, path, order):
    cave = [[0]*n for i in range(n)]
    for one in path:
        start = one[0]
        end = one[1]
        cave[start][end] = 1
        cave[end][start] = 1

    return cave

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))