import pygame as pg
import pytmx
from pytmx.util_pygame import load_pygame
pg.init()



black = (0,0,0)
white = (255,255,255)
grey = (137,137,137)

tilewidth = 32

vec = pg.math.Vector2

def cr(num):
    return ((num * tilewidth)*2) + 20

def read(file,startx,starty,endx,endy):
    tiled_map.layers
    for x in range(3):
        print(tiled_map.layers[x])
    #s = j.splitlines()
    l = []
    #for x in layer:
    #    l.append(x.split(','))

    #for y in range(20):
        #for x in range(40):
    layer = tiled_map.layers[0]
    for x, y, image in layer.tiles():
        #print(int(l[y][x])+1)
        #print(image)
        if x >= startx and x <= endx and y >= starty and y <= endy: 
            h = Platform(image,(cr(x)-5,cr(y)))#f'assets/tileset/{int(l[y][x])+1}.png'
            collide.add(h)
    for f in range(2):
        layer = tiled_map.layers[f+1]
        for x, y, image in layer.tiles():
            #print(int(l[y][x])+1)
            #print(image)
            if x >= startx and x <= endx and y >= starty and y <= endy:
                h = Platform(image,(cr(x)-5,cr(y)))#f'assets/tileset/{int(l[y][x])+1}.png'
                asl.add(h)
                    
class Platform(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.surf = pg.transform.scale(image,(64,64))#pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)
class Player(pg.sprite.Sprite):
    def __init__(self,image,coords):
        super().__init__()
        self.vel = vec(0, 0)
        self.pos = vec(coords[0], coords[1])
        self.surf = image#pg.transform.scale(image,(32,32))#pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)
    def update():
        PRESSED = pygame.key.get_pressed()

        if PRESSED[pygame.K_LEFT]:
            pos[0]-=10
        elif PRESSED[pygame.K_RIGHT]:
            pos[0]+=10
        if PRESSED[pygame.K_UP]:
            pos[1]-=10
        elif PRESSED[pygame.K_DOWN]:
            pos[1]+=10  

screen = pg.display.set_mode((cr(40/2)-20,cr(20/2)-15))
pg.display.set_caption('rpg')


asl   = pg.sprite.Group()
player = Player(pg.image.load('assets/playerright.png'),(cr(14),cr(6)))


collide = pg.sprite.Group()

tiled_map = load_pygame('assets/1.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collision = tiled_map.get_layer_by_name('collide')
read('assets/1.lvl',0,0,20,10)
clock = pg.time.Clock()
running = True

asl.add(player)
screen = pg.display.set_mode((cr(40/2)-20,cr(20/2)-15))

screen.fill(grey)

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
