import turtle
radius = int(input('반지름 :'))
rotatecnt = int(input('회전 횟수 :'))

turtle.shape("turtle")
for i in range(rotatecnt):
    turtle.circle(radius)
    turtle.right(360/rotatecnt)
