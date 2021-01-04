# 집합 (Set)
# 중복 안됨, 순서 없음

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (자바와 파이썬을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (자바를 할 수 있거나 파이썬을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (자바를 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬을 할 줄 아는 사람이 늘어님
python.add("김태호")
print(python)

# 자바를 잊었어요
java.remove("김태호")
print(java)
