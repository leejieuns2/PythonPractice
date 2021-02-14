# 파이썬 연습
# 백준 10809. 알파벳 찾기
# https://www.acmicpc.net/problem/10809

# 알파벳 소문자 리스트를 가져오기 위해 import 추가
from string import ascii_lowercase

alpha_list = list(ascii_lowercase)
str = list(input())

# A-Z 까지 str에 있는지 탐색
for i in range(len(alpha_list)):
    if(alpha_list[i] in str):
        # 있으면 첫번째 index 출력
        print(str.index(alpha_list[i]), end=' ')
    else:
        # 없으면 -1
        print(-1, end=' ')
