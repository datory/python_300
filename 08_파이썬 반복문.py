# 131
# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
from calendar import c


print('131')

# my answer
# 에러

# the answer
# 사과
# 귤
# 수박


# 132
# for문의 실행결과를 예측하라.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")
print('\n132')
# my answer
# #####

# the answer
# #####
# #####
# #####



# 133
# 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
# for 변수 in ["A", "B", "C"]:
#   print(변수)
print('\n133')

# my code
print("A")
print("B")
print("C")

# the answer
# 파이썬 인터프리터가 어떤 순서로 코드를 실행하는지를 떠올려 보세요.
# "변수 바인딩(라인 1) -> 변수 출력 (라인 2)" 과정을 자료구조 데이터 개수 만큼 반복합니다.
변수 = "A"
print(변수)
변수 = "B"
print(변수)
변수 = "C"
print(변수)

# 간단해서 변수의 바인딩없이 다음과 같이 코드를 작성해도 됩니다.
# 모두 동일한 결과를 출력합니다.
print("A")
print("B")
print("C")


# 134
# for문을 풀어서 동일한 동작을하는 코드를 작성하라.
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
print('\n134')
변수 = 'A'
print('출력:', 변수)
변수 = 'B'
print('출력:', 변수)
변수 = 'B'
print('출력:', 변수)

print("출력:", "A")
print("출력:", "B")
print("출력:", "C")



# 135
# for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
print('\n135')
변수 = 'A'
b = 변수.lower()
print('변환:', b)
변수 = 'B'
b = 변수.lower()
print('변환:', b)
변수 = 'C'
b = 변수.lower()
print('변환:', b)

print('변환:', 'a')
print('변환:', 'b')
print('변환:', 'c')



# 136
# 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
print('\n136')
for 변수 in [10, 20, 30]:
    print(변수)

리스트 = [10, 20, 30]
for 변수 in 리스트:
    print(변수)



# 137
# 다음 코드를 for문으로 작성하라.
# print(10)
# print(20)
# print(30)
print('\n137')
for 변수 in [10, 20, 30]:
    print(변수)


    
# 138
# 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
print('\n138')
for 변수 in [10, 20, 30]:
    print(변수)
    print("-------")



# 139
# 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)
print('\n139')

# my code
for 변수 in ['++++', 10, 20, 30]:
    print(변수)

# the answer
print("++++")
for 변수 in [10, 20, 30]:
  print(변수)



#   140
# 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")
print('\n140')

# my code
for 변수 in ['-------', '-------', '-------', '-------']:
    print(변수)

# the answer
for 변수 in ["가", "나", "다", "라"]:
  print("-------")

for 변수 in [1, 2, 3, 4]:
  print("-------")



#   141
# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라.
# 단 부가세는 10원으로 가정한다.
# 리스트 = [100, 200, 300]
# 110
# 210
# 310
print('\n141')
리스트 = [100, 200, 300]
for 변수 in 리스트:
    print(변수+10)
    


# 142
# for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
# 리스트 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김
print('\n142')
리스트 = ["김밥", "라면", "튀김"]
for 변수 in 리스트:
    print('오늘의 메뉴:', 변수)



# 143
# 리스트에 주식 종목이름이 저장돼 있다.
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.
# 6
# 4
# 4
print('\n143')
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 변수 in 리스트:
    print(len(변수))



# 144
# 리스트에는 동물이름이 문자열로 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라.
# dog 3
# cat 3
# parrot 6
print('\n144')
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(동물, len(동물))



# 145
# 리스트에 동물 이름 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.
# d
# c
# p
print('\n145')

# my code
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(동물[:1])

# the answer
리스트 = ['dog', 'cat', 'parrot']
for 이름 in 리스트:
  print(이름[0])



# 146
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1
# 3 x 2
# 3 x 3
print('\n146')
리스트 = [1, 2, 3]
for 숫자 in 리스트:
    print('3 x', 숫자)



# 147
# 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
print('\n147')

# my code
리스트 = [1, 2, 3]
for 숫자 in 리스트:
    print('3 x', 숫자, '=', 3*숫자)

# the answer
리스트 = [1, 2, 3]
for 변수 in 리스트:
  print("3 x {} = {}".format(변수, 3 * 변수))



# 148
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 나
# 다
# 라
print('\n148')

# my code
리스트 = ["가", "나", "다", "라"]
for 한글 in 리스트:
    print(한글)

# the answer
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[1:]:
  print(변수)



# 149
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 가
# 다
print('\n149')

# my code
리스트 = ["가", "나", "다", "라"]
리스트 = 리스트[0], 리스트[2]
for 한글 in 리스트:
    print(한글)

# the answer
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :2]:
  print(변수)



# 150
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 라
# 다
# 나
# 가
print('\n150')

# my code
리스트 = ["가", "나", "다", "라"]
리스트.reverse()
for 한글 in 리스트:
    print(한글)

# the answer
리스트 = ["가", "나", "다", "라"]
for 변수 in 리스트[: :-1]:
  print(변수)


  
# 151
# 리스트에는 네 개의 정수가 저장돼 있다.
# 리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
# -20
# -3
print('\n151')
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0:
        print(변수)


        
# 152
# for문을 사용해서 3의 배수만을 출력하라.
# 리스트 = [3, 100, 23, 44]
# 3
print('\n152')
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
    if 변수 % 3 == 0:
        print(변수)



# 153
# 리스트에서 20 보다 작은 3의 배수를 출력하라
# 리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18
print('\n153')

# my code
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
    if 변수 < 20 and 변수 % 3 == 0:
        print(변수)

# the answer
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
    if (변수 < 20) and (변수 % 3 == 0):
        print(변수)



# 154
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language
print('\n154')
리스트 = ["I", "study", "python", "language", "!"]
for 변수 in 리스트:
    if len(변수) >= 3:
        print(변수) 



# 155
# 리스트에서 대문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# A
# D
# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
# >> 변수 = "A"
# >> 변수.isupper()
# True
# >> 변수 = "a"
# >> 변수.isupper()
# False
print('\n155')
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.isupper():
        print(변수)



# 156
# 리스트에서 소문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# b
# c
print('\n156')

# my code
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
    if 변수.islower():
        print(변수)

# the answer
# 비교 연산자를 사용해서 다음과 같이 표현할 수 있습니다.
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() == False:
    print(변수)
    
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper() != True:
    print(변수)

# 논리 연산자 not을 사용할 수도 있습니다.
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if not 변수.isupper():
    print(변수)



# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.

# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.

# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC
print('\n157')
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수.upper())



# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
# (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
print('\n158')
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
리스트[:].split(.)
print(리스트)
for 변수 in 리스트:
    print(변수)

