import time
#특정시간 대기 while 문
i = time.time()
while i + 5 > time.time():
    pass
print("exit")