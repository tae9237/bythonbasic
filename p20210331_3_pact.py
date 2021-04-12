#실습1)
#1)별찍기1
# for x in range(1,7,):
#     print('★'*x)
#2)별찍기2
# for x in range(6,0,-1):
#     print('★'*x)

#3)별찍기3
 # for x in range(1,7):
 #     print('★'*x)

#실습2)구구단 출력
# for x in range(1,10):
#     print('2 * %d=%d'%(x,2*x))

# dan=int(input('단수는?'))
# for x in range(1,10):
#     print('%d * %d = %d'%(dan,x,dan*x))



#실습3)0부터 3의배수 출력
# last=int(input('마지막수는?'))
# for x in range(0,last+1,3):
#      print(x, end='\t')
#
# print()
# for x in range(0,last+1):
#      if x%3==0:
#           print(x,end ='\t')

#실습4)
#1)두수와 기호를 입력받는다
#2)기호에 따라 계산
#3)계속진행여부 입력
# while True:
#      a=input('첫번째수')
#      if a == 'q': break
#      a=int(a)
#      b=int(input('두번째수'))
#      c=input('기호는?')
#
#      if c=='+':
#           print(a+b)
#      elif c=='-':
#           print(a-b)
#      elif c=='*':
#           print(a*b)
#      elif c=='/':
#           print(a/b)
#      else:
#           print('잘못된 기호')


# while True:
#      a=input('첫번째수')
#      if a == 'q': break
#      a=int(a)
#      b=int(input('두번째수'))
#      while True:
#           c=input('기호:')
#           if c in ['+','-','*','/']:
#                break


#실습5)
# dicA={1:94,2:87,3:91,4:75,5:92}
# print(dicA.keys())
# print(dicA.values())
# print(dicA.items())
#
# for x,y in dicA.items():
#     if y>=90:
#         print(x,'번')

#실습6)
#1)사원의 판매수량 입력
#2)히스토그램 그리기
#데이터구조{'홍길동':7,'이순신':3,'김순희':8,'이철수':4}

# data=['홍길동','이순신','김순희','이철수']
# qty={}
# for name in data:
#     qty[name]=int(input(name+'?'))
# print(qty)
# for name,s in qty.items():
#     print(name,'*'*s)

