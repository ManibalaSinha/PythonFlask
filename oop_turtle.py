import turtle
#define constants
WIDTH=1000
HEIGHT=1000
DELAY = 20 #milliseconds
def move_turtle():
    stamper.forward(1)
    stamper.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

#create window where we will do drawing
screen=turtle.Screen()
screen.setup(WIDTH, HEIGHT)#set dimensions of the turtle graphics window 
screen.title("Stamping")
screen.bgcolor("cyan")
screen.tracer(0) #turns off automatic animation

#create a turtle to do any stuff
stamper= turtle.Turtle()
stamper.shape("triangle")
stamper.color("blue")
stamper.shapesize(50 / 20)#20 focus
stamper.stamp() #current location
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(200, 200)
stamper.stamp()

#set animation in motion
move_turtle()

turtle.done()