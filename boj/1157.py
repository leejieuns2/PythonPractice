# 파이썬 연습
# 백준 1157. 단어 공부
# https://www.acmicpc.net/problem/1157

str = input()

# 문자열 전부 대문자로 변경 (대/소문자 구별 없이 같은 결과가 나와야 하므로)
str = str.upper()

# 알파벳 개수 세기
dic = {}
for i in range(len(str)):
    if str[i] in dic:
        dic[str[i]] += 1
    else:
        dic[str[i]] = 1

# 가장 많이 사용된 알파벳 찾기
max_key = max(dic, key=dic.get)
max_value = dic[max_key]
dic.pop(max_key)

# 가장 많이 사용된 알파벳이 여러 개일 경우 ? 출력
if max_value in dic.values():
    print("?")
else:
    print(max_key)
