name ='김인영'
age = '29'

print("-"*40)
c = name+'님 반갑습니다. ' + '나이는 ' + age + '살 이시군요. '
print(c)
print("-"*40)

#파이썬 데이터의 길이 구하는 함수
print(len(c))

#인덱싱과 슬라이싱
#인덱싱: 각 문자열 마다 번호를 부여
#슬라이싱: 추출하고자 하는 문자열의 인덱싱 번호를 통해 호출

a = "Life is too short, You need Pyton."
print(a[0], a[-1])