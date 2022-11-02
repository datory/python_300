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



# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
print('\n213')

# my answer
# String 은 ""를 붙여줘야 한다.

# the anwer
# 함수에 정의와 다르게 함수를 호출하고 있다.
# 함수를 호출할 때 하나의 파라미터를 입력해야한다.



# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int
print('\n214')

# my answer
# 함수를 호출할때 두번째 파라미터가 int라서

# the anwer
# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다.
# 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다.



# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
print('\n215')

# my code
def print_with_smile(a):
    print(a + ':D')

print_with_smile('hello')

# the answer
def print_with_smile (string) :
    print (string + ":D")



# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
print('\n216')

# my code
print_with_smile('안녕하세요')



# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
print('\n217')

# my code
def print_upper_price(a):
    print(a * 0.3)
print_upper_price(10)

# the answer
def print_upper_price(price) :
    print(price * 1.3)
print_upper_price(10)



# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
print('\n218')

# my code
def print_sum(a, b):
    print(a + b)
print_sum(1, 1)



# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
print('\n219')

# my code
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
print_arithmetic_operation(3, 4)

# the answer
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
print_arithmetic_operation(3, 4)



# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라.
# 단 if 문을 사용해서 수를 비교하라.
print('\n220')

# my code
def print_max(a, b, c):
    if a < b and a< c:
        print(a)
    elif b < a and b < c:
        print(b)
    else :
        print(c)

print_max(3, 2, 1)


# the answer
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)

print_max(3, 2, 1)


print(max(3, 2, 1))



# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# print_reverse("python")
# nohtyp
print('\n221')

def print_reverse(a):
    print(a[::-1])
print_reverse('python')



# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# print_score ([1, 2, 3])
# 2.0
print('\n222')

# my code
def print_score(a, b, c):
    print((a + b + c) / 3)
print_score(1, 2, 3)

# the answer
def print_score(score_list) :
    print(sum(score_list)/len(score_list))
print_score([1, 2, 3])



# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
print('\n223')

# my code
def print_even(a):
    for i in a:
        if i % 2 == 0:
            print(i)
print_even([1, 2, 3, 4])

# the answer
def print_even (my_list) :
    for v in my_list :
        if v % 2 == 0 :
            print(v)
print_even([1, 2, 3, 4])



# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
print('\n224')

# my code
def print_keys(a):
    for k in a.keys():
        print(k)
print_keys({"이름":"김말똥", "나이":30, "성별":0})

# the answer
def print_keys(dic):
    for keys in dic.keys():
        print(keys)
print_keys({"이름":"김말똥", "나이":30, "성별":0})



# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
print('\n225')

# my code
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(a, b):
    print(my_dict[b])
print_value_by_key  (my_dict, "10/26")


# the answer
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key (my_dict, key) :
    print(my_dict[key])
print_value_by_key  (my_dict, "10/26")



# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
print('\n226')

# my code
def print_5xn(string):
    print(string[0:5])
    print(string[5:10])
print_5xn("아이엠어보이유알어걸")

# the answer
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])
print_5xn("아이엠어보이유알어걸")



# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸
print('\n227')

# my code
# def print_mxn(string, num):



# the answer
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])
print_mxn("아이엠어보이유알어걸", 3)



# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라.
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000
print('\n228')

# my code
def calc_monthly_salary1(annual_salary):
    average = annual_salary / 12
    print(int(average))
calc_monthly_salary1(12000000)

# the answer
def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay
    print(monthly_pay)
calc_monthly_salary(12000000)



# 229
# 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)
print('\n229')

# my code
# 왼쪽: a=100
# 오른쪽: b=200

# the answer
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

