# Tuple(튜플)
# 리스트와 비슷한 자료형. 한번 결정된 요소를 바꿀 수 없다는 특징 존재.
# 튜플은 특이하게 괄호를 생략해도 튜플로 인식하기 때문에 쉽게 선언할 수 있음.

# 괄호가 없는 튜플.
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test: ", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용.
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a: ", a)
print("b: ", b)
print("c: ", c)
