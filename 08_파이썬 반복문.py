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

# my code
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
    print(변수[0].upper(), 변수[1:])

# the answer
# 지금까지 배웠던 내용을 모두 응용해야 하는 문제입니다. 첫 번째 단어만 대문자로 변경해야하기 때문에 아래의 순서로 처리해야 합니다.
# 1) 인덱싱으로 첫번째 문자를 가져온다.
# 2) upper() 함수로 대문자로 변경한다.
# 3) 변경한 대문자와 나머지 문자를 이어붙인다.
# 정리한 내용을 코드로 작성하면 다음과 같습니다.
리스트 = ['dog', 'cat', 'parrot']
for 변수 in 리스트:
  첫글자 = 변수[0]              # 1)
  대문자 = 첫글자.upper()     # 2)
  print(대문자 + 변수[1:])      # 3)

# 간단하기 때문에 한줄에 코드를 작성해도 좋습니다.
for 변수 in 리스트:
  print(변수[0].upper() + 변수[1:])



# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
# (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
print('\n158')

# my code
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# 리스트[:].split(.)
# print(리스트)
# for 변수 in 리스트:
#     print(변수)

# the answer
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for 변수 in 리스트:
  split = 변수.split(".")
  print(split[0])  



# 159
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
print('\n159')
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if split[1] == 'h':
    print(변수)



# 160
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h
print('\n160')

# my code
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split('.')
  if split[1] == 'h' or split[1] == 'c':
    print(변수)

# the answer
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)



# 161
# for문과 range 구문을 사용해서 0~99까지
# 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
print('\n161')
for 변수 in range(100):
  print(변수)



# 162
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여
# 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
# 참고) range의 세번 째 파라미터는 증감폭을 결정합니다.
# >> print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]
print('\n162')
for i in range(2002, 2051, 4):
  print(i)



# 163
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
# 3 
# 6 
# 9 
# 12 
# 15 
# 18 
# 21 
# 24 
# 27 
# 30
print('\n163')

# my code
for x in range(0, 31, 3):
  if x == 0:
    pass
  else:
    print(x)

# the answer
for num in range(3, 31, 3):
    print (num)



# 164
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
print('\n164')

# my code
for num in range(99, -1, -1):
  print(num)

# the answer
for i in range(100):
    print(99 - i)



# 165
# for문을 사용해서 아래와 같이 출력하라.
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
print('\n165')

# my code
# for num in range(0, 1, 0.1):
#   print(num)

# the answer
for num in range(10) :
    print(num / 10)



# 166
# 구구단 3단을 출력하라.
# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27
print('\n166')

# my code
for num in range(1, 10):
  print(num * 3)

# the answer
for i in range(1, 10) :
    print (3, "x", i, " = ", 3 * i)



# 167
# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
# 3x1 = 3
# 3x3 = 9
# 3x5 = 15
# 3x7 = 21
# 3x9 = 27
print('\n167')

# my code
for num in range(1, 10):
  if num % 2 == 1:
    print(3, 'x', num, '=', num * 3)

# the answer
# range(1, 10, 2)를 사용해서 홀수를 만듭니다.
num = 3
for i in range(1, 10, 2) :
    print (num, "x", i, " = ", num * i)

# 혹은 조건문을 사용해서 해결할 수도 있습니다.
num = 3
for i in range(1, 10) :
    if i % 2 == 1 :
        print (num, "x", i, " = ", num * i)



# 168
# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# 합 : 55
print('\n168')

# my code
num = 0
for i in range(1, 11):
  num = num + i
print(num)

# the answer
# hab 이라는 변수에 0을 저장하고, for 문을 통해 모든 값에 대해 누적합니다.
hab = 0
for i in range(1, 11):
    hab += i
print ("합 :", hab)

# hab += i 는 아래 코드를 축약해서 작성한 것입니다.
hab = hab + i



# 169
# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# 합: 25
print('\n169')
sum = 0
for i in range(1, 11):
  if i % 2 == 1:
    sum += i
print("합 :", sum)



# 170
# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
print('\n170')

# my code
multi = 0
for i in range(1, 11):
  multi += i * i
  print(multi)

# the answer
result = 1
for i in range(1, 11) :
    result *= i
print(result)

# result *= i 는 아래 코드를 축약해서 작성한 것입니다.
# result = result * i




# 171
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
print('\n171')

# my code
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
  print(i)

# the answer
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(price_list[i])

# len() 함수를 사용하면 price_list 가 변해도 코드의 수정이 필요없습니다.
# 아래가 더 좋은 코드입니다.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])



# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
print('\n172')

# my code
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
  print(i, price_list[i])

# the answer
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)



# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
print('\n173')



