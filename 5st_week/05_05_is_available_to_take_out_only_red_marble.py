from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
# 위에서 패턴이 아무것도 안보임 => 다 해봐야하는 건가?

# 파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 True, 없으면 False를 반환한다.
# => 모든 수를 탐색해도 괜찮은 범위
# => BFS를 써야함.
# Queue -> visited [0, 1, 3, 4] 기존에 인덱스를 넣었음
# 공이 2개가 있는데, 각 구슬이 방문했던 곳들을 중첩해서
#                         n    x   m    x   n     x     m
# visited 4차원 배열. [red_row][red_col][blue_row][blue_col] = True

# 각 구슬이 어디에 위치햌는지가 궁금
    # 북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 떄 까지이다.


# [
#     ["#", "#", "#", "#", "#"],
#     ["#", ".", ".", "B", "#"],
#     ["#", "R", "B", ".", "#"],
#     ["#", "R", "O", ".", "#"],
#     ["#", "#", "#", "#", "#"],
# ]
# 세번째 줄에 R이 오른쪽으로 1칸 이동하려고 한다면 B도 오른쪽으로 1칸 이동해야할 것인데, 이 떄, 어느 것이
# B -> 오른쪽 벽으로 가는데 걸린 이동한 칸 몇칸? 1칸
# R -> 오른쪽 벽으로 가는데 걸린 이동한 칸 몇칸? 2칸
# 벽과 얼마나 칸이 떨어져 있는지를 보고 어디까지 움직였을 떄 몇칸 만큼 움직일 수 있느냐를 알고싶은데 벽 혹은 구멍이 나올떄 까지

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0

    # 다음 이동이 벽이거나, 혹은 현재 위치가 구멍이라면
    while game_map[r + diff_r][c+ diff_c] != '#' and game_map[r][c] != 'O':
        r += diff_r
        c += diff_c
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)] # 4차원 배열
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == 'R':
                red_row, red_col = i, j
            if game_map[i][j] == 'B':
                blue_row, blue_col = i, j
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()

        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, red_move_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, blue_move_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i],
                                                                                 game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':
                continue

            if game_map[next_red_row][next_red_col] == 'O':
                return True

            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_move_count > blue_move_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
            # [
            #     ["#", "#", "#", "#", "#"],
            #     ["#", ".", ".", "B", "#"],
            #     ["#", ".", ".", "R,B", "#"],
            #     ["#", "R", "O", ".", "#"],
            #     ["#", "#", "#", "#", "#"],
            # ]
            # 세번째 줄에 R이 오른쪽으로 1칸 이동하려고 한다면 B도 오른쪽으로 1칸 이동해야할 것인데, 이 떄, 어느 것이
            # B -> 오른쪽 벽으로 가는데 걸린 이동한 칸 몇칸? 1칸
            # R -> 오른쪽 벽으로 가는데 걸린 이동한 칸 몇칸? 2칸
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))