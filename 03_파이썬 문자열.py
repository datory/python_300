# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예
# p t
print("\n021 문자열 인덱싱")
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210

# my code
print("\n022 문자열 슬라이싱")
license_plate = "24가 2210"
print(license_plate[4:])

# the answer
license_plate = "24가 2210"
print(license_plate[-4:])


# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

# my code
print("\n023 문자열 인덱싱")
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4], sep="")

# the answer
stinstring = "홀짝홀짝홀짝"
print(string[::2])


# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예:
# NOHTYP
print("\n024 문자열 슬라이싱")
string = "PYTHON"
print(string[::-1])


# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

# the answer
print("\n025 문자열 치환")
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)


# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222
print("\n26 문자열 다루기")
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)



# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예:
# kr

# my code
print("\n027 문자열 다루기")
url = "http://sharebook.kr"
print(url[-2:])

# the answer
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])



# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
print("\n028 문자열은 immutable")
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment)메서드를 지원하지 않음을 알 수 있습니다.


# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
# my code
# string = 'abcdfe2a354a32a'
# string.replace[a, A]

# the answer
print("\n029 replace 메서드")
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)


# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
print("\n030 replace 메서드")
string = 'abcd'
string.replace('b', 'B')
print(string)



# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# >> a = "3"
# >> b = "4"
# >> print(a + b)
print("\n031 문자열 합치기")
a = "3"
b = "4"
print(a + b)


# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)
print("\n032 문자열 곱하기")
print("Hi" * 3)


# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
# 실행 예:
# --------------------------------------------------------------------------------
print("\n033 문자열 곱하기")
print('-' * 80)


# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예:
# python java python java python java python java
print("\n034 문자열 곱하기")
# my code
t1 = 'python'
t2 = 'java'
print(t1, t2, t1, t2, t1, t2, t1, t2)

# the answer
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)



# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
print("\n035 문자열 출력")
# my code
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: "+name1+" 나이: "+str(age1))
print("이름: "+name2+" 나이: "+str(age2))

# the answer
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
# print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미합니다.



# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("\n036 문자열 출력")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))


# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print("\n037 문자열 출력")
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")



# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
print("\n038 컴마 제거하기")
# my code
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(",", "")))

# the answer
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))



# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
print("\n039 문자열 슬라이싱")
분기 = "2020/03(E) (IFRS연결)"

# my code
print(분기[0:7])

# the answer
print(분기[:7])


# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "
print("\n040 strip 메서드")
# my code
data = "   삼성전자    "
print(data.replace(" ", ""))

data = "   삼성전자    "
print(data.strip())

# the answer
data = "   삼성전자    "
data1 = data.strip()
print(data1)




# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"
print("\n041 upper 메서드")
# my code
ticker = "btc_krw"
print(ticker.upper())

# the answer
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)



# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"
print("\n042 lower 메서드")
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)



# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
print("\n043 capitalize 메서드")

# my code
ticker = "hello"
print(ticker.capitalize())

# the answer
a = "hello"
a = a.capitalize()
print(a)




# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
print("\n044 endswith 메서드")
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))



# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
print("\n045 endswith 메서드")

# the answer
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))





# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
# file_name = "2020_보고서.xlsx"
print("\n046 startswith 메서드")
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))




# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
print("\n047 split 메서드")
a = "hello world"
print(a.split(" "))



# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
print("\n048 split 메서드")
ticker = "btc_krw"
print(ticker.split("_"))



# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"
print("\n049 split 메서드")
date = "2020-05-01"
print(date.split("-"))



# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "
print("\n050 rstrip 메서드")
data = "039490     "
print(data.split())



