
# TODO Do not edit this file directly! Instead, create a new file called
# TODO a03_username.py and copy this code into it!

#################################################################################
# Author: Sarah Keown
# Username: sarahkeown
#
# Assignment:
# Purpose:
# Google Doc Link: https://docs.google.com/document/d/1F9wfattarM5KmVeo90zHmc2OPbv30SzBD70jnOEW99c/edit?usp=sharing
#
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle

wn = turtle.Screen()

def turtle_grass():
    """
    This code has the first turtle draw the background of the picture
    i.e. sky and grass
    """
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("#44C8FA")   #changes background color using Hexadecimal

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.forward(350)
    t.right(90)
    t.forward(150)
    t.right(90)             #makes the grass
    t.pendown()
    t.pensize(200)
    t.pencolor("green")
    for i in [0, 1,]:
        t.forward(700)
        t.left(90)
        t.forward(150)
        t.left(90)
    t.goto(500, -500)


def turtle_house():
    """New Turtle to draw the House"""

    tu = turtle.Turtle()
    tu.speed(0)
    tu.penup()
    tu.goto(-100,100)
    tu.pendown()
    tu.fillcolor("navy")    # house
    tu.begin_fill()
    for x in [0, 1, 2, 3]:
        tu.right(90)
        tu.forward(200)
    tu.end_fill()
    tu.forward(5)
    tu.fillcolor("saddlebrown")   # roof
    tu.begin_fill()
    tu.left(135)
    for t in range(2):
        tu.forward(150)
        tu.left(90)
    tu.left(45)
    tu.forward(150)
    tu.end_fill()
    tu.penup()        #door
    tu.goto(-230,0)
    tu.pendown()
    tu.fillcolor()
    tu.begin_fill()
    for d in [0, 1]:
        tu.forward(50)
        tu.right(90)
        tu.forward(100)
        tu.right(90)
    tu.end_fill()
    tu.penup()
    tu.left(90)   #left side window
    tu.forward(30)
    tu.fillcolor("snow")
    tu.begin_fill()
    for w in range(4):
        tu.forward(50)
        tu.left(90)
    tu.penup()
    tu.right(90)
    tu.forward(55)
    for w in range(4):   #right side window
        tu.forward(50)
        tu.left(90)
    tu.end_fill()
    tu.pendown()   #window lines
    tu.pencolor("black")
    for i in range(4):
        tu.forward(50)
        tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.penup()   #window lines on left side
    tu.forward(-155)
    tu.right(90)
    tu.forward(25)
    tu.left(90)
    tu.pendown()
    for i in range(4):
        tu.forward(50)
        tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(25)
    tu.left(90)
    tu.forward(50)
    tu.penup()   #door knob
    tu.right(90)
    tu.forward(105)
    tu.left(90)
    tu.forward(37)
    tu.pensize(7)
    tu.pendown()
    tu.forward(1)
    tu.penup()
    tu.goto(-500, -500)

def turtle_dog():
    """Turtle will draw a dog to live with the people in the house :) """

    dog = turtle.Turtle()
    dog.speed(0)
    dog.pencolor("Brown")
    dog.penup()
    dog.goto(0, -100)   #head
    dog.pendown()
    dog.pensize(25)
    dog.forward(15)
    dog.left(90)
    dog.forward(5)
    dog.right(90)
    dog.pensize(35)
    dog.forward(5)
    dog.penup()   #body
    dog.right(90)
    dog.forward(25)
    dog.left(90)
    dog.forward(5)
    dog.pendown()
    dog.forward(70)
    dog.pensize(13)   #tail
    dog.left(45)
    dog.forward(40)
    dog.penup()   #ear
    dog.goto(20, -85)
    dog.pendown()
    dog.pencolor("black")
    dog.right(115)
    dog.forward(20)
    dog.penup()   #nose
    dog.goto(-8, -93)
    dog.pendown()
    dog.pensize(7)
    dog.forward(1)
    dog.penup()
    dog.forward(40)
    dog.left(70)   #legs
    dog.pencolor("brown")
    dog.pensize(13)
    dog.forward(15)
    dog.pendown()
    for d in [0, 1]: #front legs
        dog.right(90)
        dog.forward(40) #leg down
        dog.right(180)
        dog.forward(40)#leg up
        dog.right(90)
        dog.forward(15)
    dog.forward(35)    #back legs
    dog.right(90)
    dog.forward(40)    #leg down
    dog.right(180)
    dog.forward(40)    #leg up
    dog.right(90)
    dog.forward(15)
    dog.right(90)
    dog.forward(40)    #leg down
    dog.right(180)
    dog.forward(40)    #leg up
    dog.penup()
    dog.goto(0, -500)


