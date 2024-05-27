from turtle import Screen
import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=500)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)


