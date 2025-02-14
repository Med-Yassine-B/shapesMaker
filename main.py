import pygame
import math
import src.button as button
import src.UI as UI

w,h=700,500

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((w,h))

selected_color=(255,255,0)
selected_drown_shape=None

drown_shapes=[]
start_pos=()
drawing=False

pannel_size=(200,h)
pannel_start=w-pannel_size[0]


canvas=pygame.Surface((w-pannel_size[0],h))

buttons_margin=30
buttons_size=50

# change to the new UI system

rect_button_pos=(pannel_start+buttons_margin,buttons_margin)
rect_buton_color=(255,0,0)

circle_pos=(pannel_start+buttons_margin+buttons_size//2,
                    buttons_margin*4)
circle_button_color=(255,0,0)

delete_button_pos=(pannel_start+buttons_margin,
                  buttons_margin*4+buttons_margin)
delete_button_color=(255,255,0)
#======
select_button_pos=(pannel_start+buttons_margin,
                   buttons_margin*6+buttons_margin)
select_button_color=(255,255,0)

def UI_render():
    UI.sidePannel.render(screen)
    pygame.display.flip()
    pass


def check_buttons_click(click_pos):

    #check for rect_click
    if rect_button_pos[0]+buttons_size>click_pos[0]>rect_button_pos[0]and rect_button_pos[1]+buttons_size>click_pos[1]>rect_button_pos[1]:
        # print("RECT CLICKED")
        return "rect"

    #check for circle click_pos
    click_distance=math.sqrt((circle_pos[0]-click_pos[0])**2+
                             (circle_pos[1]-click_pos[1])**2)
    if click_distance<buttons_size//2:
        # print("CIRCLE CLICKED")
        return "circle"
        pass

    #check for delete_click
    if delete_button_pos[0]+buttons_size>click_pos[0]>delete_button_pos[0]and delete_button_pos[1]+buttons_size>click_pos[1]>delete_button_pos[1]:
        # print("DELETE CLICKED")
        return "delete"

    #check for select_click
    if select_button_pos[0]+buttons_size>click_pos[0]>select_button_pos[0]and select_button_pos[1]+buttons_size>click_pos[1]>select_button_pos[1]:
        # print("SELECT CLICKED")
        return "select"
    pass

def render():
    #===render
    screen.fill((255,255,255))
    for shape in drown_shapes:
        if shape[0]=="rect":
            pygame.draw.rect(screen,shape[1],
                        (shape[2],shape[3],
                         shape[4],shape[5]))
        elif shape[0]=="circle":
            pygame.draw.circle(screen,shape[1],
                               (shape[2],shape[3]),
                               shape[4])
    if drawing:
        draw_preview(selected_shape,start_pos,pygame.mouse.get_pos())
    #render UI at the end
    UI_render()

    pass

def canvas_clicked(pos):
    return pos[0]<pannel_start
    
def add_shape(shape,start,end):
    if shape=="rect":
        s=(min(start[0],end[0]),min(start[1],end[1]))
        e=(max(start[0],end[0]),max(start[1],end[1]))
        drown_shapes.append(("rect",selected_color,
                             s[0],
                             s[1],
                             e[0]-s[0],
                             e[1]-s[1]))
    elif shape=="circle":
        r=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
        drown_shapes.append(("circle",selected_color,
                             start[0],start[1],r))

def shape_clicked(shape,pos):
    if shape[0]=="rect":
        return pos[0]>shape[2] and pos[1]>shape[3] and pos[0]<shape[2]+shape[4] and pos[1]<shape[3]+shape[5]

    if shape[0]=="circle":
        c=math.sqrt(((pos[0]-shape[2])**2)+((pos[1]-shape[3])**2))
        return c<shape[4]

def draw_preview(shape,start,end):
    if shape=="rect":
        s=(min(start[0],end[0]),min(start[1],end[1]))
        e=(max(start[0],end[0]),max(start[1],end[1]))
        pygame.draw.rect(screen,(200,100,100,0),(
                             s[0],
                             s[1],
                             e[0]-s[0],
                             e[1]-s[1]))
    elif shape=="circle":
        r=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
        pygame.draw.circle(screen,(200,100,100),(
                            start[0],start[1]),r)

    #pygame.display.flip()
    

running=True
def start():
    screen.fill((255,255,255))
    render()
    pygame.display.flip()

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            s=UI.sidePannel.is_clicked(event.pos)
            if s!=None:
                selected_shape=s
                print(selected_shape)
            
            #detect drawing shapes
            elif canvas_clicked(event.pos):
                if selected_shape=="rect":
                    start_pos=event.pos
                    drawing=True
                elif selected_shape=="circle":
                    start_pos=event.pos
                    drawing=True
                elif selected_shape=="delete":
                    for i in range(len(drown_shapes)):
                        if shape_clicked(drown_shapes[i],event.pos):
                            drown_shapes[i]=("deleted")
                    print("used delete")

                #selecting drown shapes
                elif selected_shape=="select":
                    for i in range(len(drown_shapes)-1,-1,-1):
                        if shape_clicked(drown_shapes[i],event.pos):
                            if drown_shapes[i][0]=="rect":
                                drown_shapes[i]=(drown_shapes[i][0],
                                                 (0,0,255),
                                                 drown_shapes[i][2],
                                                 drown_shapes[i][3],
                                                 drown_shapes[i][4],
                                                 drown_shapes[i][5])
                                break
                            elif drown_shapes[i][0]=="circle":
                                drown_shapes[i]=(drown_shapes[i][0],
                                                 (0,0,255),
                                                 drown_shapes[i][2],
                                                 drown_shapes[i][3],
                                                 drown_shapes[i][4])
                                break
            


                        
                        

        #add shape when mouse up
        elif event.type==pygame.MOUSEBUTTONUP:
            if start_pos!=() and canvas_clicked(event.pos):
                if selected_shape=='rect':
                    add_shape("rect",start_pos,event.pos)
                elif selected_shape=="circle":
                    add_shape("circle",start_pos,event.pos)
                    pass
            drawing=False
    #elif event.type==pygame.MOUSEMOTION:
    render()

    clock.tick(60)



