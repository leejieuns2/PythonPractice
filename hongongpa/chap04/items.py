# 딕셔너리 선언
example_dictionary = {
    "keyA": "valueA",
    "keyB": "valueB",
    "keyC": "valueC",
}

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 items() 함수")
print("items() : ", example_dictionary.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
