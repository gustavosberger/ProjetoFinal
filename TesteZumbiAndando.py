#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:47:15 2018
@author: Gustavo
"""

import pygame
import sys
from pygame.locals import *
import os


class Personagem(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images= []
        self.jumping= False
        self.jump_offset= 0
        for i in range(0,7):
            img = pygame.image.load(os.path.join('images','__Bandit02_Walk_00' + str(i) + '.png')).convert_alpha()
            img = pygame.transform.scale(img, (95, 150))
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

         
    def controle(self, x, y):
        self.movex += x
        self.movey += y
        
        
    
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[(self.frame//ani)+1]
            
            
class Zumbi(pygame.sprite.Sprite): 
    def __init__(self, arquivo_imagem,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        image = pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (75,150))
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY
    
    def move(self):
       self.rect.x += self.vx

ani = 4 
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Jogo EP')
fundo = pygame.image.load('fundo-800X600.jpg').convert()
player = Personagem()
player.rect.x = 0
player.rect.y = 480
steps = 10
char_group = pygame.sprite.Group()
char_group.add(player)



# cria os zumbis
zumbi1 = Zumbi("go_1.png", 700, 455, -1)
zumbi1_group = pygame.sprite.Group()
zumbi1_group.add(zumbi1)

zumbi2 = Zumbi("go_1.png", 700, 455, -2)
zumbi2_group = pygame.sprite.Group()
zumbi2_group.add(zumbi2)

zumbi3 = Zumbi("go_1.png", 700, 455, -1.8)
zumbi3_group = pygame.sprite.Group()
zumbi3_group.add(zumbi3)

zumbi4 = Zumbi("go_1.png", 700, 455, -3)
zumbi4_group = pygame.sprite.Group()
zumbi4_group.add(zumbi4)

zumbi5 = Zumbi("go_1.png", 700, 455, -2.6)
zumbi5_group = pygame.sprite.Group()
zumbi5_group.add(zumbi5)

relogio =pygame.time.Clock()


rodando = True
while rodando:
    tempo = relogio.tick(30)
    zumbi1.move()
    if zumbi1.rect.x == -200:
        zumbi1.rect.x= 800
    zumbi2.move()
    if zumbi2.rect.x == -200:
        zumbi2.rect.x= 800
    zumbi3.move()
    if zumbi3.rect.x== -200:
        zumbi3.rect.x= 800
    zumbi4.move()
    if zumbi4.rect.x== -200:
        zumbi4.rect.x= 800
    zumbi5.move()
    if zumbi5.rect.x== -200:
        zumbi5.rect.x= 800

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            rodando = False
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.controle(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.controle(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.controle(0,-steps)
                
                
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.controle(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.controle(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
                
        if player.rect.x== 0:
            player.rect.x= 800
    
                
    #gera saídas
    
    tela.blit(fundo, (0, 0))
    player.update()
    char_group.draw(tela)
    zumbi1_group.draw(tela)
    zumbi2_group.draw(tela)
    zumbi3_group.draw(tela)
    zumbi4_group.draw(tela)
    zumbi5_group.draw(tela)            
    pygame.display.update()
    
pygame.display.quit()