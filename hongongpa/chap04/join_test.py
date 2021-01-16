# join()
# 문자열.join(문자열로 구성된 리스트)

print("::".join(["1", "2", "3", "4", "5"]))
number = int(input("정수 입력 > "))

# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {} 입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {} 입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))
