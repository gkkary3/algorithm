# 장르별 가장 많이 재생된 곡 2개

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다. (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
#
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
#
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]

def get_melon_best_album(genres, plays):
    genre_play_sum = {}       # 장르별 총 재생 수
    genre_to_songs = {}       # 장르별 곡 리스트: [(재생 수, 고유 번호)]

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 수 저장
        if genre not in genre_play_sum:
            genre_play_sum[genre] = 0
        genre_play_sum[genre] += play

        # 장르별 곡 정보 저장
        if genre not in genre_to_songs:
            genre_to_songs[genre] = []
        genre_to_songs[genre].append((play, i))

    # 1. 장르를 총 재생 수 기준으로 내림차순 정렬
    genre_play_list = list(genre_play_sum.items())
    genre_play_list.sort(key=lambda x: x[1], reverse=True)

    result = []

    for genre, _ in genre_play_list:
        # 2. 각 장르의 곡들을 재생 수 내림차순, 고유 번호 오름차순으로 정렬
        songs = genre_to_songs[genre]
        songs.sort(key=lambda x: (-x[0], x[1]))

        # 3. 최대 2곡까지 추가
        for song in songs[:2]:
            result.append(song[1])

    return result



print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))