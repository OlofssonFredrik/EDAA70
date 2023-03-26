from maze import Maze
import turtle


maze = Maze(4)
x,y = maze.entry()

ninja = turtle.Turtle()
ninja.penup()
ninja.goto(x,y)
ninja.shapesize(0.75)
ninja.shape('turtle')
angle = 90
ninja.setheading(angle)




while not maze.at_exit((x,y)):
    print(f"xcor: {ninja.xcor()} ycor: {ninja.ycor()}")
    
    
    if maze.wall_at_left(angle,(x,y)):
        ninja.forward(9)
    else:
        angle = 180
        ninja.setheading(angle)
   
    
   
    #ninja.left(90)
    
        
    
        
        
    #if not maze.wall_in_front(angle,(x,y)):
    #    ninja.forward(10)
    #
    #ninja.forward(10)
    #if x == ninja.xcor():
    #    break
    
    x = ninja.xcor()
    y = ninja.ycor()
    
    
#Gå rakt fram. 
#Finns det inte vägg till vänster? Gå Vänster
#F
   
    
turtle.mainloop()

