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

# the answer
for i in range(len(price_list)):
    print(3 - i, price_list[i])

# 3이라는 숫자보다는 일반적인 형태로 아래와 같이 코딩하는게 좋습니다.
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])



# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
print('\n174')

# the answer
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])



# 175
# my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
print('\n175')

# # my code
my_list = ["가", "나", "다", "라"]
# for i in range(4):
#   print(my_list[i], my_list[i+1])


# the answer
# 어렵다면 한단계씩 생각해 봅시다.
# for문을 사용하지 않고 인덱싱만을 사용해서 코드를 작성해보면 인덱스간의 규칙관계가 눈에 들어옵니다.
# 같은 행에 있는 두 개의 데이터는 인덱스가 +1 차이납니다. 또한 행이 증가할 때마다 인덱스가 +1 씩 증가합니다.
print(my_list[0], my_list[1])
print(my_list[1], my_list[2])
print(my_list[2], my_list[3])

# 분석한 규칙을 바탕으로 반복문을 작성합시다.
# 아래는 첫 열 "가 나 다" 를 한 라인에 하나씩 출력하는 코드입니다.
# for 문이 인덱스를 0, 1, 2 차례로 바인딩하고 인덱싱을 사용해 값을 출력합니다.
for i in [0, 1, 2]:
    print(my_list[i])

# 한 행에 두 개의 데이터를 출력하고 싶기 때문에 이전 코드의 print 문에 출력하고 싶은 데이터를 추가합니다.
# 같은 행의 두 데이터는 인덱스 차이가 +1 이라는 것을 잊지마세요.
# i가 0일 때는 0, 1 위치의 값이 출력됩니다.
# i가 1일 때는 1, 2 위치의 값이 출력됩니다.
# * i가 2일 때는 2, 3 위치의 값이 출력됩니다.
for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1])

# 위의 코드를 사용해도 원하는 출력값을 얻을 수 있지만 아래는 코드를 보다 일반적인 형태로 변경했습니다.
# len 함수를 사용한 것을 눈여겨 보세요.
for i in range( len(my_list) - 1 ) :
  print(my_list[i], my_list[i+1])

# 아래와 같이 작성해도 됩니다. 인덱스를 갖고 노는 겁니다.
# for문을 단계별로 풀어 써가며 확인해보세요.
for i in range( 1, len(my_list) ) :
  print(my_list[i-1], my_list[i])



# 176
# 리스트를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마
print('\n176')
my_list = ["가", "나", "다", "라", "마"]
for i in range(2, len(my_list) ) :
  print(my_list[i-2], my_list[i-1], my_list[i])



# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
print('\n177')
my_list = ["가", "나", "다", "라"]
for i in reversed(range(1, len(my_list))) :
  print(my_list[i], my_list[i-1])



# 178
# 리스트에는 네 개의 정수가 저장되어 있다.
# 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다.
# 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
# 100
# 200
# 400
print('\n178')
my_list = [100, 200, 400, 800]
for i in range(0, len(my_list)-1):
  print(my_list[i+1]-my_list[i])



# 179
# 리스트에는 6일 간의 종가 데이터가 저장되어 있다.
# 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# my_list = [100, 200, 400, 800, 1000, 1300]
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다.
# 두 번째 줄에는 200, 400, 800의 평균값이 출력된다.
# 같은 방식으로 나머지 데이터의 평균을 출력한다.
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333
print('\n179')
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(0, len(my_list)-2):
  print((my_list[i]+my_list[i+1]+my_list[i+2])/3)



# 180
# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다.
# 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
print('\n180')

# my code
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
for i in range(0, len(low_prices)):
  print(high_prices[i] - low_prices[i])

# the answer
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)

# 181
# 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
# 101호	102호
# 201호	202호
# 301호	302호
print('\n181')

# my code
list_1 = ['101호', '102호']
list_2 = ['201호', '202호']
list_3 = ['301호', '302호']
print(list_1)
print(list_2)
print(list_3)

# the answer
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]
print(apart)



# 182
# 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
# 시가	종가
# 100	80
# 200	210
# 300	330
print('\n182')
stock = [ ['시가', 100, 200, 300], ['종가', 80, 210, 330] ]
print(stock)



