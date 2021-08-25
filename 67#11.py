s = int(input('시작 :'))
h = int(input('높이 :'))
for i in range(1,h+1):
    for j in range(1,h+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print((s+j-1)%10,end=" ")
    print()
