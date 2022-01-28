# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
print('101')
print('파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?')
print('bool type')



# 102
# 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
print('102')
print('아래 코드의 출력 결과를 예상하라')
print('print(3 == 5)')
print('False')



# 103
# 아래 코드의 출력 결과를 예상하라
# print(3 < 5)
print('103')
print('아래 코드의 출력 결과를 예상하라')
print('print(3 < 5)')
print('True')



# 104
# 아래 코드의 결과를 예상하라.
# x = 4
# print(1 < x < 5)
print('104')
print('아래 코드의 결과를 예상하라.')
print('print(1 < x < 5)')
print('True')



# 105
# 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))
print('105')
print('아래 코드의 결과를 예상하라.')
print('print ((3 == 3) and (4 != 3))')
print('True')



# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)
print('106')
print('아래 코드에서 에러가 발생하는 원인에 대해 설명하라.')
print('print(3 => 4)')

# my answer
print('3 => 4 가 아니라 3 >= 4 이다.')

# the answer
print('지원하지 않는 연산자입니다.')



# 107
# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World")
print('107')
print('아래 코드의 출력 결과를 예상하라.')
print('if 4 < 3:')
print('     print("Hello World")')

# my answer
print('')

# the answer
print('조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.')



# 108
# 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
print('108')
print('아래 코드의 출력 결과를 예상하라.')
print('if 4 < 3:')
print('     print("Hello World.")')
print('else:')
print('     print("Hi, there.")')
print('Hi, there.')



# 109
# 아래 코드의 출력 결과를 예상하라
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
print('109')
print('아래 코드의 출력 결과를 예상하라.')
print('if True :')
print('    print ("1")')
print('    print ("2")')
print('else :')
print('    print("3")')
print('print("4")')
print('1')
print('2')
print('4')



# 110
# 아래 코드의 출력 결과를 예상하라
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
print('110')
print('아래 코드의 출력 결과를 예상하라.')

# my answer
print('1')
print('2')
print('5')

# the answer
print('3')
print('5')



# 111
# 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# >> 안녕하세요
# 안녕하세요안녕하세요
print('111')

# my code
# a = str(input())
# if a = '안녕하세요':
#     print('안녕하세요안녕하세요')
# else:
#     print('아닙니다')

# the answer
user = input("입력:")
print(user * 2)



# 112
# 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# >> 숫자를 입력하세요: 30
# 40
print('112')

# my code
user = int(input('입력:'))
print(user+10)

# the answer
user = input("숫자를 입력하세요: ")
print(10 + int(user))


# 113
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# >> 30
# 짝수
print('113')

# my code
user = input("숫자를 입력하세요: ")
if int(user)/2 == 0:
    print('짝수')
elif int(user)/2 != 0:
    print('홀수')

# the answer
user = input("")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")



# 114
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255
print('114')

# my code
user = input('숫자를 입력하세요: ')
if int(user)+20 <= 255:
    print(int(user)+20)
elif int(user)+20 > 255:
    print(255)



# the answer
user = input("입력값: ")
num = 20 + int(user)
if num > 255:
    print(255)
else:
    print(num)

