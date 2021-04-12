#모듈
# import time
# print(time.localtime().tm_year,'년', end=' ',sep='')
# print(time.localtime().tm_mon,'월', end=' ',sep='')
# print(time.localtime().tm_mday,'일',sep='')

# from _datetime import datetime
# now=datetime.now()
# print(now)
# now.strftime(('%Y-%m-%d %H:%ML%S'))


#sleep함수:프로그램 실행 속도를 제어
# import time
# print('시작')
# time.sleep(3)
# print('3초지남')

#timer 만들기
# import time
# s=int(input('몇초?'))
# print('타임시작')
# for x in range(1,s+1):
#     time.sleep(1)
#     print(x,'초')
# print('타임종료')

#난수모듈
# import random
# awin=0
# bwin=0
# a=random.randint(1,6)
# b=random.randint(1,6)
# print('나:',a,'너:',b)
# if a>b:
#     print('나 승')
# elif a<b:
#     print('너 승')
# else:
#     print('무승부')

#samle()
# import random
# print(random.sample(range(1,46),6))

#choice()
# print(random.choice(['가위','바위','보']))

#shuffle():섞는다
# data=[1,2,3,4,5]
# random.shuffle(data)
# print(data)

# import turtle

# turtle.shape('turtle')
# turtle.color('blue')
# for x in range(4):
#     turtle.forward(300)
#     turtle.right(500)
# turtle.done()

