import pygame
import math
import src.app.shape as Shape

class canvas:
    def __init__(self):
        self.w=500
        self.h=500
        self.shapes=[]
        self.selected_shape="rect"
        self.start_pos=(0,0)
        self.drawing=False
        self.mousePos=(0,0)
        self.selected=None

    def draw_shapes(self,screen):
        for shape in self.shapes:
            shape.render(screen)

    def is_clicked(self,pos):
        return pos[0]<self.w and pos[1]<self.h
    
    def add_shape(self,end):
        if not (self.start_pos and end and self.selected_shape):
            return

        if self.selected_shape=="rect":
            s=(min(self.start_pos[0],end[0]),
               min(self.start_pos[1],end[1]))

            e=(max(self.start_pos[0],end[0]),
               max(self.start_pos[1],end[1]))

            e=(e[0]-s[0],e[1]-s[1])

            sh=Shape.Rect(s[0],s[1],e[0],e[1])
            self.shapes.append(sh)
            
        elif self.selected_shape=="circle":
            r=math.sqrt((end[0]-self.start_pos[0])**2+(end[1]-self.start_pos[1])**2)
            sh=Shape.Circle(self.start_pos[0],self.start_pos[1],r)

            self.shapes.append(sh)

    def draw_preview(self,screen):
        end=self.mousePos
        if not self.drawing:    return
        if self.selected_shape=="rect":
            s=(min(self.start_pos[0],end[0]),
               min(self.start_pos[1],end[1]))

            e=(max(self.start_pos[0],end[0]),
               max(self.start_pos[1],end[1]))

            pygame.draw.rect(screen,(200,100,100,0),(
                                 s[0],
                                 s[1],
                                 e[0]-s[0],
                                 e[1]-s[1]))
        elif self.selected_shape=="circle":
            r=math.sqrt((end[0]-self.start_pos[0])**2+(end[1]-self.start_pos[1])**2)
            pygame.draw.circle(screen,(200,100,100),(
                                self.start_pos[0],self.start_pos[1]),r)
    def select(self,pos):
        for i in range(len(self.shapes)-1,-1,-1):
            if self.shapes[i].is_clicked(pos):
                self.shapes[i].color=(50,60,70)
                break
        pass
    def delete(self,pos):
        for i in range(len(self.shapes)-1,-1,-1):
            if self.shapes[i].is_clicked(pos):
                self.shapes.pop(i)
                break
        pass



