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

# my code
import datetime

now = datetime.datetime.now()
print(type(now))

# the answer
import datetime

now = datetime.datetime.now()
print(now, type(now))



# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
print('\n243')

# my code
import datetime

now = datetime.datetime.now()


# the answer
import datetime

now = datetime.datetime.now()

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)


    
# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요.
# strftime 메서드를 사용하세요.
# 18:35:01
print('\n244')
import datetime
now = datetime.datetime.now()
print(now.strftime('%H:%M:%S'))



# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다.
# "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
print('\n245')

# my code
# import datetime
# print(datetime.datetime.strptime("2020-05-04"))


# the answer
import datetime

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))



# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
print('\n246')

# my code
import time
import datetime
from time import time
from time import sleep

# time()
# print('before')
# sleep(3.5)
# print('after')


# the answer
# import time
# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

