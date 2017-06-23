import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

  #    draw_square()
  #    draw_circle()
  #    draw_triangle()

    draw_circleof_squares()
    
    window.exitonclick()

def draw_square(some_turtle):

    count = 0
    while(count < 4):
        some_turtle.forward(100)
        some_turtle.right(90)
        count = count + 1
"""
def draw_circle():
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)

def draw_triangle():
    
    nemo = turtle.Turtle()
    nemo.shape("arrow")
    nemo.color("green")
    nemo.speed(1)

    swim = 0
    while(swim < 3):
        nemo.forward(100) 
        nemo.left(120)
        swim = swim + 1
"""

def draw_circleof_squares():
    ccount = 0
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(5)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
                      
draw_shapes()


