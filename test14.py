counter = 0
def f(n):
    global counter
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(15))
print(counter)

