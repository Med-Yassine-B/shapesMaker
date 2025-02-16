import src.ui.UI as UI
import src.ui.canvas as Canvas
import src.app.shape as shape

#list of shapes drown on the canvas
canvas=Canvas.canvas()
shapes:list=[shape.Circle(50,50,50)]

def update():
    pass

def render(screen):
    canvas.draw_shapes(screen,shapes)

    UI.sidePannel.render(screen)
    pass
