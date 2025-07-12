k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]

# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 0 -> 1
# 1 -> 0
# 2 -> 3
# 3 -> 2

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

# 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.
#
# 게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.
#
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다. 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

# => 쌓인 순서를 저장 => 즉, Map에서 어떻게 체크 말들이 쌓여있는지 저장 => game_map 과 유사하게 만들되, 2차원 배열의 원소 각각에 리스트[stack] 저장
# => 쌓인 순서대로 같이 이동 => Stack을 써야된다.
# => 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다 => 반복문으로 이동시키는 것이 필요

# 1. 1번 말이 이동하려는 칸이
#     1) 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 1번 말을 올려놓는다.
#          - 1번 말의 위에 다른 말이 있는 경우에는 1번 말과 위에 있는 모든 말이 이동한다.
#          - 예를 들어, 1, 2, 3로 쌓여있고, 이동하려는 칸에 4, 5가 있는 경우에는 1번 말이 이동한 후에는 4, 5, 1, 2, 3가 된다.
#      2) 빨간색인 경우에는 이동한 후에 1번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
#          - 1, 2, 3 가 이동하고, 이동하려는 칸에 말이 없는 경우에는 3, 2, 1가 된다.
#          - 1, 4, 6, 7가 이동하고, 이동하려는 칸에 말이 5, 3, 2로 있는 경우에는 5, 3, 2, 7, 6, 4, 1가 된다.
#       3) 파란색인 경우에는 1번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
#       4) 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1 # 맨처음 게임 시작한 부분도 하나의 턴이라고 가정
    current_stacked_horse_map = [[ [] for _ in range(n) ] for _ in range(n) ]  # 4 x 4 2차원 배열
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i) #current_stacked_horse_map[0][0] = [0]

    while turn_count <= 1000:
        for  horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r, new_c = r + dr[d], c + dc[d]

            #       3) 파란색인 경우에는 1번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
            #       4) 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                # 이동 방향을 반대로 하고 한칸 이동.
                new_r, new_c = r + dr[new_d], c + dc[new_d]
                horse_location_and_directions[horse_index][2] = new_d # 본래의 위치에도 direction을 update

                # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우와 체스판을 벗어나는 경우 이동하지 않고 가만히
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue


            #    1) 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 1번 말을 올려놓는다.
            #      - 1번 말의 위에 다른 말이 있는 경우에는 1번 말과 위에 있는 모든 말이 이동한다.
            #      - 예를 들어, 1, 2, 3로 쌓여있고, 이동하려는 칸에 4, 5가 있는 경우에는 1번 말이 이동한 후에는 4, 5, 1, 2, 3가 된다.

            # current_stacked_horse_map[0][0] = [0,3,4] 0번쨰 인덱스 말이 동쪽으로 이동한다. => 0,3,4 가 이동
            # current_stacked_horse_map[0][1].append(current_stacked_horse_map[0][0])


            # current_stacked_horse_map[0][0] = [0,3,4] 3번쨰 인덱스 말이 동쪽으로 이동한다. => 3, 4가 이동
            # current_stacked_horse_map[0][0] = [0] 으로 업데이트!
            # current_stacked_horse_map[0][1].append(current_stacked_horse_map[0][0][현재 이동하려고 했던 말 위에 있는 것들만])
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]

                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break

            # 2) 빨간색인 경우에는 이동한 후에 1번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            # - 1, 2, 3가 이동하고, 이동하려는 칸에 말이 없는 경우 3,2,1가 된다.
            # - 1, 4, 6, 7가 이동하고, 이동하려는 칸에 말이 5,3,2로 있는 경우 5,3,2,7,6,4,1가 된다.
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                # 본래의 위치에도 r,c 를 update
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c
            #   턴이 징행 되던 중 말이 4개 이상 쌓이는 순간 게임이 중단.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))