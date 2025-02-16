import pygame
import src.ui.UI as UI
import src.ui.canvas as Canvas
import src.app.shape as shape

#list of shapes drown on the canvas
canvas=Canvas.canvas()
shapes:list=[shape.Circle(50,50,50)]
drawing=False

def update(events):
    for event in events:
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            s=UI.sidePannel.is_clicked(event.pos)
            if s!=None:
                canvas.selected_shape=s
                print("SELECTED SHAPE:",canvas.selected_shape)

            elif canvas.is_clicked(event.pos):
                canvas.start_pos=event.pos
                if canvas.selected_shape in ["rect","circle"]:
                    canvas.drawing=True

                if canvas.selected_shape=="rect":
                    canvas.start_pos=event.pos
                    print("pos defined")
                    print(event.pos)
                    canvas.drawing=True
                elif canvas.selected_shape=="circle":
                    canvas.start_pos=event.pos
                    canvas.drawing=True

        elif event.type==pygame.MOUSEBUTTONUP:
            if canvas.is_clicked(event.pos) and canvas.start_pos!=None:
                canvas.add_shape(event.pos)
                """
                if canvas.selected_shape=='rect':
                    canvas.add_shape("rect",canvas.start_pos,event.pos)
                elif canvas.selected_shape=="circle":
                    canvas.add_shape("circle",canvas.start_pos,event.pos)
                    pass
                """
            canvas.drawing=False

def render(screen):
    canvas.draw_shapes(screen)
    UI.sidePannel.render(screen)
    pass
