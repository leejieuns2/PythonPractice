# 리스트

# 리스트를 선언합니다.
# 파이썬은 리스트를 출력할 때 자동적으로 [] (대괄호)와 , (쉼표)가 추가됨.
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 출력합니다
print("# 리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

# 기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

# 함수
print("# 길이 구하기")
print("len(list_a) = ", len(list_a))

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(subway)

# 모두 지우기
num_list.clear()
print(subway)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 가능
num_list.extend(mix_list)
print(num_list)
