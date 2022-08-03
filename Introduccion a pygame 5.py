#Animacion lluvia video 5

import pygame, sys, random

white = (255,255,255)
blue = (0,0,255)

pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coord_list = []
for i in range(60):
        x = random.randint(0,800)
        y = random.randint(0,500)
        coord_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)

    for coord in coord_list:
        pygame.draw.circle(screen,blue,coord,2)
        coord[1] += 1
        if coord[1] > 500:
            coord[1] = 0
    
    pygame.display.flip()
    clock.tick(60)