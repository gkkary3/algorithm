
# 예시: 0001100
# 그룹: 000, 11, 00 → 0그룹 = 2개, 1그룹 = 1개
#
# 모두 0으로 만들려면 1번만 뒤집으면 됨 → 정답: 1
def count_min_flips(s):
    # 첫 문자를 기준으로 초기 그룹 설정
    count_0 = 0
    count_1 = 0

    if s[0] == '0':
        count_0 += 1
    else:
        count_1 += 1

    # 연속된 숫자가 바뀔 때마다 그룹 수 증가
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 += 1

    return min(count_0, count_1)

print("정답 =", count_min_flips("0001100"))  # 출력: 1
print("정답 =", count_min_flips("11111"))    # 출력: 0
print("정답 =", count_min_flips("010101"))   # 출력: 2
