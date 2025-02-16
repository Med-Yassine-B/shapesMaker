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
        pass

    def draw_shapes(self,screen):
        for shape in self.shapes:
            shape.render(screen)

    def is_clicked(self,pos):
        return pos[0]<self.w and pos[1]<self.h
    
    def add_shape(self,end):
        print("SHAPE:",self.selected_shape)
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



