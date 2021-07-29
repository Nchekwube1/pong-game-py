import turtle
wn = turtle.Screen()
wn.title("Pong game by @FrancisUnekwe")

wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)





paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("lightblue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lightblue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lightblue")
ball.penup()
ball.goto(0,0)
ball.dx=.1
ball.dy=.1


def pad_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def pad_a_dw():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    
def pad_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def pad_b_dw():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(pad_a_up,"w")
wn.onkeypress(pad_a_dw,"x")
wn.onkeypress(pad_b_up,"Up")
wn.onkeypress(pad_b_dw,"Down")









while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1  