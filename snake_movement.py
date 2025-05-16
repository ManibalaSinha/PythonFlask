import turtle
#define constants
WIDTH=1000
HEIGHT=1000
DELAY = 500 #milliseconds
#offset determines how much snakes moves in each directions
offsets ={
    "up":(0, 20),
    "down":(0,-20),
    "left":(-20, 0),
    "right":(20, 0)
}
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"
def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"
def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"
def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"
def move_snake():
    stamper.clearstamps()#remove existing stamps by stamper
    new_head = snake[-1].copy() #last segment of the list
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #Add new head to snake body
    snake.append(new_head)
    #remove last segment of snake
    snake.pop(0)
    #Draw snake 
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
    #refresh screen
    screen.update()
#repeat
    turtle.ontimer(move_snake, DELAY)
#create window where we will do drawing
screen=turtle.Screen()
screen.setup(WIDTH, HEIGHT)#set dimensions of the turtle graphics window 
screen.title("Snake Control")
screen.bgcolor("red")
screen.tracer(0) #disable automatic animation
#Event handler
screen.listen()#listen to event 
screen.onkey(go_up, "Up") #when key is pressed
screen.onkey(go_right, "Right") 
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
#create a turtle to do any stuff
stamper= turtle.Turtle()
stamper.shape("square")
stamper.penup()

#Create snake as a list of coordinate pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"#global variable
#Draw snake 
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

#set animation in motion
move_snake()

turtle.done()