
import sys

# end => 끝에 붙이기
print("python", "java", "javascript", sep=", ", end="?")
print("무엇이 더 재밌을까요?")

# 표준입출력
print("Python", "Java", file=sys.stdout)
# 에러출력
print("Python", "Java", file=sys.stderr)

subject = "수학"
score = 20
# 오른쪽, 왼쪽 공백처리
print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번호
# 001,002,003
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

# 사용자 입력을 받아 저장한 변수는 default가 string으로 전환됨.
# 만약 정수형으로 받고 싶으면 추후 변환 필요.
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 {0} 입니다.".format(answer))

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >-10}".format(-500))
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
print("{0:^<+30,}".format(100000000))
