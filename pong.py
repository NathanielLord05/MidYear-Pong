#sara 
# creating main screen
screen = ---.Screen()
screen.title = ("Play the Pong Game!")
screen.setup(width=900, height = 500)
screen.bgcolor = ("black")

# right paddle
r_paddle = ()
r_paddle.speed(0)
r_paddle.shape("triangle")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=2)


