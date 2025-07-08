input = "abcabcabcabcdededededede"

# n = len(input)

# for split_size in range(1, n // 2 + 1):
#     splited = []
#     for i in range(0, n, split_size):
#         # print(i, input[i:i + split_size])
#         splited.append(input[i:i + split_size])
#     print("splited is ", splited)

# 1개의 길이
# a
# b
# c
# d ....
#
# 2개의 길이
# ab
# ca
# bc ....

# 모든 경우에서 가장 압축을 많이 시킨 문자열의 길이를 반환

# 문자여르이 길이를 n 이라고 한다면,
# 1부터 n개까지 길이로 쪼갤 수 있다.
#
# 1 ~ n//2 까지만 쪼개자 => 왜냐하면 반이 넘어가는 것 까지 쪼개면 애초에 성립될 수 없다. 반 이상의 기링가 반보고딜 수 없기 떄문

def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, n // 2 + 1):
        splited = []
        for i in range(0, n, split_size):
            # print(i, input[i:i + split_size])
            splited.append(string[i:i + split_size])

        compressed = ""
        count = 1
        for i in range(0, len(splited) - 1): # 맨 뒤에꺼는 안보겠다는 의미 현재 인덱스 기준으로 뒤에꼐 나랑 일치하는 지만 보기 떄문
            cur, next = splited[i], splited[i + 1]

            if cur == next:
                count += 1
            else:
                if count == 1:
                    compressed += cur
                else:
                    compressed += f"{count}{cur}"
                count = 1
        if count == 1:
            compressed += splited[-1]
        else:
            compressed += f"{count}{splited[-1]}"
        result = min(len(compressed), result)
    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))