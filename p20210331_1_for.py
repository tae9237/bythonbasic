#반복문:for
# for x in[21,21,2,2,3,3,3,1,1]:
#     print('plython')

# data=['홍길동','세종','영조']
# for x in data:
#     print(x)
# for x in [0,1,2,]:
#     print(data[x])

#실습)0~9출력

# data=[0,1,2,3,4,5,6,7,8,9]
# for x in data:
#     print(x)

#정수를 생성
#range(start,stop,step)
# print(list(range(0,50,10)))
# print(list(range(50)))#stop
# print(list(range(0,50)))#start,stop

# for x in range(0,100):
#     print(x)

#합계를 구하기
#1부터 1까지 출력
# s=0#합계를 저장할 변수
# for x in range(1,11):
#     s=x+s #s+=x
#     print(s)

# for x in range(1,11):
#     s=x+s
# print(s) # 최종값만 나오게

#실습)사용자에게 마지막숫자를 입력받아 1부터 그수까지 더하기
# s=0
# l=int(input('마지막숫자?'))
# for x in range(1,l+1):
#     s+=x
# print(s)
#break
#실습)1부터 100까지 합이 2000이 넘을때의 수를 출력
# s=0
# for x in range(1,101):
#     s+=x
#     if s>2000:
#         break #반복문을 종료할 때
# print(x,s)

#실습)바보라는 글자가 발견되면 강퇴
# data=['안녕','반가워','방가','오늘만나']
# bad=['바보','멍청이']
# for x in data:
#     print(x)
#     if x in bad:
#         print('강퇴')
#         break

# for x in data:
#     print(x)
#     if x=='바보':
#         print('강퇴')
#         break

# for x in data:
#     print(x)
#     if x in bad:
#         print('강퇴')
#         break
# else:#for문이 정상수행했다면(break문을 실행하지 않았을 때)
#     print('바른말사용')

#continue:계속진행
# data=[9,1,40,20,31,22]
# for x in data:
#     if x%2==1: continue
#     print(x)

#실습)모든 점수 60이상 합격
# data=[65,45,95,55,70]
# data=input('점수는?').split()
# print(data)
# data=map(int , data)
# for x in data:
#     print(x)
#     if x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

# for x in data:
#     print(x)
#     if  x<60:
#         print('불합격')
#         break
# else:
#     print('합격')

#실습)모든점수 합계가 300이상 합격
# data=[65,45,95,55,70]
# s=0
# for x in data:
#     s+=x
#     if s>300:
#         print('합격')
#         break
# else:
#     print('불합격')

