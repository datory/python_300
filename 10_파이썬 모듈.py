# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
print('\n241')

# the answer
import datetime

now = datetime.datetime.now()
print(now)



# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print('\n242')

# my answer
import datetime

now = datetime.datetime.now()
print(type(now))

# the answer
import datetime

now = datetime.datetime.now()
print(now, type(now))