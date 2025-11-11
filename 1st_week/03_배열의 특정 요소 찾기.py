def is_number_exist(number, array):

    # 방법1 O(n)
    # for arr in array:
    #     if arr == number:
    #         return True
    # return False

    # 방법2. O(1) Set 사용 
    array_set = set(array)
    return number in array_set

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))