# 183
# 아래 표를 stock 이름의 딕셔너리로 표현하라.
# 시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# 시가	종가
# 100	80
# 200	210
# 300	330
print('\n183')

# my code
stock = {'시가':'종가', 100:80, 200:210, 300:330}
print(stock)

# the answer
stock = {"시가": [100, 200, 300], "종가": [80, 210, 330] }
print(stock)



# 184
# 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라.
# 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다.
# 첫 열이 날짜이다.
# 10/10	80	110	70	90
# 10/11	210	230	190	200
print('\n184')
stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200] }
print(stock)



# 185
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
print('\n185')

# my code
apart = [ [101, 102], [201, 202], [301, 302] ]
print(apart[0][0], "호")
print(apart[0][1], "호")
print(apart[1][0], "호")
print(apart[1][1], "호")
print(apart[2][0], "호")
print(apart[2][1], "호")

# the answer
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")



# 186
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호
print('\n186')

# my code
apart = [ [101, 102], [201, 202], [301, 302] ]
l_apart = apart.reverse()
for row in apart:
    for col in row:
        print(col, "호")

# the answer
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row:
        print(col, "호")



# 187
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호
print('\n187')
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")



# 188
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# -----
# 102 호
# -----
# 201 호
# -----
# 202 호
# -----
# 301 호
# -----
# 302 호
# -----
print('\n188')

# my code
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
  for col in row:
    print(col, '호')
    print('-----')

# the answer
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print("-" * 5)



# 189
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----
print('\n189')

# my code
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    print("-" * 5)
    for col in row:
        print(col, "호")


# the answer
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")



# 190
# 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----
print('\n190')

# my code
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print("-----")

# the answer
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
print("-" * 5)



# 191
# data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# ...
print('\n191')

# my code
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for price in data:
  for commission in price:
    print(commission, ".", commission*0.014)

# the answer
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for column in line:
        print(column * 1.00014)


# 192
# 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# 1980.2772
# ----
# 7501.05
# 2050.2870000000003
# 2050.2870000000003
# 1980.2772
# ----
# 15452.163
# 15052.107
# 15552.177
# 14902.086000000001
# ----
print('\n192')

# my code
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for price in data:
  for commission in price:
    print(commission, ".", commission*0.014)
  print('----')

# the answer
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for line in data:
    for column in line:
        print(column * 1.00014)
    print("----")



# 193
# 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
# >> print(result)
# [2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]
print('\n193')

# my code
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for line in data:
    for column in line:
        print(column * 1.00014)
    print("----")
print(result)

# the answer
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)



# 194
# 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
# >> print(result)
# [
#  [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
#  [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
#  [15452.163, 15052.107, 15552.177, 14902.086000000001]
# ]
print('\n194')

# my code
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)

# the answer
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)


# 195
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
# 화면에 종가데이터를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 190
# 310
print('\n195')

# my code
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for x in ohlc:
#     for y in x:
#         print(y[3])

# the answer
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])



# 196
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
# 종가가 150원보다 큰경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 190
# 310    
print('\n196')

# my code
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3] >= 150:
        print(row[3])

# the answer
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if (row[3] > 150):
        print(row[3])



# 197
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
# 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 310
print('\n197')

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if (row[3] >= row[0]):
        print(row[3])



# 198
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
# 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# >> print(volatility)
# [40, 30, 10]
print('\n198')

# my code
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for row in ohlc[1:]:
    volatility.append(row[1]-row[2])
print(volatility)

# the answer
# range 구문을 사용해서도 문제를 풀 수 있습니다.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in range(1, len(ohlc)):
    volatility.append(ohlc[i][1]-ohlc[i][2])
print(volatility)



# 199
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다.
# 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다.
# 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
# 10
print('\n199')
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[0] < row[3]:
        print(row[1] - row[2])



# 200
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다.
# 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.
# 0
print('\n200')

# my code
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
myList = []
del sum
for row in ohlc[1:]:
    myList.append(row[3] - row[0])
listSum = sum(myList)
print(listSum)

# the answer
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)
