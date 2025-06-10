array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    array1_idx = 0
    array2_idx = 0
    while array1_idx < len(array1) and array2_idx < len(array2):
        if array1[array1_idx] < array2[array2_idx]:
            result.append(array1[array1_idx])
            array1_idx += 1
        else:
            result.append(array2[array2_idx])
            array2_idx += 1

    while array1_idx < len(array1):
        result.append(array1[array1_idx])
        array1_idx += 1

    while array2_idx < len(array2):
        result.append(array2[array2_idx])
        array2_idx += 1
    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))