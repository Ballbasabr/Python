
from turtle import *

def draw_cat():
    cat = Turtle()
    cat.speed(0)
    cat.screen.setup(800, 600)

    # Тело кошки
    cat.penup()
    cat.goto(0, -100)
    cat.pendown()
    cat.color("black")
    cat.begin_fill()
    cat.circle(100)
    cat.end_fill()

    # Голова кошки
    cat.penup()
    cat.goto(0, 0)
    cat.pendown()
    cat.color("gray")
    cat.begin_fill()
    cat.circle(50)
    cat.end_fill()

    # Левое ухо
    cat.penup()
    cat.goto(-35, 50)
    cat.pendown()
    cat.begin_fill()
    cat.goto(-75, 90)
    cat.goto(-15, 90)
    cat.goto(-35, 50)
    cat.end_fill()

    # Правое ухо
    cat.penup()
    cat.goto(35, 50)
    cat.pendown()
    cat.begin_fill()
    cat.goto(75, 90)
    cat.goto(15, 90)
    cat.goto(35, 50)
    cat.end_fill()

    # Левый глаз
    cat.penup()
    cat.goto(-20, 20)
    cat.pendown()
    cat.color("white")
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()

    cat.penup()
    cat.goto(-20, 25)
    cat.pendown()
    cat.color("black")
    cat.begin_fill()
    cat.circle(5)
    cat.end_fill()

    # Правый глаз
    cat.penup()
    cat.goto(20, 20)
    cat.pendown()
    cat.color("white")
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()

    cat.penup()
    cat.goto(20, 25)
    cat.pendown()
    cat.color("black")
    cat.begin_fill()
    cat.circle(5)
    cat.end_fill()

    # Нос
    cat.penup()
    cat.goto(0, 10)
    cat.pendown()
    cat.color("pink")
    cat.begin_fill()
    cat.circle(5)
    cat.end_fill()

    # Рот
    cat.penup()
    cat.goto(0, 10)
    cat.pendown()
    cat.right(90)
    cat.circle(10, 180)
    cat.penup()
    cat.goto(0, 10)
    cat.pendown()
    cat.circle(10, -180)

    # Хвост
    cat.penup()
    cat.goto(-10, 150)
    cat.pendown()
    cat.color("gray")
    cat.pensize(20)
    cat.right(45)
    cat.circle(50, 55)

    cat.screen.exitonclick()
    cat.screen.mainloop()
    
draw_cat()