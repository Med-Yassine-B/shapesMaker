import pygame
import src.app.app as app

w,h=700,500

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((w,h))

running=True
while running:

    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            running=False

    app.update(events)
    app.render(screen)
    clock.tick(60)



