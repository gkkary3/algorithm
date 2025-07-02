input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    result =  fibo_recursion(n-1) + fibo_recursion(n-2)

    return result


print(fibo_recursion(input))  # 6765