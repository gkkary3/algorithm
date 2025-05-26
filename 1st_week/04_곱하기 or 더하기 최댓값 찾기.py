# 리스트를 왼쪽에서 오른쪽으로 보면서, 현재 수와 결과값을 더할지 곱할지 선택한다.
# 현재 값이나 결과값 중 하나라도 0 또는 1이면 더하기
# 둘 다 2 이상이면 곱하기

def find_max_plus_or_multiply(array):
    result = array[0]  # 첫 번째 값을 초기값으로 설정

    for i in range(1, len(array)):
        num = array[i]
        print("현재 값:", num, "현재 결과:", result)

        if result <= 1 or num <= 1:
            result += num
        else:
            result *= num

        print("계산 후 결과:", result)

    return result

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0, 3, 5, 6, 1, 2, 4]))
print("정답 = 8820 현재 풀이 값 =", result([3, 2, 1, 5, 9, 7, 4]))
print("정답 = 270 현재 풀이 값 =", result([1, 1, 1, 3, 3, 2, 5]))
