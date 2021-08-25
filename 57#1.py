import sys
num=[8,7,3,2,9,4,1,6,5]

maxnum=-sys.maxsize-1
minnum=sys.maxsize
for i in num:
    if maxnum < i:
        maxnum=i
    if minnum > i:
        minnum=i
print("최댓값 :",maxnum)
print("최솟값 :",minnum)