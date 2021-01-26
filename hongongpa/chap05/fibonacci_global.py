# 변수를 선언합니다.
counter = 0


# 함수를 선언합니다.
def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력합니다.
    print("fibonacci({})를 구합니다.".format(n))

    # global 변수
    # : 파이썬은 함수 내부에서 함수 외부에 있는 변수를 참조하지 못하기 때문에 global 키워드를 사용해 선언해주어야 함.
    global counter
    counter += 1

    # 피보나치를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 함수를 호출합니다.
fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
