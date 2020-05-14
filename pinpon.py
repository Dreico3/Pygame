#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 500#aqui colocamos el ancho de la ventana
HEIGHT = 350 #aqui colocamos el alto de la ventana
 
# Clases
# ---------------------------------------------------------------------


class bolaa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = poner_imagen('Imagenes/balon.png', True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.10]
    
    def actualiza(self,time,pala_juga,pala_juga2,puntos):#este es el metodo que permite q la pelota se mueva
        self.rect.centerx += self.speed[0]*time
        self.rect.centery += self.speed[1]*time

        if self.rect.left <= 0: #esto espara controllar los puntos
            puntos[1]+=1
        if self.rect. right >= WIDTH:
            puntos[0]+=1
        if self.rect.centerx<=0 or self.rect.right>=WIDTH:#esto hace que la pelota balla en eje x y si toca el borde del ancho rebota
            self.speed[0]= -self.speed[0]
            self.rect.centerx += self.speed[0]*time
        if self.rect.top<=0 or self.rect.bottom>=HEIGHT:#eje y
            self.speed[1]= -self.speed[1]
            self.rect.centery += self.speed[1]*time
        if pygame.sprite.collide_rect(self, pala_juga): #esto es lo que hace q la pelota choque
            self.speed[0]= -self.speed[0]
            self.rect.centerx += self.speed[1]*time

        if pygame.sprite.collide_rect(self, pala_juga2): #esto es para el jugador dos
            self.speed[0]= -self.speed[0]
            self.rect.centerx += self.speed[1]*time
        return puntos

class pala(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image=poner_imagen('Imagenes/pala.png')
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=HEIGHT/2
        self.speed=0.5
    def mover(self,time,keys):
        if self.rect.top>=0:
            if keys[K_UP]:
                self.rect.centery -= self.speed*time
        if self.rect.bottom<=HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed*time
    def ia(self,time,ball):
        if ball.speed[0]>=0 and ball.rect.centerx>=WIDTH/2:
            if self.rect.centery< ball.rect.centery:
                self.rect.centery +=self.speed*time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self .speed*time



# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def poner_imagen(filename, transparent=False):  #filenane el la ubicacion de la imagen y el otro pregunta si es transparete
        try: 
            image = pygame.image.load(filename)#aqui guardamos nuestra imagen en la variable image
        except pygame.error: #aqui verificamos si hubo error en incertar la imagen
                return "opercion errone"
        image = image.convert() #aqui convertimos la imagen en formato pygame para mejorar la velocidad
        if transparent:#aqui preguntamos si la imagen es transparente
                color = image.get_at((0,0)) #obtiene el color del pixel del la esquina superior
                image.set_colorkey(color, RLEACCEL)#esto lo define como transparente
        return image
   
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))#aqui creamos el tamaño de la pantalla 
    pygame.display.set_caption("Pruebas Pygame")#aqui ponemos el nombre de la ventana
 
    background_image = poner_imagen('Imagenes/fondo.jpg')#aqui ponemos el fondo de la ventana
    bola=bolaa()
    pala_jugador=pala(30)
    pala_jugador2=pala(WIDTH-30)

    clock=pygame.time.Clock()#esto es para crear algo q controle el timepo de juego
    puntos=[0,0]
 
    while True:
        time=clock.tick(60)#aqui colocamos la velocidad de juego
        keys=pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        puntos=bola.actualiza(time,pala_jugador,pala_jugador2,puntos)#aqui actualizamos la piciions de la pelota al pazar el tiempo
        
        pala_jugador.mover(time,keys)
        pala_jugador2.ia(time,bola)

        screen.blit(background_image, (0, 0))
       
        screen.blit(bola.image, bola.rect)
        screen.blit(pala_jugador.image,pala_jugador.rect)#el orden de esto es muy importante
        screen.blit(pala_jugador2.image,pala_jugador2.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
