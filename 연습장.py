# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
print('\n124')
user1 = input('input number1: ')
user2 = input('input number2: ')
user3 = input('input number3: ')
if user1 >= user2 and user1 >= user3:
    print(user1)
elif user2 >= user1 and user2 >= user3:
    print(user2)
elif user3 >= user1 and user3 >= user2:
    print(user3)

