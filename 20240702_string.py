name ='김인영'
age = '29'

print("-"*40)
c = name+'님 반갑습니다. ' + '나이는 ' + age + '살 이시군요. '
print(c)
print("-"*40)

#파이썬 데이터의 길이 구하는 함수
print(len(c))

#파이썬 문자열의 인덱싱 및 슬라이싱
#인덱싱: 각 문자열 마다 번호를 부여
#슬라이싱: 추출하고자 하는 문자열의 인덱싱 번호를 통해 호출

str = "국가기간/전략산업과정 스마트안전 Python 활용 데이터분석"
print(len(str))
print(str[0], str[-1])

#print(Python)
print(str[18:25])
print(str[-15:-9])


#데이터타입
a = "1"
b = 1

print(a)
print(b)

print(type(a))
print(type(b))

#숫자형의 사칙 연산
number_1 = 10
number_2 = 5
print(number_1/number_2)

number_3 = 13
number_4 = 2
print(number_3//number_4)
print(number_3%number_4)

print(number_4**number_2)


