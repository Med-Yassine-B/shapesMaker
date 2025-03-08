import pygame
import src.ui.UI as UI
import src.ui.canvas as Canvas

canvas=Canvas.canvas()

def update(events):
    for event in events:
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            for i in range(len(UI.windows)):
                if UI.windows[i]!=None and UI.windows[i].is_clicked(event.pos):
                    UI.windows[i].on_click(event.pos)
                    break
                else:
                    UI.windows[i]=None
            s=UI.sidePannel.is_clicked(event.pos)
            if s!=None:
                canvas.selected_shape=s
                print("SELECTED SHAPE:",canvas.selected_shape)

            elif canvas.is_clicked(event.pos):
                canvas.start_pos=event.pos
                if canvas.selected_shape in ["rect","circle"]:
                    canvas.drawing=True
                    canvas.mousePos=event.pos
                elif canvas.selected_shape=="select":
                    canvas.select(event.pos)
                elif canvas.selected_shape=="delete":
                    canvas.delete(event.pos)


        elif event.type==pygame.MOUSEBUTTONUP:
            if canvas.is_clicked(event.pos) and canvas.start_pos!=None:
                canvas.add_shape(event.pos)
            canvas.drawing=False
        elif event.type==pygame.MOUSEMOTION:
            if canvas.drawing:
                canvas.mousePos=event.pos
            pass

def render(screen):
    screen.fill((255,255,255))  #fill the screen with white
    canvas.draw_shapes(screen)
    canvas.draw_preview(screen)
    UI.sidePannel.render(screen)
    for window in UI.windows:
        if window!=None:
            window.render(screen)
    
    pygame.display.flip()
    pass
