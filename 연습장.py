# my code
user = input('현재시간:')
user = user.split(':')
minute = user[1]

if minute == '00':
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')
