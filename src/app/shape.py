import pygame

default_color=(255,0,255)

class Shape:
    def __init__(self,x,y):
        
        self.x=x
        self.y=y
        self.color=default_color

class Rect(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w=w
        self.h=h
        
    def render(self,screen):
                    pygame.draw.rect(screen,self.color,
                        (self.x,self.y,
                         self.w,self.h))

class Circle(Shape):
    def __init__(self, x, y,r):
        super().__init__(x, y)
        self.r=r
    def render(self,screen):
        print("circle rendering")
        pygame.draw.circle(screen,self.color,
                        (self.x,self.y) , self.r)
    
