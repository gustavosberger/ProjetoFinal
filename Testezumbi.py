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
import random


class Vida(pygame.sprite.Sprite):
    
    def __init__(self, arquivo_imagem,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (30,30))
        self.rect = self.image.get_rect() 
        self.rect.x = posX
        self.rect.y= posY
        
        

class Personagem(pygame.sprite.Sprite):
     
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images= []
        ataque= False
        if ataque== False:
            for i in range(0,7):
                img = pygame.image.load(os.path.join('images','__Bandit02_Walk_00' + str(i) + '.png')).convert_alpha()
                img = pygame.transform.scale(img, (95, 150))
                self.images.append(img)
                self.image = self.images[0] 
                self.rect  = self.image.get_rect() 
        if ataque== True:
            for e in range(0,7):
                img = pygame.image.load(os.path.join('03-Attack ','__Bandit02_Attack_00' + str(e) + '.png')).convert_alpha()
                img = pygame.transform.scale(img, (95, 150))
                self.images.append(img)
                self.image = self.images[0]
                self.rect  = self.  image.get_rect()

           
    def controle(self, x, y):
        self.movex += x
        self.movey += y
    
    def update(self):
        ataque= False
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
                
        if ataque== True:
            self.frame+=1
            if self.frames> 3*ani:
                self.frame= 0
            self.image= self.images[self.frame//ani]
            
             
    def gravidade(self, steps):
        speed= 0
        self.rect.y-=steps
        while self.rect.y < 480:
            speed+=1
            self.rect.y+=speed
            
class Zumbi(pygame.sprite.Sprite): 
    def __init__(self,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.frame= 0
        self.images= []
        vivo= True
        morto= False
        if vivo== True:
            for i in range (1,10):
                img = pygame.image.load(os.path.join('go_' + str(i) + '.png')).convert_alpha()
                img = pygame.transform.scale(img, (75, 150))
                self.images.append(img)
                self.image = self.images[0]
                self.rect  = self.image.get_rect()
                self.rect.x = posX
                self.rect.y= posY
        if morto== True:
            for i in range (1,7):
                img = pygame.image.load(os.path.join('die_' + str(i) + '.png')).convert_alpha()
                img = pygame.transform.scale(img, (75, 150))
                self.images.append(img)
                self.image = self.images[0]
                self.rect  = self.image.get_rect()
                self.rect.x = posX
                self.rect.y= posY
    
        

            
    def move(self):
       self.rect.x += self.vx
       self.frame+=1
       if self.frame > 3*ani:
           self.frame= 0
       self.image= self.images[self.frame//ani]
      
        
       
       

ani = 4
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Jogo EP')
fundo = pygame.image.load('fundo-800X600.jpg').convert()
player = Personagem()
player.rect.x = 0
player.rect.y = 480
steps = 10
steps2= 20
char_group = pygame.sprite.Group()
char_group.add(player)



# cria os zumbis
zumbi1 = Zumbi(700, 455, random.randrange(-1,-6,-1))
zumbi1_group = pygame.sprite.Group()
zumbi1_group.add(zumbi1)

zumbi2 = Zumbi(700, 455, random.randrange(-1,-6,-1))
zumbi2_group = pygame.sprite.Group()
zumbi2_group.add(zumbi2)

zumbi3 = Zumbi (700, 455, random.randrange(-1,-6,-1))
zumbi3_group = pygame.sprite.Group()
zumbi3_group.add(zumbi3)

zumbi4 = Zumbi(700, 455, random.randrange(-1,-6,-1))
zumbi4_group = pygame.sprite.Group()
zumbi4_group.add(zumbi4)

zumbi5 = Zumbi(700, 455, random.randrange(-1,-6,-1))
zumbi5_group = pygame.sprite.Group()
zumbi5_group.add(zumbi5)

coracao1= Vida("heart.png",30,50)
coracao1_group= pygame.sprite.Group()
coracao1_group.add(coracao1)

coracao2= Vida("heart.png",70,50)
coracao2_group= pygame.sprite.Group()
coracao2_group.add(coracao2)

coracao3= Vida("heart.png",110,50)
coracao3_group= pygame.sprite.Group()
coracao3_group.add(coracao3)


relogio =pygame.time.Clock()

i=0
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
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi1):
                ataque= True
                normal= False
                zumbi1 = Zumbi( 800, 455, random.randrange(-1,-6,-1))
                zumbi1_group = pygame.sprite.Group()
                zumbi1_group.add(zumbi1)
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi2):
                ataque= True  
                normal= False
                zumbi2 = Zumbi( 800, 455, random.randrange(-1,-6,-1))
                zumbi2_group = pygame.sprite.Group()
                zumbi2_group.add(zumbi2)
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi3):
                ataque= True
                normal= False
                zumbi3 = Zumbi( 800, 455, random.randrange(-1,-6,-1))
                zumbi3_group = pygame.sprite.Group()
                zumbi3_group.add(zumbi3)
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi4):
                ataque= True
                normal= False
                zumbi4 = Zumbi( 800, 455, random.randrange(-1,-6,-1))
                zumbi4_group = pygame.sprite.Group()
                zumbi4_group.add(zumbi1)
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi5):
                ataque= True
                normal= False
                zumbi5 = Zumbi( 800, 455, random.randrange(-1,-6,-1))
                zumbi5_group = pygame.sprite.Group()
                zumbi5_group.add(zumbi5)
                
                

                    
                
                
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.controle(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.controle(-steps,0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
                
        if pygame.sprite.collide_rect(player,zumbi1) or pygame.sprite.collide_rect(player,zumbi2) or pygame.sprite.collide_rect(player,zumbi3) or pygame.sprite.collide_rect(player,zumbi4)or pygame.sprite.collide_rect(player,zumbi5):
            i+=1
            if i== 1:
                coracao1= Vida("heart.png",800,800)
                coracao1_group= pygame.sprite.Group()
                coracao1_group.add(coracao1)
            elif i== 2:
                coracao2= Vida("heart.png",800,800)
                coracao2_group= pygame.sprite.Group()
                coracao2_group.add(coracao2)
            elif i== 3: 
                coracao3= Vida("heart.png",800,800)
                coracao3_group= pygame.sprite.Group()
                coracao3_group.add(coracao3)
                rodando= False
                
                
            

                
        
                
    
                
    #gera saídas  
    
    tela.blit(fundo, (0, 0))
    player.update()
    char_group.draw(tela)
    zumbi1_group.draw(tela)
    zumbi2_group.draw(tela)
    zumbi3_group.draw(tela)
    zumbi4_group.draw(tela)
    zumbi5_group.draw(tela) 
    coracao1_group.draw(tela)
    coracao2_group.draw(tela)
    coracao3_group.draw(tela)
    pygame.display.update()
    
pygame.display.quit()