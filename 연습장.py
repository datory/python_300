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