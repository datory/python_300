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

