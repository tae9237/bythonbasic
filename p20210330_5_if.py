#조건문
# a=10
# if a>0:
#     print('양수')
#     print(a)
# else:
#     print('음수')
# print('프로그램 종료')

#실습)회원등급 출력
#a=90보다 크면 good 아니면 try

# a=int(input('점수는?'))
# if a>90:
#     print('good')
# else:
#     print('try')

#실습)비밀번호 체크
#비밀번호 일치하면 '문이열립니다.'
#일치하지 않으면 '다시확인하세요'
# pw='1234' #기존 등록된 비밀번호

# a=input('비밀번호?')
# if pw==a:
#     print('문이열립니다.')
# else:
#     print('다시확인하세요')

#어떤수가 짝수이면 '짝수' 홀수이면 '홀수'
# a=int(input('숫자는?'))
# if a==0:
#     print('아니다')
# elif a%2==0:
#     print('짝수')
# else:
#     print('홀수')

#실습)90 A, 89~80 B, 79~70 C, 69~ 60 D, 59~ F

# a=int(input('학점은?'))
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')

#실습)몸무게와 키를 입력 받아서 비만여부 출력

# a=float(int(input('몸무게?')))
# b=float(int(input('키?')))
# c=(b-100)*0.9
# print('정상체중:',c)
#
# if a<c*0.95:
#     print('저체중')
# elif a<=c*1.05:
#     print('표준')
# else:
#     print('과체중')

#실습)계산기
#두수와 기호를 입력받아 사칙역산(+,-,*,/)를 출력
#30+20=50

# a=int(input('첫번 째 수?'))
# b=int(input('두번 째 수?'))
# c=input('기호는?')
#
# if c=='+':
#     print(a+b)
# elif c=='-':
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=='/':
#     print(a/b)
# else:
#     print('잘못된 기호')