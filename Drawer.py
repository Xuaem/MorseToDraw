import turtle

class Drawer():
    def __init__(self):
        self.canvas = turtle.Screen()
        self.canvas.setup(width = .99, height = .99)
        self.windowHeight = self.canvas.window_height() - 100
        self.windowWidth = self.canvas.window_width() - 100
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(- self.windowWidth / 2, self.windowHeight / 2)
        self.pen.color("black")
        self.pen.pendown()
    
    #Functions return X/Y coordinates respectively
    def get_xcor(self):
        return self.pen.xcor() + 1 - 1

    def get_ycor(self):
        return self.pen.ycor() + 1 - 1

    #Allows the canvas to stay open after finished drawing
    def end_canvas(self):
        self.canvas.exitonclick()

    #Resets pen to origin and sets the pen heading south
    def vertical_reset(self):
        self.pen.penup()
        self.pen.goto(- self.windowWidth / 2, self.windowHeight / 2)
        self.pen.pendown()
        self.pen.setheading(270)

    #Drawing the canvas
    def drawSegmentXAxis(self, segment_length, pen_size):
        self.drawSegment(True, segment_length, pen_size, self.windowWidth / 2, - self.windowWidth / 2, self.pen.ycor() - 8)

    def drawSegmentYAxis(self, segment_length, pen_size, final_position):
        self.drawSegment(False, segment_length, pen_size, final_position, self.pen.xcor() + 8, self.windowHeight / 2)

    def drawSegment(self, is_x_axis, segment_length, pen_size, final_postion, next_line_start_x, next_line_start_y):
        self.pen.pensize(pen_size)
        if (is_x_axis == True and (self.pen.xcor() + segment_length) >= final_postion ):
            self.pen.penup()
            self.pen.goto(next_line_start_x, next_line_start_y)
        elif (is_x_axis == False and (self.pen.ycor() - segment_length) <= final_postion ):
            self.pen.penup()
            self.pen.goto(next_line_start_x, next_line_start_y)
        self.pen.pendown()
        self.pen.forward(segment_length)
