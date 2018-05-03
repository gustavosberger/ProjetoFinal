#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:47:15 2018

@author: Gustavo
"""

import pygame
import sys
from pygame.locals import *


#inicializando
pygame.init()
tela = pygame.display.set_mode(800,600)
pygame.display.set_caption("day z")
# adicionando fundo
fundo = pygame.image.load("fundopygame.jpg").convert()







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
       


# cria os zumbis
zumbi1 = Zumbi1("go_5.png", 700, 300, 1)
zumbi1_group = pygame.sprite.Group()
zumbi1_group.add(zumbi1)

zumbi2 = Zumbi2("go_1.png", 700, 300, 1.4)
zumbi2_group = pygame.sprite.Group()
zumbi2_group.add(zumbi2)

zumbi3 = Zumbi3("go_4.png", 700, 300, 2)
zumbi3_group = pygame.sprite.Group()
zumbi3_group.add(zumbi3)

zumbi4 = Zumbi4("go_7.png", 700, 300, 3)
zumbi4_group = pygame.sprite.Group()
zumbi4_group.add(zumbi4)

zumbi5 = Zumbi5("go_10.png", 700, 300, 4)
zumbi5_group = pygame.sprite.Group()
zumbi5_group.add(zumbi5)



rodando = True
while rodando:
    for event in pygame.event.get(): 
      if event.type == QUIT: 
        rodando = False
    zumbi1.move()
    if zumbi1.rect.x < 0 or zumbi1.rect.x > 800:
      zumbi1.vx = - zumbi1.vx
    zumbi2.move()
    if zumbi2.rect.x < 0 or zumbi2.rect.x > 800:
        zumbi2.vx = - zumbi2.vx
    zumbi3.move()
    if zumbi3.rect.x<0 or zumbi3.rect.x > 800:
        zumbi3.vx = -zumbi3.vx
    zumbi4.move()
    if zumbi4.rect.x<0 or zumbi4.rect.x > 800:
        zumbi4.vx = -zumbi4.vx
    zumbi5.move()
    if zumbi5.rect.x<0 or zumbi5.rect.x > 800:
        zumbi5.vx = -zumbi5.vx
        
    
         
    
        
    #gera saídas
    tela.blit(fundo, (0, 0))
    zumbi1_group.draw(tela)
    zumbi2_group.draw(tela)
    zumbi3_group.draw(tela)
    zumbi4_group.draw(tela)
    zumbi5_group.draw(tela)
    pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()



