import turtle
turtle.shape("turtle")
radius = int(input('반지름 :'))
rotatecnt = int(input('회전 횟수 :'))
distance = int(input('이동 :'))

for i in range(rotatecnt):
    turtle.circle(radius)
    turtle.up()
    turtle.forward(radius*distance)
    turtle.down()