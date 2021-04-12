#내장함수
# data=[1,2,3,4]
# print(sum(data))

#사용자함수 sum정의
#매개변수:리스트, 반환값:합계
# def mysum(data):
#     s=0
#     for x in data:
#         s+=x
#     #print(s)
#     return s
#
#
# data=[1,4,5,6]
# r=mysum(data)
# print('리턴값:',r)

#max함수
# data=[13,51,12,94]
# m=max(data)
# print('가장큰값:',m)
# mi=min(data)
# print('가장작은값:',mi)

#max값 사용자 함수
# data=[13,51,12,94]
# def mymax(data):
#     m=data[0]
#     for x in data:
#         if x > m:
#             m=x
#     return m
# print('가장큰값:',mymax(data))

# def mymin(data):
#     m=data[0]
#     for x in data:
#         if x<m:
#             m=x
#     return m
# print('가장적은값:',mymin(data))

#ord(함수)
#한글은 유니코드체계
# print(ord('A'),len('A'))
# print(ord('가'),len('가'),'가'.encode(),len('가'.encode()))
# print(chr(44032))

#실습)사칙연산 함수
#매개변수 : 두수, 반홥값 : 결과
# def m(a,b):
#     return a+b
# def n(a,b):
#     return a-b
# #리턴값은 한개만 가능
# def f(a,b):
#     return a+b,a-b,a*b#튜플로변환
# print('더하기?',m(10,20))
# print('빼기?',n(20,15))
# print('결과?',f(20,10))

#실습)월급 구하기
# def s(a,b,c):
#     return a/12+b*c
#
# a=10000000
# b=50000
# c=20
# print(s(a,b,c))
