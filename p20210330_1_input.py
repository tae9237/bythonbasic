#사용자에게 입력받기
# a=input('이름은?')
# print('입력',a)
#실습
#나이를 입력받아 화면에 출력
#입력한 값은 문자취급
# a = input('나이는?')
# print('당신의 나이는', a, '입니다')
# print('당신의 나이는'+ a +'입니다')
# print('당신의 나이는', a, '입니다',sep='')

#날씨를 입력받아 오늘의 날씨 출력
#예)오늘의 날씨는 맑음
# txt='오늘의 날씨는'
# a=input('날씨?')
# print(txt, a)
# print(txt,a,sep='')

#도움말출력
#helP(print, inpup 등)

#사용자가 입력한 값에 100을 더해서 출력
# a=input('숫자는?')
# a=int(a)#정수로 변환해서 변환해주는 함수
# a=float(a)#실수로 변환해서 변환해주는 함수
# print(a+100)

#실습 두수를 입려받아 사칙연산 프로그램
# a=int(input('첫번 째 수는?'))
# b=int(input('두번 째 수는?'))
# print('두수의 합은',(a+b),'입니다')
# print('%d + %d = %d'%(a,b,a+b))
# print('%d - %d = %d'%(a,b,a-b))
# print('%d * %d = %d'%(a,b,a*b))
# print('%d / %d = %d'%(a,b,a/b))

# data = input('두 수는?')
# print(data.split())
# a=int(data.split()[0])
# b=int(data.split()[1])
# print(a,b)
# print('%d + %d =%d'%(a,b,a+b))
# print(a,'+',b,'=',a+b,sep='')

# data = input('두 수는?').split() #두 수를 분리
# a,b = map(int, data) #data의 각값을 int함수를 적용한후 a,b에 대입
# print(a,'+',b,'=',a+b)

#실습 원의 넓이 구하기
# a= int(input('반지름의 길이는?'))
# a= float(a)
# print('원의 넓이는',a*a*3.14,'입니다')