import turtle


# functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y <= dispHeight // 2 - 70:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y >= 70 - dispHeight // 2:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y <= dispHeight // 2 - 70:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y >= 70 - dispHeight // 2:
        y -= 20
    paddle_b.sety(y)


# define ball boundaries
def bound_ball():
    x = ball.xcor()
    y = ball.ycor()
    if y > dispHeight // 2 or y < -(dispHeight // 2):
        ball.dy *= -1
    if x > dispWidth // 2:
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_a.score += 1
        pen.clear()
        pen.write(arg="Player A:{}\t\t\t Player B:{}".format(paddle_a.score, paddle_b.score), align="center",
                  font=("courier", 16, "bold"))
    if x < -(dispWidth // 2):
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_b.score += 1
        pen.clear()
        pen.write(arg="Player A:{}\t\t\t Player B:{}".format(paddle_a.score, paddle_b.score), align="center",
                  font=("courier", 16, "bold"))


# function to detect collision
def check_bounce():
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if (-(dispWidth // 2 - 40) <= ball_x <= -(dispWidth // 2 - 50)) and (paddle_a.ycor() + 50 > ball_y >
                                                                         paddle_a.ycor() - 50):
        ball.setx(-(dispWidth // 2 - 50))
        ball.dx *= -1
    elif (dispWidth // 2 - 50) <= ball_x <= (dispWidth // 2 - 40) and (paddle_b.ycor() + 50 > ball_y >
                                                                       paddle_b.ycor() - 50):
        ball.setx(dispWidth // 2 - 50)
        ball.dx *= -1


def kill_game():
    global isAlive
    isAlive = False


def pause_game():
    global isPaused
    isPaused = not isPaused


dispWidth = 800
dispHeight = 600

# Spread the carousel
gameScreen = turtle.Screen()
gameScreen.title("Ping Pong")
gameScreen.bgcolor('black')
gameScreen.setup(height=dispHeight, width=dispWidth)
gameScreen.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.penup()
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto((-((dispWidth // 2) - 30), 0))
paddle_a.score = 0

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.penup()
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto((dispWidth // 2) - 30, 0)
paddle_b.score = 0

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color('white')
pen.goto(0, dispHeight // 2 - 70)
pen.write(arg="Player A:{}\t\t\t Player B:{}".format(paddle_a.score, paddle_b.score), align="center",
          font=("courier", 16, "bold"))

# Key Bindings
gameScreen.listen()
gameScreen.onkeypress(paddle_a_up, "w")
gameScreen.onkeypress(paddle_a_down, "s")
gameScreen.onkeypress(paddle_b_up, "Up")
gameScreen.onkeypress(paddle_b_down, "Down")
gameScreen.onkeypress(pause_game, "space")
gameScreen.onkeypress(kill_game, "Escape")

# main Game loop
if __name__ == '__main__':
    isAlive = True
    isPaused = False
    while isAlive:
        # Ball Movement
        if not isPaused:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            # ball.sety(0)
            # ball.setx(350)
            bound_ball()
            check_bounce()
        gameScreen.update()
