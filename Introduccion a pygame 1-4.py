#Video del 1-4

#importa la libreria
import pygame, sys

#Inicializa la libreria
pygame.init()

#Primero definicimos una ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

#Define reloj para controlar los frame por seg
reloj = pygame.time.Clock()

#Definir colores
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

#Definimos coordenadas para el cuadrado
coord_x = 400
coord_y = 200
#Definimos la velocidad a la que se movera mi cuadrado
speed_x = 3
speed_y = 3

while True:
    #Registra todos los eventos que estan pasando en mi ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si el evento es de salir, cierra la ventana
            sys.exit()

    ### ----------- ZONA DE LOGICA
    #Aumenta la coord en x del cuadrado para generar un movimiento
    coord_x = coord_x + speed_x


    #Coloca color de fondo en la pantalla
    screen.fill(white)
    
    ### ----------- ZONA DE DIBUJO (siempre despues de pintar la pantalla)

    #Coloca una linea en la pantalla, line(pantalla donde dibuja, color, donde inicia y termina horizontalmente , donde inicia y termina verticalmente, grosor)
    #pygame.draw.line(screen, green, [0,100], [100,200], 5)

    ##Coloca un cuadrado en la pantalla, rect(pantalla donde dibuja, color, (punto de inicio en x e y, ancho, alto))
    #pygame.draw.rect(screen, black,(100,100,80,80))

    #Loops para dibujar 
    #for i in range(100,700,100):
    #    pygame.draw.rect(screen, black, (x, 230, 50, 50))
    pygame.draw.rect(screen, black,(coord_x,coord_y,speed_x,speed_y))

    ### ----------- ZONA DE DIBUJO

    #Actualiza la pantalla
    pygame.display.flip()

    #Define los frames por segundos
    reloj.tick(60)