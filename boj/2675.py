# 파이썬 연습
# 백준 2675. 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())

rlist = []
slist = []
for i in range(t):
    r, s = input().split()
    rlist.append(r)
    slist.append(s)

for i in range(t):
    s = slist[i]
    r = rlist[i]
    rslt = ''

    for j in range(len(s)):
        rslt = rslt + (s[j] * int(r))

    print(rslt)
