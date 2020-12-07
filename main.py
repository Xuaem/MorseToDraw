#Importing turtle so python can reference the drawing library
import random
import Config
import Drawer
import Encoder

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

#Turning text into number string for the drawer to use
print("You wrote: " + xmaster_input + " " + ymaster_input)
logMorse = Encoder.morse_encode(xmaster_input)
logMorseY = Encoder.morse_encode(ymaster_input)

#Next step is to save the new string and convert dot-dashes
#to an input that turtle can understand i.e (.) being 10 pixels
#or (-) being 20 pixels (logMorse)
print("\n\n" + "DEBUG:: " + logMorse + "\n" + logMorseY)
print("\n")


#Starting a turtle window that exits on click only
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
        drawer.drawSegmentXAxis(20,3)
    elif (logMorse[x] == "2"):
        drawer.drawSegmentXAxis(rnum2short, 1)
    elif (logMorse[x] == "3"):
        drawer.drawSegmentXAxis(rnum3long, 1)
    elif (logMorse[x] == "4"):
        drawer.drawSegmentXAxis(rnum4longdark, 3)

#Taking down pens final position on the y-axis so we can reference that for the y-axis drawing
finalHorizontal = drawer.get_ycor()

#Once done with the x-axis, we want the turtle to return to its start position and work down
drawer.vertical_reset()

#Doing the same thing vertically (Y Axis)
lngthMorseY = len(logMorseY)
for x in range(0, lngthMorseY):
    rnum2short = random.randint(8,30)
    rnum3long = random.randint(50,225)
    rnum4longdark = random.randint (40,100)
    if (logMorseY[x] == "0"):
        drawer.drawSegmentYAxis(10, 3, finalHorizontal)
    elif (logMorseY[x] == "1"):
        drawer.drawSegmentYAxis(20, 3, finalHorizontal)
    elif (logMorseY[x] == "2"):
        drawer.drawSegmentYAxis(rnum2short, 1, finalHorizontal)
    elif (logMorseY[x] == "3"):
        drawer.drawSegmentYAxis(rnum3long, 1, finalHorizontal)
    elif (logMorseY[x] == "4"):
        drawer.drawSegmentYAxis(rnum4longdark, 3, finalHorizontal)

#Allows the canvas to stay open after finishing the drawing
drawer.end_canvas()

