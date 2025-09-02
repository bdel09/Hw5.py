#Name: Benjamin Del Barrio
#Email: Benjamin.delbarrio31@myhunter.cuny.edu

import turtle
wn= turtle.Screen()
t=turtle.Turtle()
t.color('blue')
t.speed(0)
for i in range(50):
   for j in range(5):
    t.forward(100)
    t.right(72)
   t.right(70)
t.done()
wn.exitonclick()
