import pygame

class Window:
    def __init__(self):
        self.pos=(50,50)
        self.w=100
        self.h=100
        self.color=(50,50,50)
        self.children=[]
        self.val=None
        
    def render(self,screen):
        pygame.draw.rect(screen,self.color,(self.pos[0],self.pos[1],self.w,self.h))
        close_b_size=15
        close_b_x=self.pos[0]+self.w-close_b_size
        
        pygame.draw.rect(screen,(255,0,0),(close_b_x,self.pos[1],close_b_size,close_b_size))
        for child in self.children:
            child.render(screen)
    def is_clicked(self,MPos:tuple):
        if (MPos[0]>self.pos[0] and MPos[1]>self.pos[1]) and (MPos[0]<self.pos[0]+self.w and MPos[1]<self.pos[1]+self.h):
            self.on_click(MPos)
            return True
        return False
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def on_click(self,MPos:tuple):
        for child in self.children:
            if child.shape.is_clicked(MPos,child.pos):
                child.on_click()

        
        pass
    def close(self):
        pass
