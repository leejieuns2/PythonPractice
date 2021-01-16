# chap 04. 반복문
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
print()

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()

print("# 리스트의 요소 하나 제거하기")
list_a = [0, 1, 2, 3, 4, 5]

# 제거 방법[1] - del
del list_a[1]
print("del list_a[1] : ", list_a)

# 제거 방법[2] - pop
list_a.pop(2)
print("pop(2) : ", list_a)

# 값으로 제거하기 - remove
list_a.remove(2)
print("remove(2) : ", list_a)

# 모두 제거하기
list_a.clear()
print(list_a)
