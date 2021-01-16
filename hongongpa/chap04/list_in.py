# 리스트 내포

# 리스트 내포를 하지 않은 원래의 for문 코드
array = []

for i in range(0, 20, 2):
    array.append(i * i)

print(array)

# 리스트를 선언합니다.
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것]
array = [i * i for i in range(0, 20, 2)]

# 리스트를 출력합니다.
print(array)

# 리스트 내포 안에 if 구문 넣어서 조합하기

# 리스트를 선언합니다.
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

# 리스트를 출력합니다.
print(output)
