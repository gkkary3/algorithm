def is_correct_parenthesis(string):
    stack = []
    isTrue = False
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        isTrue = True
    
    return isTrue


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))