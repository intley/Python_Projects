#Program attempts to draw a flower using the turtle function
import turtle

def flower_line():
    window = turtle.Screen()
    window.bgcolor("white")

    dave = turtle.Turtle()
    dave.color("blue")
    dave.shape("turtle")
    dave.speed(2)

    for i in range(1,100):
        dave.forward(100)
        dave.right(10)

flower_line()
