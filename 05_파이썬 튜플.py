# 071
# my_variable 이름의 비어있는 튜플을 만들라.
print('071 튜플')
my_variable = ()
print(type(my_variable))



# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
print('072 튜플')
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)



# 073
# 숫자 1 이 저장된 튜플을 생성하라.
print('073 튜플')

# my code
num = (1)
print(num)

# the answer
my_tuple = (1)
type (my_tuple)



# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
print('074 튜플 오류')

# my code
# 튜플은 변경이 불가하다.

# the answer
# tuple은 원소(element)의 값을 변경할 수 없습니다.



# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
print('075 튜플')
t = 1, 2, 3, 4
print(type(t))
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.



# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
print('076 튜플')

# my code
t = ('a', 'b', 'c')

# the answer
t = ('A', 'b', 'c')
print(t)



# 077
# 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
print('077 튜플 리스트로 변환')

# my code
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(type(interest))

# the answer
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(type(data))



# 078
# 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
print('078 리스트 튜플로 변환')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(type(tuple(interest)))


