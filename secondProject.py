import turtle
import tkinter as tk

def draw_heart(turt):
    turt.fillcolor('red')
    turt.begin_fill()
    turt.left(179)
    turt.forward(113)
    turt.circle(-90,180)
    turt.setheading(60)
    turt.circle(-90,180)
    turt.forward(112)
    turt.end_fill()

def write_text(turt):
    turt.penup()
    turt.setpos(-70,70)
    turt.pendown()
    turt.color('White')
    turt.write( "HaPpY BiRtHdAy",align ='center',font=('italic',16,'bold'))

def main():
    window = turtle.Screen()
    window.bgcolor('black')
    my_turtle = turtle.Turtle()
    my_turtle.speed(2)
    draw_heart(my_turtle)
    write_text(my_turtle)
    window.mainloop()

if __name__=="__main__":
    main()