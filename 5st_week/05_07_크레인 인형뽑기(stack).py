board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        index = move -1
        for row_info in board:
            if row_info[index] != 0:
                bucket.append(row_info[index])
                row_info[index] = 0

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    answer += 2
                    bucket = bucket[0:-2]
                break
    return answer

print(solution(board,moves))