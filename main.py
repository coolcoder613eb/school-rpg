import pygame as pg
pg.init()


black = (0,0,0)
white = (255,255,255)

tilewidth = 32

def cr(num):
    return num * tilewidth


screen = pg.display.set_mode((cr(40),cr(20)))
pg.display.set_caption('Pong')



clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_x or event.key==pg.K_q: #Pressing the x Key will quit the game
                         running=False


    screen.fill(black)
    pg.display.flip()
    clock.tick(60)

pg.quit()
