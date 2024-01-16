import time 
from colorama import Fore ,Back ,Style ,init 
init (autoreset =True )
def startMessage ():
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code: ")
    OOOO0OO000OO0OOOO ="Jaan"
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] wrong code')
        print (Fore .BLUE +''' 
   1. Join my Telegram Group for Code 
   2. insta Id cybershielddefender
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')
        startMessage ()
    else :
        print (Fore .GREEN +"Successfully Unlocked Tool!")
        pass 
if __name__ =="__main__":
    startMessage ()

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint
#Main
import turtle
import random
import time
from pygame import mixer

# Adding music is optional as per your choice.
mixer.pre_init(frequency=48000, size=-16, channels=2, buffer=512)
mixer.init()
mixer.music.load("happy-birthday-song.mp3") #add your music file name or path

# sets background
bg = turtle.Screen()
bg.bgcolor("black")
mixer.music.play()


# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("lightblue")

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("orange")

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("black")

# Happy Birthday message

turtle.penup()
turtle.goto(-150, 50)
turtle.color("pink")
turtle.pendown()

# ENTER YOUR NAME IN THE NAME PLACE
turtle.write(arg=f"Happy Birthday Qadir!", align="left", font=("jokerman", 24, "normal"))

time.sleep(5)
