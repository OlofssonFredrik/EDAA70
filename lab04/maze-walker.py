from maze import Maze
import turtle



x,y = Maze(4).entry()

ninja = turtle.Turtle
ninja.goto(x,y)

turtle.mainloop()