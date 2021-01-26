
# 메모 변수를 저장할 딕셔너리를 선언합니다.
dictionary = {
    1: 1,
    2: 1
}


# 함수를 선언합니다.
def fibonacci(n):
    if n in dictionary:
        # 만약 메모가 되어 있으면 메모된 값을 리턴.
        return dictionary[n]
    else:
        # 메모되어 있지 않다면, 값을 계산한 후 메모에 저장.
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output


# 함수를 호출합니다.
print("fibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))
print("fibonacci(30): ", fibonacci(30))
print("fibonacci(40): ", fibonacci(40))
