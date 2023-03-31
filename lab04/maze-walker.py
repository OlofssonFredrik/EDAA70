import turtle
import maze

def solve_maze(maze_num,turtle_size):
    # Create maze object
    maze.object = maze.Maze(maze_num)

    # If a big maze, make the turtle run faster
    if(maze_num==5):
        turtle.Screen().tracer(2)
    if(maze_num==4):
        turtle.Screen().delay(0.8)

    # Create turtle object
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    t.penup()
    t.shapesize(turtle_size)

    # Set turtle position to entry and direction upwards
    t.goto(maze.object.entry())
    t.setheading(90)
    
    # Highlight the turtles path
    t.pendown()
    t.pencolor('Red')
    
    
    # Walk along the left wall until exit is reached
    while not maze.object.at_exit(t.pos()):
        # Check if there is a wall to the left
        left_wall = maze.object.wall_at_left(t.heading(), t.pos())

        # Check if there is a wall in front of turtle
        front_wall = maze.object.wall_in_front(t.heading(), t.pos())

        if left_wall and front_wall:
            # Wall to the left and front, turn right
            t.right(90)
        elif left_wall and not front_wall:
            # Wall to the left but no wall in front, move forward
            t.forward(1)
        else:
            # No wall to the left, turn left
            t.left(90)
            t.forward(1)

    # Exit reached, print a message
    print("Exit reached!")

    # Keep the turtle window open until manually closed
    turtle.mainloop()


print("==========================================================================")
print("Enter which maze you want to solve, you can choose between 1-5 and the size of your turtle, choose between 0-1.")
print("==========================================================================")
maze_num = int(input("Enter maze "))
turtle_size = float(input("Enter Turtle Size "))

solve_maze(maze_num,turtle_size)
