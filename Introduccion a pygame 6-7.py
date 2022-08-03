#Video 6 - 7

import pygame, sys

white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

pygame.init()

#Para ocultar el mouse en la pantalla
pygame.mouse.set_visible(0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x_teclado = 10
y_teclado = 10
x_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Obtiene la tecla que se aprieta
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed -= 3
            if event.key == pygame.K_d:
                x_speed += 3
        #Obtiene la tecla que se deja de apretar
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_speed = 0
            if event.key == pygame.K_d:
                x_speed = 0

    #Obtiene la posicion del mouse (x,y)
    mouse_pos = pygame.mouse.get_pos()
    x_mouse = mouse_pos[0]
    y_mouse = mouse_pos[1]
    x_teclado += x_speed
    screen.fill(white)
    pygame.draw.rect(screen,black,(x_teclado,y_teclado,50,50))
    pygame.draw.rect(screen,blue,(x_mouse,y_mouse,50,50))
    pygame.display.flip()
    clock.tick(60)