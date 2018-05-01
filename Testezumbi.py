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
        self.rect.x = posX
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

# cria os zumbis
zumbi1 = Zumbi1("bola-25X25.png", 700, 300, 1)
zumbi1_group = pygame.sprite.Group()
zumbi1_group.add(zumbi1)

zumbi2 = Zumbi2("bola-25X25.png", 700, 300, 1.1)
zumbi2_group = pygame.sprite.Group()
zumbi2_group.add(zumbi2)



rodando = True
while rodando:
    for event in pygame.event.get(): 
      if event.type == QUIT: 
        rodando = False
    zumbi1.move()
    if zumbi1.rect.x < 0 or zumbi1.rect.x > 800:
      zumbi1.vx = - zumbi1.vx
    if zumbi1.rect.x > 0:
       zumbi2.move()
       if zumbi2.rect.x < 0 or zumbi2.rect.x > 800:
           zumbi2.vx = - zumbi2.vx
        
    
         
    
        
    #gera saídas
    tela.blit(fundo, (0, 0))
    zumbi1_group.draw(tela)
    zumbi2_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()



