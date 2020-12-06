import turtle

class Drawer:
	def __init__(self):
		self.canvas = turtle.Screen()
		self.canvas.setup(width = .99, height = .99)
		self.windowHeight = canvas.window_height()
		self.windowWidth = canvas.window_width()
		self.pen = turtle.Turtle()
		self.pen.hideturtle()
		self.pen.speed(0)
		self.pen.penup()
		self.pen.goto(((windowWidth/2) - (windowWidth) + 50),((windowHeight/2) - 50))
		self.pen.color("black")
		self.pen.pendown()

	def drawSegment(self, segment_length):
		if ((pen.xcor() + segment_length) >= (windowWidth/2 - 50)):
			pen.penup()
			pen.goto(((windowWidth/2) - (windowWidth) + 50),pen.ycor() - 8)
			pen.pendown()
			pen.pensize(3)
			pen.forward(10)
		else:
			pen.pendown()
			pen.pensize(3)
			pen.forward(10)

	def draw(c):
		drawSmallSpace()
		if c == " ":
			drawSpace()

	def drawDot():

	def drawDash():

	def drawSpace():

"ry w"

".-.&-.-- .--"



