import turtle
import random

ninja = turtle.Turtle()


def random_walk(padda, step, steplen, degrees):
    for i in range(step):
        val = random.randint(0,1)
        if val > 0.5:
            padda.right(degrees)
            padda.pendown()
            padda.pencolor('green')
        else:
            padda.left(degrees)
            padda.pendown()
            padda.pencolor('red')
            
        ninja.forward(steplen)
    turtle.mainloop()
    
random_walk(ninja,20,10,90)
    





#Gå slumpmässigt
#100 Steg frammåt
#Varje steg 10px
#Innan varje steg, slump 45 grader vänster/höger