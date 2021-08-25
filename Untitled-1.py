a = int(input("정수1 : "))
b = int(input("정수2 : "))
c = str(input("연산자: "))
def calc(num, num2, ca):
    if(ca == [*,-,/,+,' ']):
        if(a>b):
            num = a
            num2 = b
            ca = c
            print('num' + 'ca' + 'num2')
        elif(b>a):
            num = b
            num = a
            ca = c
            print('num' + 'ca' + 'num2')
        elif(num == -99):
            num = a
            print("프로그램 종료")
        else :
            num = a
            num2 = b
            ca = c
            print('num' + 'ca' + 'num2' + "=" + "연산자오류")

