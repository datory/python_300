# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
from posixpath import split


print('\n101')
print('파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?')
print('bool type')



# 102
# 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
print('\n102')
print('아래 코드의 출력 결과를 예상하라')
print('print(3 == 5)')
print('False')



# 103
# 아래 코드의 출력 결과를 예상하라
# print(3 < 5)
print('\n103')
print('아래 코드의 출력 결과를 예상하라')
print('print(3 < 5)')
print('True')



# 104
# 아래 코드의 결과를 예상하라.
# x = 4
# print(1 < x < 5)
print('\n104')
print('아래 코드의 결과를 예상하라.')
print('print(1 < x < 5)')
print('True')



# 105
# 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))
print('\n105')
print('아래 코드의 결과를 예상하라.')
print('print ((3 == 3) and (4 != 3))')
print('True')



# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)
print('\n106')
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
print('\n107')
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
print('\n108')
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
print('\n109')
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
print('\n110')
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
print('\n111')

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
print('\n112')

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
print('\n113')

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
# 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255
print('\n114')

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



# 115
# 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0
print('\n115')
user = input('입력값: ')
num = int(user) - 20
if num < 0:
    print('출력값: 0')
elif num > 255:
    print('출력값: 255')
else:
    print('출력값:', num)



# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다
print('\n116')

# my code
# user = input('현재시간:')
# user = user.split(':')
# minute = user[1]

# if minute == '00':
#     print('정각 입니다.')
# else:
#     print('정각이 아닙니다.')

# the answer
time = input("현재시간: ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")



# 117
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.
print('\n117')

# my code
fruit = ["사과", "포도", "홍시"]
user = input('좋아하는 과일은? ')
if user == fruit[0]:
    print('정답입니다.')
elif user == fruit[1]:
    print('정답입니다.')
elif user == fruit[2]:
    print('정답입니다.')

# the answer
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")



# 118
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
print('\n118')

# my code
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input('투자 종목: ')
if user in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

# the answer
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
종목 = input("종목먕: ")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")



# 119
# 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.
print('\n119')
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('제가 좋아하는 계절은: ')
if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')



# 120
# 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 좋아하는과일은? 한라봉
# 오답입니다.
print('\n120')

# my code
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 과일은? ')
if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# the answer
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")



# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# >> a
# A
# 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다.
# 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다.
# 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
print('\n121')
user = input('알파벳을 입력하세요: ')
if user.islower():
    print(user.upper())
else:
    print(user.lower())



# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100 A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A
print('\n122')

# my code
user = int(input('학점을 입력하세요: '))
if user >= 81 and user <= 100:
    print('grade is A')
elif user >= 61 and user <= 80:
    print('grade is B')
elif user >= 41 and user <= 60:
    print('grade is C')
elif user >= 21 and user <= 40:
    print('grade is D')
elif user >= 0 and user <= 20:
    print('grade is E')
    
# the answer
score = input("score: ")
score = int(score)
if 81 <= score <= 100:
    print("grade is A")
elif 61 <= score <= 80:
    print("grade is B")
elif 41 <= score <= 60:
    print("grade is C")
elif 21 <= score <= 40:
    print("grade is D")
else:
    print("grade is E")



# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
# >> 입력: 100 달러
# 116700.00 원
print('\n123')

# my code
user = input('입력: ')
user = user.split()
print(user)
if user[1] == '달러':
    print(int(user[0])*1167)
elif user[1] == '엔':
    print(int(user[0])*1.096)
elif user[1] == '유로':
    print(int(user[0])*1268)
elif user[1] == '위안':
    print(int(user[0])*171)

# the answer
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")



# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
print('\n124')

# my code
user1 = input('input number1: ')
user2 = input('input number2: ')
user3 = input('input number3: ')
if user1 >= user2 and user1 >= user3:
    print(user1)
elif user2 >= user1 and user2 >= user3:
    print(user2)
elif user3 >= user1 and user3 >= user2:
    print(user3)

# the answer
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)



# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
# 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.
print('\n125')

# my code
user = input('휴대전화 번호 입력: ')
user = user.split('-')
print(user)
if user[0] == '011':
    print('당신은 SKT 사용자입니다.')
elif user[0] == '016':
    print('당신은 KT 사용자입니다.')
elif user[0] == '019':
    print('당신은 LGU 사용자입니다.')
else:
    print('당신은 알수없음 사용자입니다.')

# the answer
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")