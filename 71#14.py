
t = 0
n = 0
while True:
    n = n + 1
    t = pow(2,n)
    
    print(f'{n}번 접으면 {t}mm')
    if t >= 100000:
        print(f'횟수 : {n} 두께 : {t}')
        break