import turtle

def initials_turtle():
    window = turtle.Screen()
    window.bgcolor("white")

    draw_r()
 #   draw_gap()
    draw_r2()

    window.exitonclick()

def draw_r():
    rr = turtle.Turtle()
    rr.shape("turtle")
    rr.color("blue")
    rr.speed(5)
    rr.forward(100)
    rr.right(90)
    rr.forward(100)
    rr.right(90)
    rr.forward(100)
    rr.left(90)
    rr.forward(100)
    rr.right(180)
    rr.forward(200)
    rr.right(180)
    rr.forward(100)
    rr.left(45)
    rr.forward(135)

def draw_r2():
    rr = turtle.Turtle()
    rr.shape("turtle")
    rr.speed(5)

    rr.color("blue")
    rr.forward(100)
    rr.color("white")
    rr.forward(50)
    rr.color("blue")
    rr.forward(100)
    rr.right(90)
    rr.forward(100)
    rr.right(90)
    rr.forward(100)
    rr.left(90)
    rr.forward(100)
    rr.right(180)
    rr.forward(200)
    rr.right(180)
    rr.forward(100)
    rr.left(45)
    rr.forward(135)
    
initials_turtle()
