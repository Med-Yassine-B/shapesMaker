import pygame

class canvas:
    def __init__(self):
        pass

    def draw_shapes(self,screen,shapes):
        for shape in shapes:
            shape.render(screen)
