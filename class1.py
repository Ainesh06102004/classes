import random


class Ball(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def elasticity(self):
        elastic = "Nice"
        print(elastic)

ball1 = Ball(69,420)
print(ball1.x,ball1.y)
ball1.elasticity()