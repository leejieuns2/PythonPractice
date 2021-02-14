# 백준 1316. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

num = int(input())

rslt = 0
for i in range(num):
    str = input()

    word = []
    rslt += 1
    for s in str:
        if s in word:
            # 문자가 연속되는 경우
            # 직전애 삽입된 word의 값이 지금 value의 값과 같은 경우는 연속되기 때문에 그룹 단어다.
            if word.index(s) == len(word) - 1:
                continue
            # 이미 있는 단어인데 연속되지 않을 경우
            else:
                # 그룹 단어가 아니므로 -1
                rslt -= 1
                break
        else:
            word.append(s)

print(rslt)
