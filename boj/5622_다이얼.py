# 백준 5622. 다이얼
# https://www.acmicpc.net/problem/5622

# enumerate
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.

alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

str = input()

rslt = 0
for i in str:
    for index, value in enumerate(alphabet):
        if(i in value):
            # index는 0부터 시작, 숫자 1을 걸려면 2초가 필요하므로 기존 index에서 3을 더해야함.
            rslt += index + 3
            break

print(rslt)
