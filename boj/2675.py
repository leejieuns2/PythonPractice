# 파이썬 연습
# 백준 2675. 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())

# 테스트 케이스 개수가 정해져 있지 않으므로 각각 리스트에 담기
rlist = []
slist = []

# 테스트 케이스 개수만큼 입력 받기
for i in range(t):
    r, s = input().split()
    rlist.append(r)
    slist.append(s)

for i in range(t):
    s = slist[i]
    r = rlist[i]
    rslt = ''

    # 파이썬은 문자열 곱셈이 가능하므로 문자열 곱셈으로 새 string 만들기
    for j in range(len(s)):
        rslt = rslt + (s[j] * int(r))

    print(rslt)
