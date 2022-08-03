#Pong game - Video 8

import pygame, sys

# Definicion de colores
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)

#Inicializacion de reloj , pantalla y gameover
pygame.init()
size_screen = (800, 500)
screen = pygame.display.set_mode(size_screen)
clock = pygame.time.Clock()
game_over = False

#Definicion de caracteristicas sobre los player
player_width = 15
player_height = 90
player_1_x = 50
player_1_y = 200
player_2_x = 735
player_2_y = 200
player_1_speed_y = 0
player_2_speed_y = 0

#Definicion de la pelota
ball_x = 400
ball_y = 250
ball_r = 10
ball_speed_x = 3
ball_speed_y = 3


#Jugar
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        #Detectar movimiento jugador 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_1_speed_y -= 3
            if event.key == pygame.K_d:
                player_1_speed_y += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_1_speed_y = 0
            if event.key == pygame.K_d:
                player_1_speed_y = 0
        
        #Detectar movimiento jugador 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_2_speed_y -= 3
            if event.button == 3:
                player_2_speed_y += 3
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                player_2_speed_y = 0
            if event.button == 3:
                player_2_speed_y = 0

    #Movimiento jugadores
    if (player_1_y  + player_1_speed_y > 0) and (player_1_y + player_1_speed_y < 410):
        player_1_y += player_1_speed_y
    if (player_2_y  + player_2_speed_y > 0) and (player_2_y + player_2_speed_y < 410):
        player_2_y += player_2_speed_y

    #Movimiento pelota
    if (ball_y < 10) or (ball_y > 490): #Rebote de la pelota
        ball_speed_y *= -1
    if (ball_x < 0): # Jugador 1 perdio
        ball_x = 400
        ball_y = 250
        ball_speed_x *= -1
        ball_speed_y *= -1
    if (ball_x > 800): # Jugador 2 perdio
        ball_x = 400
        ball_y = 250
        ball_speed_x *= -1
        ball_speed_y *= -1
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(white)

    # Creacion de jugadores y pelota
    player_1 = pygame.draw.rect(screen, black, (player_1_x, player_1_y, player_width, player_height))
    player_2 = pygame.draw.rect(screen, black, (player_2_x, player_2_y, player_width, player_height))
    ball = pygame.draw.circle(screen, blue, (ball_x,ball_y), ball_r)

    # Colisiones
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball_speed_y *= -1
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()