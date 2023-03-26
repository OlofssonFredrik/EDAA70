import turtle
import math
import random


ninja = turtle.Turtle()
ninja2 = turtle.Turtle()


class Padda:
    def __init__(self,padda1,padda2,x1,x2,y1,y2):
        self.padda1 = padda1
        self.padda2 = padda2
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def distance(self, x1,x2,y1,y2):
        dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return dist
    
    def random_walk(self):
        self.padda1.pendown()
        self.padda1.goto(self.x1, self.y1)
        
        self.padda2.pendown()
        self.padda2.goto(self.x2, self.y2)
        
        while self.distance(self.x1, self.x2,self.y1, self.y2) != 0:
           
            step = random.randint(1,10)
            degree = random.randint(-90,90)
            left_right_padda1 = random.randint(0,1)
            left_right_padda2 = random.randint(0,1)
            
            if left_right_padda1 > 0.5:
                self.padda1.forward(step)
                self.padda1.right(degree)
            else:
                self.padda1.forward(step)
                self.padda1.left(degree)
                
            if left_right_padda2 > 0.5:
                self.padda2.forward(step)
                self.padda2.right(degree)
            else:
                self.padda2.forward(step)
                self.padda2.left(degree)
            
            self.x1 = self.padda1.xcor()
            self.x2 = self.padda1.ycor()
            self.y1 = self.padda2.xcor()
            self.y2 = self.padda2.ycor()
            
        turtle.mainloop()

ninja = turtle.Turtle
ninja2 = turtle.Turtle
Padda(ninja, ninja2,-50,-50,50,50).random_walk()
        

    

