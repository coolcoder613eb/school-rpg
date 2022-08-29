import pygame as pg
import pytmx
from pytmx.util_pygame import load_pygame
pg.init()



black = (0,0,0)
white = (255,255,255)
grey = (137,137,137)

tilewidth = 32

def cr(num):
    return ((num * tilewidth)) + 20

def read(file):
    tiled_map.layers
    for x in range(2):
        print(tiled_map.layers[x+1])
    #s = j.splitlines()
    l = []
    #for x in layer:
    #    l.append(x.split(','))

    #for y in range(20):
        #for x in range(40):
    for f in range(2):
        layer = tiled_map.layers[f+1]
        for x, y, image in layer.tiles():
            #print(int(l[y][x])+1)
            #print(image)
            h = Platform(image,(cr(x)-5,cr(y)))#f'assets/tileset/{int(l[y][x])+1}.png'
            asl.add(h)
                    
class Platform(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.surf = pg.transform.scale(image,(32,32))#pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)
class Player(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.surf = image#pg.transform.scale(image,(32,32))#pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)

screen = pg.display.set_mode((cr(40)-20,cr(20)-15))
pg.display.set_caption('rpg')


asl   = pg.sprite.Group()
player = Player(pg.image.load('assets/playerright.png'),(cr(18),cr(10)))


tiled_map = load_pygame('assets/1.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collision = tiled_map.get_layer_by_name('collide')
read('assets/1.lvl')
clock = pg.time.Clock()
running = True
screen.fill(grey)
asl.add(player)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_x or event.key==pg.K_q: #Pressing the x Key will quit the game
                         running=False


    #print(asl)
    for entity in asl:
        screen.blit(entity.surf, entity.rect)


    #screen.fill(black)
    pg.display.flip()
    clock.tick(60)

pg.quit()
