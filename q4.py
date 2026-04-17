import turtle

class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
    def __str__(self):
        return f"({self.x},{self.y})"
    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.dot()
        turtle.write(str(f"point{p}"))





p1 = point(0, 0)
p2 = point(100, 0)
p3 = point(100, 100)
p4 = point(0, 100)


points = [p1, p2, p3, p4]



for p in points:
    p.draw()
turtle.exitonclick()