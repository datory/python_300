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


