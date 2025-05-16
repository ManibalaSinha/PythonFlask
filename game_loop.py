import turtle
import random
#define constants
WIDTH = 500
HEIGHT = 500
DELAY = 100 #milliseconds
FOOD_SIZE = 10
#offset determines how much snakes moves in each directions
offsets = {
    "up": (0, 20),
    "down": (0,-20),
    "left": (-20, 0),
    "right": (20, 0)
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
def game_loop():
    stamper.clearstamps()#remove existing stamps by stamper
    new_head = snake[-1].copy() #last segment of the list
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        turtle.bye() #closing the program
    else:
        #add new head to snake body
        snake.append(new_head)
        if not food_collision():
        #remove last segment of snake
            snake.pop(0)
        #Draw snake 
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
    #refresh screen
    screen.update()
    #repeat
    turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return(x,y)
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) **2) ** 0.5 # Pythagoras Theorem
    return distance
#create window where we will do drawing
screen=turtle.Screen()
screen.setup(WIDTH, HEIGHT)#set dimensions of the turtle graphics window 
screen.title("Snake Food")
screen.bgcolor("blue")
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

#Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

#set animation in motion
game_loop()

turtle.done()