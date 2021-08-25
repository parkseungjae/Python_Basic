score = float(input("학점을 입력해주세요"))

if score == 4.5:
    print("A+")
elif 3.5 <= score < 4.0:
    print("A")
elif 3.0 <= score < 3.5:
    print("B+")
elif 2.5 <= score < 3.0:
    print("B")
elif 2.0 <= score < 2.5:
    print("C+")
elif 1.5 <= score < 2.0:
    print("C")
elif 1.0 <= score < 1.5:
    print("D+")
elif score == 0.0:
    print("F")

