from collections import deque

c = 11
b = 2

# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉, 증가하는 속도가 1초마다 1씩 계속 늘어난다.

# B - 1, B + 1, 2 * B

# Cony
# T 0 1  2  3  4
#  11 12 14 17 21

# Brown
# 모든 경우의 수를 다 봐야함. => BFS, DFS
# T 0 1                                  => 배열
#   2 1-1. B-1 = 1    1-1-1, B-1 = 0     => 위치가 동적으로 마구잡이로 변하는 경우 키 값을 추가하기 쉬운 딕셔너리
#                     1-1-2, B+1 = 2     => [0] 초에 위치할 수 있었던 곳들
#                     1-1-2, 2*B = 2     => [1] 초에 위치할 수 있었던 곳들
#                                        => [2] 초에 위치할 수 있었던 곳들
#                                           [{key1: 1, key2: 2 }, ... ]
#     1-2, B+1 = 3    1-2-1, B-1 = 2
#                     1-2-2, B+2 = 4
#                     1-2-3, 2*B = 6

#     1-3. 2*B = 4
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))

    # 10 이라는 위치에 도달 했던 게 1초, 10초 600초 700초

    visited = [{} for _ in range(200001)] # [{}, {} ... 20만개]

    #visited[10] = {1: 10: 600: 700: True}

    #visited[3] = 3의 위치에 도달한 시간들의 모음집. dictionary  = {5: True, 0: True}
    #visited[5] = 5의 위치에 도달한 시간들의 모음집. dictionary

    # 1. 코니와 브라운의 위치 p는 조건0 <= x <= 200,000.을 만족한다.
    # 2. 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
    while cony_loc <= 200000:
        cony_loc += time # Cony의 위치
        if cony_loc > 200000:
            break

        if time in visited[cony_loc]:
            return time

        for _ in range(0, len(queue)):
            current_position, current_time = queue.popleft() # brown_loc , 0

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True ## 현재 new_position이 위치한 곳에 new_time 이라는 키 값에 true를 대입
                queue.append((new_position,new_time)) # brown_loc - 1, 1
            new_position = current_position + 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True  ## 현재 new_position이 위치한 곳에 new_time 이라는 키 값에 true를 대입
                queue.append((new_position, new_time))  # brown_loc + 1, 1
            new_position = current_position * 2
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True  ## 현재 new_position이 위치한 곳에 new_time 이라는 키 값에 true를 대입
                queue.append((new_position, new_time))  # brown_loc * 1, 1

        # 2. 중복 제거 방법
        # for _ in range(len(queue)):
        #     current_position, current_time = queue.popleft()
        #     new_time = current_time + 1
        #
        #     for new_position in [current_position - 1, current_position + 1, current_position * 2]:
        #         if 0 <= new_position <= 200000:
        #             # 중복 방지
        #             if new_time not in visited[new_position]:
        #                 visited[new_position][new_time] = True
        #                 queue.append((new_position, new_time))
        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))