import turtle

ninja = turtle.Turtle()

ninja2 = turtle.Turtle()
for i in range(4):
    ninja.forward(150)
    ninja.left(90)
    
    ninja2.backward(150)
    ninja2.right(90)
    
turtle.mainloop()