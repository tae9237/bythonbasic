#class:객체를 만들기 위한 틀
class Car:
    #속성
    name='아이오닉5'
    n='전기차'
    color='실버'
    pw=False
    #기능
    def power(self):
        pw = not Car.pw

c1=Car()
print(c1.name)
c1.power()
c2=Car()
print(c2.n)
