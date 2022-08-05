#Video del 16

import pygame, sys, random

#Definimos constantes
size_screen = (720, 720)
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
            self.rect.x = random.randrange(size_screen[0])
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

class Game(object):
    def __init__(self):
        #Inicializo el juego
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        for i in range(5):
            meteor = Meteor()
            meteor.set_meteor(size_screen[0],size_screen[1])
            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)
        self.player = Player()
        self.all_sprite_list.add(self.player)

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def runLogic(self):
        self.all_sprite_list.update()
        meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)

    def displayFrame(self, screen):
        screen.fill(white)
        self.all_sprite_list.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    clock = pygame.time.Clock()
    done = False
    game = Game()

    while not done:
        done = game.processEvents()
        game.runLogic()
        game.displayFrame(screen)
        clock.tick(60)

    pygame.quit()
    
if __name__ == "__main__":
    main()

