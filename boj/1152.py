# 백준 1152. 단어의 개수
# https://www.acmicpc.net/problem/1152

# 공백만 입력받는 부분을 고려해야 함.
# filter() 함수를 이용해 공백이 리스트에 삽입되는 것을 방지함
# strip() 함수 : 양옆의 공백을 제거해주는 함수.
str = list(filter(None, input().strip().split(" ")))
print(len(str))
