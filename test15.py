메모 = {1:1, 2:1}
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output
print(f(40))