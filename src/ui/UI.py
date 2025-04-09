import src.ui.button as button
import src.ui.pannel as pannel
import src.ui.window as window


w,h=700,500
buttons_margin=30
class SidePanel (pannel.Pannel):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.selected_button=None
    
    def is_clicked(self,MPos:tuple):
        if MPos[0]>self.start:
            r=None
            for child in self.children:
                if  child.shape.is_clicked(MPos,child.pos):
                    r=child.val
                    self.select(child)
                    break
            self.on_click()
            return r
        return None


    def select(self,selected):
        if self.selected_button !=None:
            self.selected_button.color=tuple(self.selected_button.original_color)

        self.selected_button=selected
        self.selected_button.color=(0,0,100)
windows:list[window.Window]=[]

sidePannel=SidePanel(w,h)

rect_button=button.Button((buttons_margin,buttons_margin))
rect_button.set_color((129, 204, 0))
rect_button.val='rect'
sidePannel.add_child(rect_button)
sidePannel.select(rect_button)

circle_button=button.Button((buttons_margin,
                    buttons_margin*4))
circle_button.shape=button.ShapeCircle()
circle_button.set_color((129, 204, 0))
circle_button.val="circle"
sidePannel.add_child(circle_button)

delete_button=button.Button((buttons_margin,
                  buttons_margin*4+buttons_margin))
delete_button.val="delete"
sidePannel.add_child(delete_button)

select_button=button.Button((buttons_margin,
                   buttons_margin*6+buttons_margin))
select_button.set_color((68, 0, 255))
select_button.val="select"
sidePannel.add_child(select_button)

# """
color_button=button.Button((buttons_margin,
                  buttons_margin*6+buttons_margin))
color_button.set_color((255, 0, 0))
def color_button_on_click():
    colorWindow=window.Window()
    windows.append(colorWindow)
color_button.shape.on_click=color_button_on_click
sidePannel.add_child(color_button)
# """
