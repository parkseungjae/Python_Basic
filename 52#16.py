n = 0
s = 0
while True:
    num = int(input("정수:"))
    s += num
    if num < 0:
        s -= num
        continue
    elif num == 0:
        print(f'합 : {s}')
        break
