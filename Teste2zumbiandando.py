#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:47:15 2018

@author: Gustavo
"""

import pygame
import sys
from pygame.locals import *



class Zumbi1(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx
    
    
    
class Zumbi2(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx
       
     
        
class Zumbi3(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx
      
     
        
class Zumbi4(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = [posX]
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx
       
       
   
    
class Zumbi5(pygame.sprite.Sprite):
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.image = pygame.image.load(arquivo_imagem)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx
       
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Jogo Zumbis')

# carrega imagem de fundo (https://wallpapersafari.com/dark-green-background/)
fundo = pygame.image.load("fundo-800X600.jpg").convert()




rodando = True

# ======= Loop principal ======
while rodando:
    for event in pygame.event.get(): 
      if event.type == QUIT: 
        rodando = False
    distancia_percorrida1= 0
    distancia_percorrida2= 0
    
    # ======= Loop para mudar de fase======
    while distancia_percorrida2 < 10000:

        # ======= Loop imagem 1 ======      
        if 0 <= distancia_percorrida1 < 1:
            zumbi1 = Zumbi1("go_1.png", 700, 300, -1)
            zumbi1_group = pygame.sprite.Group()
            zumbi1_group.add(zumbi1)
            
            zumbi1.move()
            if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
            distancia_percorrida1+= zumbi1.rect.x
            distancia_percorrida2+= zumbi1.rect.x
            tela.blit(fundo, (0, 0))
            zumbi1_group.draw(tela)
            pygame.display.update()  
       
        
        
        # ======= Loop imagem 2 ======   
        elif 1<= distancia_percorrida1< 2:
           zumbi1 = Zumbi1("go_2.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
            
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()  
           
           
           
        # ======= Loop imagem 3 ======       
        elif 2<= distancia_percorrida1 < 3:
           zumbi1 = Zumbi1("go_3.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                      
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
            
        
        # ======= Loop imagem 4 ======   
        elif 3<= distancia_percorrida1< 4:
           zumbi1 = Zumbi1("go_4.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                       
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
           
        
        # ======= Loop imagem 5 ======   
        elif 4<= distancia_percorrida1< 5:
           zumbi1 = Zumbi1("go_5.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                       
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
          
        
        # ======= Loop imagem 6 ======   
        elif 5<= distancia_percorrida1< 6:
           zumbi1 = Zumbi1("go_6.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                       
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
           

          
        # ======= Loop imagem 7 ======      
        elif 6<= distancia_percorrida1< 7:
           zumbi1 = Zumbi1("go_7.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
            
           
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
           
        
        # ======= Loop imagem 8 ======   
        elif 7<= distancia_percorrida1< 8:
           zumbi1 = Zumbi1("go_8.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                       
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
         
        
        # ======= Loop imagem 9 ======   
        elif 8<= distancia_percorrida1< 9:
           zumbi1 = Zumbi1("go_9.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
                       
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()
          
        
        # ======= Loop imagem 10 ======   
        elif 9<= distancia_percorrida1< 10:
           zumbi1 = Zumbi1("go_10.png", 700, 300, 1)
           zumbi1_group = pygame.sprite.Group()
           zumbi1_group.add(zumbi1)
            
           zumbi1.move()
           if zumbi1.rect.x == -200:
              zumbi1.rect.x= 800
           distancia_percorrida1+= zumbi1.rect.x
           distancia_percorrida2+= zumbi1.rect.x
           tela.blit(fundo, (0, 0))
           zumbi1_group.draw(tela)
           pygame.display.update()


        else:
            distancia_percorrida1= 0
            
    
             
    
        
    #gera saídas
    tela.blit(fundo, (0, 0))
    zumbi1_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()