def turtle_doghouse():
    """Turtle will draw a dog house for the dog to chill in when he's outside
    and put his name on the house"""

    dh = turtle.Turtle()
    dh.penup()
    dh.speed(0)
    dh.goto(200, -175)
    dh.pendown()
    dh.fillcolor("navyblue")
    dh.begin_fill()
    for d in range(2):
        dh.forward(150)
        dh.left(90)
        dh.forward(100)
        dh.left(90)
    dh.end_fill()
    dh.penup()
    dh.left(90)   #dog house roof
    dh.forward(100)
    dh.pendown()
    dh.fillcolor("saddlebrown")
    dh.begin_fill()
    dh.left(90)
    dh.forward(15)
    dh.right(125)
    dh.forward(70)
    dh.right(55)
    dh.forward(100)
    dh.right(55)
    dh.forward(70)
    dh.right(125)
    dh.forward(160)
    dh.end_fill()
    dh.penup()  #ball #he needs some toys
    dh.pencolor("yellow")
    dh.left(90)
    dh.forward(105)
    dh.right(90)
    dh.forward(30)
    dh.pensize(20)
    dh.pendown()
    dh.forward(1)
    dh.pencolor("lime")
    dh.pensize(5)
    dh.forward(8)
    dh.forward(-17)
    dh.penup()
    dh.goto(-500, -500)
    word = turtle.Turtle()   # doghouse writing
    word.penup()
    word.setpos(275, -110)
    word.pendown()
    word.color("white")
    word.write("Hershey's House", move=False, align='center', font=("Comic Sans", 12, ("bold", "normal")))
    word.penup()
    word.goto(500, 500)

def turtle_sun():
    """Draws the sun and some clouds"""
    sun = turtle.Turtle()
    sun.penup()
    sun.speed(0)
    sun.goto(330, 300)
    sun.pendown()
    sun.pencolor("yellow")
    sun.pensize(150)
    sun.forward(1)
    sun.pensize(25)   #sun rays
    sun.penup()
    sun.forward(15)
    sun.right(90)
    sun.forward(90)
    sun.pendown()
    sun.forward(30)
    sun.penup()
    sun.forward(-50)
    for s in range(3):
        sun.right(90)
        sun.forward(50)
        sun.left(60)
        sun.forward(15)
        sun.pendown()
        sun.forward(30)
        sun.penup()
        sun.forward(-50)
    sun.penup()
    sun.goto(500, 500)
    cloud = turtle.Turtle()   # clouds
    cloud.color("white")
    cloud.penup()
    cloud.goto(0, 100)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(15)
        cloud.forward(15)
        cloud.pensize(20)
        cloud.forward(15)
        cloud.pensize(15)
        cloud.forward(15)
    cloud.penup()
    cloud.goto(60, 120)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(18)
        cloud.forward(15)
        cloud.pensize(23)
        cloud.forward(15)
        cloud.pensize(15)
        cloud.forward(15)
    cloud.penup()
    cloud.goto(200, 40)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(10)
        cloud.forward(15)
        cloud.pensize(15)
        cloud.forward(15)
        cloud.pensize(10)
        cloud.forward(15)
    cloud.penup()
    cloud.goto(100, 100)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(10)
        cloud.forward(15)
        cloud.pensize(15)
        cloud.forward(15)
        cloud.pensize(10)
        cloud.forward(15)
    cloud.penup()
    cloud.goto(-100, 200)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(25)
        cloud.forward(20)
        cloud.pensize(35)
        cloud.forward(20)
        cloud.pensize(25)
        cloud.forward(20)
    cloud.penup()
    cloud.goto(-260, 250)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(40)
        cloud.forward(30)
        cloud.pensize(50)
        cloud.forward(30)
        cloud.pensize(40)
        cloud.forward(30)
    cloud.penup()
    cloud.goto(-55, 230)
    cloud.pendown()
    for c in range(1):
        cloud.pensize(35)
        cloud.forward(30)
        cloud.pensize(45)
        cloud.forward(30)
        cloud.pensize(35)
        cloud.forward(30)
def main():

    turtle_grass()
    turtle_house()
    turtle_dog()
    turtle_doghouse()
    turtle_sun()

    wn.exitonclick()

main()

