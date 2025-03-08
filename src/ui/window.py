import pygame

class window:
    def __init__(self):
        self.x=50
        self.y=50
        self.w=100
        self.h=100
        self.color=(50,50,50)
        self.children=[]
        
    def render(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
        for child in self.children:
            child.render(screen)
    def on_click(self):
        pass
