from turtle import *
from random import randrange

# We store the segments of our snake in an array of coordinates
snake = [[10,0]]
# We store the current direction of our snake as a vector
aim = [0,-10]
# This is the initial coordinates of our first item of food
food = [20,0]

# Function to change the direction of the snake
def change(x,y):
  aim[0] = x
  aim[1] = y

# A reusable function for drawing a solid square 
def draw_square(x,y,size,name):
  up()
  goto(x,y)
  down()
  color(name)
  begin_fill()
  
  for count in range(4):
    forward(size)
    left(90)
    
  end_fill()

# A function to determine whether a coordinate is inside the playing area
def inside(head):
  return -200 < head[0] < 190 and -200 < head[1] < 190

# A function to move the snake, and then redraw the screen
def move():
  # create a new head of the snake by taking the previous head, and adding the aim vector
  head = [snake[-1][0] + aim[0], snake[-1][1] + aim[1]]
  
  # If we are outside the playing area, or hit our tail, draw a red square and exit
  if not inside(head) or head in snake:
    draw_square(head[0],head[1],9,'red')
    update()
    return
  
  # Add the new head to the snake
  snake.append(head)
  
  # If we are on a food square, create a new random food square
  if head == food:
    food[0] = randrange(-15,15) * 10
    food[1] = randrange(-15,15) * 10

  # Otherwise, remove the end of our snake  
  else:
    snake.pop(0)

  # clear everything on the screen  
  clear()
  
  # draw a square for every segment in our snake
  for body in snake:
    draw_square(body[0],body[1],9,'black')

  # draw the square for food
  draw_square(food[0],food[1],9,'green')
  
  # display all our drawing on the screen
  update()
  
  # wait 100ms, then do it all again
  Screen().ontimer(move,200) #default 100
  
Screen().setup(420,420,370,0)
hideturtle()

# This makes the turtle do all the drawing in the background.  We need to call update() to display it
Screen().tracer(0,0)

# Listen for key press, and run the change function if an arrow key is pressed.
Screen().listen()
Screen().onkey(lambda: change(10,0), 'Right')
Screen().onkey(lambda: change(-10,0), 'Left')
Screen().onkey(lambda: change(0,10), 'Up')
Screen().onkey(lambda: change(0,-10), 'Down')

# Start the snake moving
move()

done()