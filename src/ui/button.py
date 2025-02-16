import pygame

default_bg_color=(0,255,255)

class ShapeRect:
    def __init__(self):
        self.size=50
        pass
    
    def render(self,screen,position,color):
        pygame.draw.rect(screen,color,
                        (position[0],
                        position[1],
                        self.size,
                        self.size))
    def is_clicked(self,MPos,pos):
        return (MPos[0]>pos[0] and MPos[0]<pos[0]+self.size) and (MPos[1]>pos[1] and MPos[1]<pos[1]+self.size)

class ShapeCircle:
    def __init__(self):
        self.size=50

    def render(self,screen,position,color):
        pygame.draw.circle(screen,color,
                       (position[0]+self.size//2,
                        position[1]+self.size//2),
                       self.size//2)
    def is_clicked(self,MPos,pos):
        return (pos[0]-MPos[0])**2 + (pos[1]-MPos[1])**2 <= (self.size)**2


class Button:
    def __init__(self,pos=(0,0)):
        self.pos=pos
        self.color=(0,255,255)
        self.original_color=tuple(self.color)
        self.margin:int=5
        self.shape:ShapeRect|ShapeCircle=ShapeRect()
        self.parent=None
        self.val=None
        
    def set_color(self,color):
        self.color=tuple(color)
        self.original_color=tuple(color)
    def render(self,screen):
        if self.shape:
            self.shape.render(screen,self.pos,self.color)

    def on_click(self):
        print("button clicked")
        return self.val
        pass
