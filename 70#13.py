d = int(input('단 :'))

for i in range(d,10):
    for j in range(1,10):
        if d == 9:
            print("%d * %d= %d"%(i,j, i*j))
        elif d >= 2 and d <= 8:
            print(d, "*", i, d*i,d+1,"*",i,"=",(d+1)*i)