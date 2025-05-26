def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        char_idx = ord(char) -  ord('a')
        alphabet_occurrence_array[char_idx] += 1

    max_idx_value = alphabet_occurrence_array[0]
    max_idx = 0
    for index in range(0, len(alphabet_occurrence_array) -1):
        if max_idx_value < alphabet_occurrence_array[index]:
            max_idx_value = alphabet_occurrence_array[index]
            max_idx = index
    return chr(max_idx + ord('a'))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))