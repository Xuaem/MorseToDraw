#Importing turtle so python can reference the drawing library
import random
import Config
import Drawer

#Taking the input from user to convert to Morse
current_input = input("Input the text to convert to morse: \n\n")
xmaster_input = ""
ymaster_input = ""

while current_input != "!!!!!" or current_input == "\n":
    xmaster_input = xmaster_input + current_input
    current_input = input("Input the text to convert to morse: \n\n")

current_input = input("Would you like to add a y-axis? (Y/N) \n\n")
current_input = current_input.capitalize()
if current_input != "N":
    current_input = input("Input the text to convert to morse: \n\n")
    while current_input != "!!!!!" or current_input == "\n":
        ymaster_input = ymaster_input + current_input
        current_input = input("Input the text to convert to morse: \n\n")

xlngth = len(xmaster_input)
ylngth = len(ymaster_input)
logMorse = ""
logMorseY = ""

#X Axis
print("You wrote: " + xmaster_input + " " + ymaster_input)
for x in range(0, xlngth):
    c = xmaster_input[x]
    c = c.upper()
    logMorse = logMorse + Config.morseNumericalKeyVal[c]
    print(Config.morseNumericalKeyVal[c])

#Y Axis
for x in range(0, ylngth):
    c = ymaster_input[x]
    c = c.upper()
    logMorseY = logMorseY + Config.morseNumericalKeyVal[c]
    print(Config.morseNumericalKeyVal[c])

#Next step is to save the new string and convert dot-dashes
#to an input that turtle can understand i.e (.) being 10 pixels
#or (-) being 20 pixels (logMorse)

print("\n\n" + "DEBUG X-Axis:: " + logMorse + "\nY-Axis::" + logMorseY)
print("\n")


#Starting a turtle window that exits on click only*********
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
drawer = Drawer.Drawer()

#Scanning through logMorse to translate 0/1/2/3 into dashes horizontally
#and making a new line when the turtle reaches the margin
lngthMorseX = len(logMorse)
for x in range(0, lngthMorseX):
    rnum2short = random.randint(8,30)
    rnum3long = random.randint(50,225)
    rnum4longdark = random.randint (40,100)
    if (logMorse[x] == "0"):
        drawer.drawSegmentXAxis(10, 3)
    elif (logMorse[x] == "1"):
        drawer.drawSegmentXAxis(20, 3)
    elif (logMorse[x] == "2"):
        drawer.drawSegmentXAxis(rnum2short, 1)
    elif (logMorse[x] == "3"):
        drawer.drawSegmentXAxis(rnum3long, 1)
    elif (logMorse[x] == "4"):
        drawer.drawSegmentXAxis(rnum4longdark, 3)

#Taking down pens final position on the y-axis so we can reference that for the y-axis drawing
#Have to use +1-1 here to define ycor as an int for some reason, otherwise ycor returns an object
finalHorizontal = drawer.get_ycor
print(finalHorizontal)

#Once done with the x-axis, we want the turtle to return to its start position and work down
drawer.vertical_reset

#Doing the same thing vertically (Y Axis)
lngthMorseY = len(logMorseY)
for x in range(0, lngthMorseY):
    rnum2short = random.randint(8,30)
    rnum3long = random.randint(50,225)
    rnum4longdark = random.randint (40,100)
    if (logMorseY[x] == "0"):
        if ((oogway.ycor() + 10) <= finalHorizontal):
            oogway.penup()
            oogway.goto(oogway.xcor() + 8,((windowHeight/2) - 50))
            oogway.pendown()
            oogway.pensize(3)
            oogway.forward(10)
        else:
            oogway.pendown()
            oogway.pensize(3)
            oogway.forward(10)
    elif (logMorseY[x] == "1"):
        if ((oogway.ycor() + 20) <= finalHorizontal):
            oogway.penup()
            oogway.goto(oogway.xcor() + 8,((windowHeight/2) - 50))
            oogway.pendown()
            oogway.pensize(3)
            oogway.forward(20)
        else:
            oogway.pendown()
            oogway.pensize(3)
            oogway.forward(20)
    elif (logMorseY[x] == "2"):
        if ((oogway.ycor() + rnum2short) <= finalHorizontal):
            oogway.penup()
            oogway.goto(oogway.xcor() + 8,((windowHeight/2) - 50))
            oogway.pendown()
        else:
            oogway.pendown()
            oogway.pensize(1)
            oogway.forward(rnum2short)
    elif (logMorseY[x] == "3"):
        if ((oogway.ycor() + rnum3long) <= finalHorizontal):
            oogway.penup()
            oogway.goto(oogway.xcor() + 8,((windowHeight/2) - 50))
            oogway.pendown()
        else:
            oogway.pendown()
            oogway.pensize(1)
            oogway.forward(rnum3long)
    elif (logMorseY[x] == "4"):
        if ((oogway.ycor() + rnum4longdark) <= finalHorizontal):
            oogway.penup()
            oogway.goto(oogway.xcor() + 8,((windowHeight/2) - 50))
            oogway.pendown()
        else:
            oogway.pendown()
            oogway.pensize(3)
            oogway.forward(rnum4longdark)

