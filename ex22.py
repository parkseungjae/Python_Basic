import datetime
now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("현재 {}월 봄".format(now.month))
if 6 <= now.month <= 9:
    print("현재 {}월 여름".format(now.month))
if 10 <= now.month <= 11:
    print("현재 {}월 가을".format(now.month))
if 12 <= now.month <= 2:
    print("현재 {}월 겨울".format(now.month))
