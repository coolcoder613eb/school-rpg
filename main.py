import pygame as pg
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
pg.init()


def cr(num):
    return ((num * tilewidth)*2) + 20


black = (0,0,0)
white = (255,255,255)
grey = (137,137,137)

tilewidth = 32
width = cr(44/2)
height = cr(24/2)

vec = pg.math.Vector2



def read(file,startx,starty,endx,endy):
    tiled_map.layers
    #for x in range(3):
        #print(tiled_map.layers[x])
    #s = j.splitlines()
    #l = []
    #for x in layer:
    #    l.append(x.split(','))

    #for y in range(20):
        #for x in range(40):
    layer = tiled_map.layers[0]
    for x, y, image in layer.tiles():
        #print(int(l[y][x])+1)
        #print(image)
        if cr(x) >= startx and cr(x) <= endx and cr(y) >= starty and cr(y) <= endy: 
            h = Platform(image,((cr(x))-startx,cr(y)-starty))#f'assets/tileset/{int(l[y][x])+1}.png'
            collide.add(h)
    for f in range(2):
        layer = tiled_map.layers[f+1]
        for x, y, image in layer.tiles():
            #print(int(l[y][x])+1)
            #print(image)
            if cr(x) >= startx and cr(x) <= endx and cr(y) >= starty and cr(y) <= endy:
                h = Platform(image,((cr(x))-startx,(cr(y))-starty))#f'assets/tileset/{int(l[y][x])+1}.png'
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
        self.npos = vec(coords[0], coords[1])
        self.img = image
        self.surf = image#pg.transform.scale(image,(32,32))#pg.image.load(image).convert_alpha()
        self.rect = self.surf.get_rect(center = coords)
        self.nrect = self.surf.get_rect(center = coords)
    def update(self):
        #print('npos1 ',self.npos,'\nnrect1 ',self.nrect)
        #'\nrect1 ',self.rect)
        self.npos = vec(self.pos)
        self.nrect.center = self.rect.center
        
        PRESSED = pg.key.get_pressed()
        #print('pos1 ',self.pos,)
        if PRESSED[pg.K_LEFT]:
            self.npos[0]-=2
            self.surf = pg.transform.rotate(self.img,180)
            self.rect = self.surf.get_rect(center = self.rect.center)
            self.nrect = self.surf.get_rect(center = self.nrect.center)
        if PRESSED[pg.K_RIGHT]:
            self.npos[0]+=2
            self.surf = pg.transform.rotate(self.img,0)
            self.rect = self.surf.get_rect(center = self.rect.center)
            self.nrect = self.surf.get_rect(center = self.nrect.center)
        if PRESSED[pg.K_UP]:
            self.npos[1]-=2
            self.surf = pg.transform.rotate(self.img,90)
            self.rect = self.surf.get_rect(center = self.rect.center)
            self.nrect = self.surf.get_rect(center = self.nrect.center)
        if PRESSED[pg.K_DOWN]:
            self.npos[1]+=2
            self.surf = pg.transform.rotate(self.img,-90)
            self.rect = self.surf.get_rect(center = self.rect.center)
            self.nrect = self.surf.get_rect(center = self.nrect.center)
        
        #print('pos2 ',self.pos,'\n')
        self.nrect.center = (self.npos.x,self.npos.y)
        if not pg.sprite.spritecollide(player,collide,False,collided = self.check):
            self.pos = vec(self.npos)
            self.rect.center = self.nrect.center
        self.nrect.center = self.rect.center
        print((self.pos.x-cr(12),self.pos.y-cr(7),self.pos.x+cr(13),self.pos.y+cr(8)))
        asl.empty()
        collide.empty()
        read('assets/1.lvl',self.pos.x-cr(12),self.pos.y-cr(7),self.pos.x+cr(13),self.pos.y+cr(8))
        #asl.add(self)
##        if self.pos.y > cr(11) and self.pos.x < cr(20):
##            read('assets/1.lvl',cr(0),cr(10),width,cr(10)+height)
##        elif self.pos.y < cr(9) and self.pos.x < cr(20):
##            read('assets/1.lvl',cr(0),cr(0),width,height)
##        elif self.pos.y > cr(11) and self.pos.x > cr(22):
##            read('assets/1.lvl',cr(21),cr(10),cr(21)+width,cr(10)+height)
##        elif self.pos.y < cr(9) and self.pos.x > cr(22):
##            read('assets/1.lvl',cr(21),cr(0),cr(21)+width,height)
        asl.add(self)
        #print()
        
        
    def check(self,s,o):
        if s.nrect.colliderect(o.rect):
            return True
        else:
            return False

screen = pg.display.set_mode((width,height),RESIZABLE)
pg.display.set_caption('rpg')


asl   = pg.sprite.Group()
player = Player(pg.image.load('assets/bachur1.png'),(cr(11),cr(6)))#playerright1


collide = pg.sprite.Group()

tiled_map = load_pygame('assets/1.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collision = tiled_map.get_layer_by_name('collide')
read('assets/1.lvl',0,0,width,height)
clock = pg.time.Clock()
running = True

asl.add(player)
screen = pg.display.set_mode((width,height),RESIZABLE)

screen.fill(grey)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_x or event.key==pg.K_q: #Pressing the x Key will quit the game
                         running=False

    screen.fill(grey)


    


    #print(asl)
    for entity in asl:
        screen.blit(entity.surf, entity.rect)
    player.update()


    #screen.fill(black)
    pg.display.flip()
    clock.tick(60)


pg.quit()
input()
