# 확인문제 5-2-1
# 리스트 평탄화(flatten)


def flatten(data):
    result = []
    for d in data:
        if type(d) == list:
            # 리스트끼리 덧셈 연산 가능.
            result += flatten(d)
        else:
            result.append(d)
    return result


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example))
