import pygame, sys

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

pygame.init()

size_screen = (1600, 900)
screen = pygame.display.set_mode(size_screen)
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    #---Zona de logica

    #---Zona de logica
    screen.fill(white)
    #---Zona de dibujo
    
    #---Zona de dibujo

    pygame.display.flip()
    clock.tick(60)

pygame.quit()