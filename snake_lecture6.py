import turtle
import time
import random

window = turtle.Screen()

window.addshape('gold.gif')
window.addshape('digging.gif')
window.addshape('godown.gif')
window.addshape('goleft.gif')
window.addshape('goright.gif')
window.addshape('goup.gif')
window.addshape('goldicon.gif')

window.title('Snakey')
window.bgcolor('yellow')
window.setup(width=800, height=800)

window.tracer(0)

goldIcon = turtle.Turtle()
goldIcon.shape('goldicon.gif')
goldIcon.penup()
goldIcon.goto(200, -350)

#1 create snake head
head = turtle.Turtle()
head.shape('godown.gif')
head.color('black')
head.penup()
head.goto(0, 100)
head.speed(0)
head.direction = 'stop'

score = 0
scoreT = turtle.Turtle()
scoreT.penup()
# 2
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.shape('goup.gif')
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
        head.shape('godown.gif')

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
        head.shape('goleft.gif')

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
        head.shape('goright.gif')

# 4
def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

# 3
window.listen()
window.onkey(go_up, 'w')
window.onkey(go_down, 's')
window.onkey(go_left, 'a')
window.onkey(go_right, 'd')


# 5

food = turtle.Turtle()
food.shape('gold.gif')
food.color('brown')
food.penup()
food.shapesize(1.0, 1.0)
food.goto(0, 0)


segments = []

delay = 0.1

def boundary():
    global head

    if head.xcor() > 400 or head.xcor() < -400:
        head.goto(0,0)
        head.direction = 'stop'



while True:

    # 6
    # if len(segments) > 1:
    #     for i in range(len(segments) -1, 0, -1):
    #         segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    # if len(segments) > 0:
    #     firstSegment = segments[0]
        # firstSegment.goto(head.xcor(), head.ycor())
    
    if head.distance(food) < 21:
        
        score = score +1
        scoreT.clear()
        scoreT.ht()
        scoreT.goto(240, -365)
        scoreT.write(str(score), font=("Verdana", 25, "normal"))

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        head.shape('digging.gif')
        window.update()
        time.sleep(0.4)

        if head.direction == 'up':
            head.shape('goup.gif')
        elif head.direction == 'down':
            head.shape('godown.gif')
        elif head.direction == 'left':
            head.shape('goleft.gif')
        else:
            head.shape('goright.gif')
        # # 7
        # for i in range(25):
        #     new_segment = turtle.Turtle()
        #     new_segment.speed(0)
        #     new_segment.shape('square')
        #     new_segment.color('white')
        #     new_segment.penup()
        #     segments.append(new_segment)

        
    move()
    boundary()
    time.sleep(delay)
    window.update()

turtle.done()