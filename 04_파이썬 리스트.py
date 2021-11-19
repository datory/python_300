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


