# 변수 선언
min_person = 2
max_person = 10
total_person = 100
memo = {}


def question(leave, sit):
    key = str([leave, sit])
    # 종료 조건
    if key in memo:
        return memo[key]
    if leave < 0:
        return 0    # 무효하니 0을 리턴한다.
    if leave == 0:
        return 1    # 유효하므로 1을 리턴한다.

    # 재귀 처리
    count = 0
    for i in range(sit, max_person + 1):
        count += question(leave - i, i)

    # 메모화 처리
    memo[key] = count

    # 종료
    return count


print(question(100, min_person))
