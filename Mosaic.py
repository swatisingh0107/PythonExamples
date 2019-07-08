#Fractal
import turtle

def draw_triangle(some_turtle):
    some_turtle.fillcolor("green")
    some_turtle.begin_fill()
    for i in range(1,4):
        some_turtle.forward(20)
        some_turtle.right(120)
    some_turtle.end_fill()

def draw_pyramid(pturtle):
     for i in range (1,4):
        count=1
        while count<=4:
            draw_triangle(pturtle)
            pturtle.forward(20)
            count=count+1
        pturtle.left(-120)


window=turtle.Screen()
window.bgcolor("white")
brad=turtle.Turtle()
brad.shape("turtle")
brad.color("blue")
brad.speed(10)
brad.right(-60)
draw_pyramid(brad)

brad.forward(80)
draw_pyramid(brad)
brad.right(60)
draw_pyramid(brad)


brad.left(-60)
brad.forward(80)
brad.left(120)


draw_pyramid(brad)

#brad.left(120)
#brad.backward(40)


window.exitonclick()
