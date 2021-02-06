# 파이썬 연습
# 백준 11720. 숫자의 합
# https://www.acmicpc.net/problem/11720

size = int(input())
num = list(input())
sum = 0
for i in range(size):
    sum += int(num.pop())
print(sum)
