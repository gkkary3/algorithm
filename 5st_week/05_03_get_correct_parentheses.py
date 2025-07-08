from collections import deque

balanced_parentheses_string = "()))((()"


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


def get_correct_parentheses(balanced_parentheses_string):
    if(is_correct_parenthesis(balanced_parentheses_string)):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

def change_to_correct_parenthesis(balanced_parentheses_string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if balanced_parentheses_string == '':
        return ''
    # 2. 문자열 balanced_parentheses_string를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    # u
    # ()()(
    # () => u 가능
    # ()() => u 불가능 wht? 다시 ()로 쪼갤 수 있기 떄문

    # )))()(((( => 열린괄호와 닫힌괄호의 개수가 일치할 떄까지 찾으면 됨
    u, v = separate_to_u_v(balanced_parentheses_string)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1: -1])

def separate_to_u_v(string):
    queue = deque(string)
    left_parenthtis, right_parenthtis = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char # )
        if char == '(':
            left_parenthtis += 1
        if char == ')':
            right_parenthtis += 1

        if left_parenthtis == right_parenthtis:
            break
    v = ''.join(queue) # '('
    return u, v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ')'
        elif char == ')':
            reversed_string += '('
    return reversed_string
print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))