# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# 실행 예
# p t
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210

# my code
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
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4], sep="")

# the answer
stinstring = "홀짝홀짝홀짝"
print(string[::2])


