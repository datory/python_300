# 201
# "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
print('\n201')

# my code
print_coin = '비트코인'
print(print_coin)

# the answer
def print_coin():
    print("비트코인")
print_coin()



# 202
# 201번에서 정의한 함수를 호출하라.
print('\n202')
print_coin()



# 203
# 201번에서 정의한 print_coin 함수를 100번 호출하라.
print('\n203')

# my code
num = 100
for x in range(num):
    print_coin()

# the answer
for i in range(100):
    print_coin()



# 204
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
print('\n204')

def print_coin_100():
    for i in range(100):
        print('비트코인')
print_coin_100()



# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.

# hello()
# def hello():
#     print("Hi")

# 실행 예
# NameError: name 'hello' is not defined
print('\n205')

# my answer
# hell() 함수를 먼저 정의안하고 불러와서 에러가 뜬다.

# the answer
# 함수가 정의되기 전에 호출되어서 에러가 발생합니다.



# 206
# 아래 코드의 실행 결과를 예측하라.

# def message() :
#     print("A")
#     print("B")

# message()
# print("C")
# message()
print('\n206')

# my answer
# A
# B
# C
# A
# B



# 207
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message() :
#     print("B")
# print("C")
# message()
print('\n207')

# my answer
# A
# C
# B



# 208
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
print('\n208')

# my answer
# A
# C
# B
# E
# D



# 209
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()
print('\n209')

# my answer
# B
# A



# 210
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()
print('\n210')

# my answer
# B
# C
# B
# C
# B
# C
# A



# 211
# 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")
print('\n211')

# my answer
# 안녕
# Hi



# 212
# 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)
print('\n212')

# my answer
# 7
# 15


