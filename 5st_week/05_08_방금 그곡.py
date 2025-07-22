import math

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def replace_step(m):
    return m.replace("C#", "c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")

def solution(m, musicinfos):
    answer = None
    max_play_time = 0
    m = replace_step(m)

    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(",")
        split_end_time = end_time.split(":")
        split_start_time = start_time.split(":")

        play_time = int(split_end_time[1]) - int(split_start_time[1])
        melody = replace_step(melody)
        # ABC(3) 라는 melody가 16초 진행되었다.
        # ABCABCABCABCA
        # 5번 + 1 -> 6번동안 반복하게 만들어라.
        # 올림(실행시간 / 멜로디의 길이)
        melody_repeated_count = math.ceil(play_time / len(melody)) # 2
        melody_played = (melody * melody_repeated_count)[:play_time]  # CDEFGABCDEFGAB
        # print("melody_played is ", melody_played)

        # 자신이 들은 멜로디가 포함되어 있는 음악 중 재생 시간이 제일 긴 음악 제목을 반환.
        if m in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time

    if answer is None:
        return "(None)"

    return answer

print(solution(m,musicinfos))
# C# -> c D# -> d