# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
print('051 리스트 생성')
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)




# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 '배트맨'을 추가하라.
print('052 리스트에 원소 추가')
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append('배트맨')
print(movie_rank)




# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. '슈퍼맨'을 '닥터 스트레인지'와 '스플릿' 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
print('053 리스트에 원소 추가')
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)




# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
print('054 리스트에 원소 삭제')

# my code
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
print(movie_rank)

# the answer
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)



# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
print('055 리스트에 원소 삭제')

# my code
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')
print(movie_rank)

# the answer
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)



# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
print('056 리스트에 원소 병합')

# my code
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang1.extend(lang2)
print(lang1)

# the answer
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)



# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1
print('057 리스트 최대값 최소값 출력')

# my code
nums = [1, 2, 3, 4, 5, 6, 7]
print(min(nums))
print(max(nums))

# the answer
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))



# 058
# 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15
print('058 리스트의 합 출력')

# my code
nums = [1, 2, 3, 4, 5]
print("sum: ", sum(nums))

# the answer
nums = [1, 2, 3, 4, 5]
print(sum(nums))




# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print('059 리스트 개수')
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))



# 060
# 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0
print('060 리스트 평균')
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)



# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print('061 리스트 슬라이싱')
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])



# 062
# 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]
print('062 리스트 홀수 슬라이싱')

# my code
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

# the answer
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])



# 063
# 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]
print('063 리스트 짝수 슬라이싱')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])



# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
print('064 리스트 역방향 슬라이싱')
nums = [1, 2, 3, 4, 5]
print(nums[::-1])




# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print('065 리스트 출력')
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])




# 066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print('066 join 메서드')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))



# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print('067 join 메서드')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))



# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print('068 join 메서드')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))



# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']
print('069 문자열 split 메서드')
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)



# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]
print('070 리스트 정렬')
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
