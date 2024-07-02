#리스트
#여러 값을 저장하는 배열이다.
#리스트에 포함된 값은 요소(Element)
#대괄호 '[]'로 표현하며, 요소는 ',' 쉼표로 구분한다.

list_kiy = ["김인영", "29", "010-2264-****", "서울시"]
print(list_kiy)
print(type(list_kiy))

print("-"*40)

print(list_kiy[0])
print(list_kiy[1])
print(list_kiy[2])
print(list_kiy[3])
print(list_kiy[-1])

print("-"*40)

#변수에 리스트의 요소 대입
name = list_kiy[0]
age = list_kiy[1]
call = list_kiy[2]
print(name)

print("-"*40)

#리스트의 요소로 리스트 삽입
students = [['학생A', '학생B', '학생C'], ['20', '21', '22'], ['서울', '인천', '대전']]
print(students[0][1])
print(students[1][0:3])

print("-"*40)

#리스트 요소끼리 사칙연산
numbers = [1, 2, 3, 4, 5]
c = numbers[2] + numbers[4]
print(c)

print("-"*40)

#리스트의 요소 개수 출력
print(len(numbers))

print(len(students))
print(len(students[0]))

print("-"*40)

#리스트에 요소 추가하기
elist = []
elist.append(30)
elist.append(25)
elist.append(99)

#리스트에 요소 삭제하기
elist.remove(30)

print(elist)