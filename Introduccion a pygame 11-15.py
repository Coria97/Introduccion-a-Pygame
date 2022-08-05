#Video del 11-16

import pygame, sys, random

#Definimos colores
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

class Meteor(pygame.sprite.Sprite):
    #Clase Meteorito
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        
    
    def set_meteor(self,x,y):
        self.rect.x = random.randrange(x)
        self.rect.y = random.randrange(y)

    def update(self):
        if self.rect.y > size_screen[1]:
            self.rect.y = 0
            self.rect.x = random.randrange(720)
        else:
            self.rect.y += 1

class Player(pygame.sprite.Sprite):
    #Clase jugador
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("nave.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]

class Shoot(pygame.sprite.Sprite):
    #Clase jugador
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -=5

        


#Parametros de inicializacion
pygame.init()
#-Screen
size_screen = (720, 720)
screen = pygame.display.set_mode(size_screen)
background = pygame.image.load("background.png").convert()
#-Reloj
clock = pygame.time.Clock()
#-condicion bucle principal
game_over = False
#-Visibilidad del mouse
pygame.mouse.set_visible = 0
#-Cargar sonido laser
sound = pygame.mixer.Sound("laser_sound.ogg")

#Lista que va a contener a todos los sprites
all_sprite_list = pygame.sprite.Group()

#Lista de meteoritos
meteor_list = pygame.sprite.Group()

#Lista de disparos
shoot_list = pygame.sprite.Group()

#Creo 50 meteoritos y los añado a las listas
for i in range(5):
    meteor = Meteor()
    meteor.set_meteor(720,720)
    meteor_list.add(meteor)
    all_sprite_list.add(meteor)

#Creo jugador y lo añado a la lista
player = Player()
all_sprite_list.add(player)

#-------------------Bucle principal-------------------
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shoot = Shoot()
                shoot.rect.x = player.rect.x + 45
                shoot.rect.y = player.rect.y - 20
                shoot_list.add(shoot)
                all_sprite_list.add(shoot)
                sound.play()


    #---Zona de logica
    all_sprite_list.update()

    for shoot in shoot_list:
        meteor_hit_list = pygame.sprite.spritecollide(shoot,meteor_list,True) # Detecta colisiones entre jugador y meteorito
        for meteor in meteor_hit_list:
            all_sprite_list.remove(shoot)
            all_sprite_list.remove(meteor)
            shoot_list.remove(shoot)
            meteor_list.remove(meteor)
            new_meteor = Meteor()
            new_meteor.set_meteor(720,1)
            meteor_list.add(new_meteor)
            all_sprite_list.add(new_meteor)
        if shoot.rect.y < -10:
            shoot_list.remove(shoot)
    
    
    #---Zona de logica

    screen.blit(background,[0,0])

    #---Zona de dibujo
    all_sprite_list.draw(screen)
    #---Zona de dibujo

    pygame.display.flip()
    clock.tick(60)

pygame.quit()