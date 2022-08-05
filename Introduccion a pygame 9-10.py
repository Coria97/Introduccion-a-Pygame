#Video del 9-10
import pygame, sys

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

pygame.init()

size_screen = (1600, 900)
screen = pygame.display.set_mode(size_screen)
clock = pygame.time.Clock()
game_over = False
pygame.mouse.set_visible = 0

# Cargo las imagenes 
background = pygame.image.load("fondo.png").convert()
player = pygame.image.load("space-station.png").convert()
#Le quito el color de fondo al player
player.set_colorkey(white) 

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    #---Zona de logica
    coord_mouse = pygame.mouse.get_pos()
    coord_x = coord_mouse[0]
    coord_y = coord_mouse[1]
    #---Zona de logica
    screen.blit(background,[0, 0])
    screen.blit(player,[coord_x,coord_y])
    #---Zona de dibujo

    #---Zona de dibujo

    pygame.display.flip()
    clock.tick(60)

pygame.quit()