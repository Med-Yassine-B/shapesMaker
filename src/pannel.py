import pygame

class Pannel:
    def __init__(self,w:int,h:int):
        self.size=(200,h)
        self.start=w-self.size[0]
        self.children_margin=30

        self.children:list=[]
    
    def add_child(self,child):
        child.pos=(child.pos[0]+self.start,child.pos[1])
        child.parent=self
        self.children.append(child)
        self.allign_children()

    def render(self,screen):
        pygame.draw.rect(screen,(50,50,50),
                    (self.start,
                    0,
                    self.size[0],
                    self.size[1]))

        for child in self.children:
            child.render(screen)
        pass
    
    def on_click(self):
        pass

    def is_clicked(self,MPos:tuple):
        if MPos[0]>self.start:
            for child in self.children:
                if  child.shape.is_clicked(MPos,child.pos):
                    child.on_click()
                    break
            self.on_click()
            return True
        return False
    
    def allign_children(self):
        x=self.children_margin+self.start
        y=self.children_margin
        for i in range(len(self.children)):
            
            self.children[i].pos=(x,y)
            if i%2==1:
                y+=self.children[i].shape.size+self.children_margin
                x=self.start+self.children_margin
            else:
                x+=self.children[i].shape.size+self.children_margin

