# 백준 2908. 상수
# https://www.acmicpc.net/problem/2908

num1, num2 = input().split(" ")

# 문자열 reverse
num1 = num1[::-1]
num2 = num2[::-1]

# 삼항연산자 사용
print(num1 if int(num1) > int(num2) else num2)
