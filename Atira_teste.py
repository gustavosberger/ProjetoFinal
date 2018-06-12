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


#======================================= Classes ============================================
morto = False
gun = False
black= (255,255,255)
vermelho= (238,44,44)
#======= Poder especial ==========
#class Especial(pygame.sprite.Sprite):

#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self)
#        self.gravity= 0.4
#        self.velocity = 0
#        self.isJumping = False
#        self.movex = 0
#        self.movey = 0
#        self.frame = 0
#        self.images= []
#        for i in range(0,7):
#            img = pygame.image.load(os.path.join('JK_P_Gun__Run_00' + str(i) + '.png')).convert_alpha()
#            img = pygame.transform.scale(img, (70, 100))
#            self.images.append(img)
#            self.image = self.images[0]
#            self.rect  = self.image.get_rect()
#
#
#    def controle(self, x, y):
#        self.movex += x
#        self.movey += y
#
#    def update(self):
#        self.rect.x = self.rect.x + self.movex
#        self.rect.y = self.rect.y + self.movey
#        if self.movex < 0:
#            self.frame += 1
#            if self.frame > 3*ani:
#                self.frame = 0
#            self.image = self.images[self.frame//ani]
#
#        if self.movex > 0:
#            self.frame += 1
#            if self.frame > 3*ani:
#                self.frame = 0
#            self.image = self.images[(self.frame//ani)+1]
#
#======== Vida do zombie ==========
class Dano(pygame.sprite.Sprite):

    def __init__ (self, arquivo_imagem,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        image= pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (30,30)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = Zumbi.rect.x


#======== Tiro ============
class Tiro(pygame.sprite.Sprite):

    def __init__(self, arquivo_imagem,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.x= posX
        self.rect.y= posY + 80

    def move(self,Vx):
        self.rect.x += Vx



#========= Placar ===========
def Pontuacao(score):
    font= pygame.font.SysFont(None,25)
    text= font.render("Zombies Killed : "+ str(score), True, black)
    tela.blit(text,(30,90))




#========= Coração ===========
class Vida(pygame.sprite.Sprite):

    def __init__(self, arquivo_imagem,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y= posY


#========== Personagem =========
class Personagem(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.gravity= 0.4
        self.velocity = 0
        self.isJumping = False
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images= []
        for i in range(0,9):
            img = pygame.image.load(os.path.join('JK_P_Gun__Run_00' + str(i) + '.png')).convert_alpha()
            img = pygame.transform.scale(img, (70, 130))
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

        self.frame += 1
        if self.frame > 3*ani:
            self.frame = 0
        self.image = self.images[self.frame//ani]


#============= Zumbi ===============
class Zumbi(pygame.sprite.Sprite):
    def __init__(self,posX,posY,velX):
        pygame.sprite.Sprite.__init__(self)
        self.vx= velX
        self.frame= 0
        self.images= []
        if morto == False:
            for i in range(1,10):
                img = pygame.image.load(os.path.join('go_' + str(i) + '.png')).convert_alpha()
                if pontos != 20:
                    img = pygame.transform.scale(img, (75, 150))
                if pontos == 20:
                    img= pygame.transform.scale(img,(150,300))
                self.images.append(img)
                self.image = self.images[0]
                self.rect  = self.image.get_rect()
                self.rect.x = posX
                self.rect.y= posY
        elif morto == True:
            for e in range (1,8):
                img = pygame.image.load(os.path.join('images','die_' + str(i) + '.png')).convert_alpha()
                if pontos != 20:
                    img = pygame.transform.scale(img, (75, 150))
                if pontos == 20:
                    img= pygame.transform.scale(img,(150,300))
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


    def die(self):
        self.frame+=1
        if self.frame > 3*ani:
            self.frame= 0
        self.image= self.imagea[self.frame//ani]




#=========== Fundo ============
class Background(pygame.sprite.Sprite):
    def __init__(self, imagem, x, y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = vel_x

    def move(self):
        if self.rect.x >= -3202:
            self.rect.x -= self.vel_x
        else:
            self.rect.x = 3202


#=========== Obstáculo ==============
class Prop(pygame.sprite.Sprite):


    def __init__(self, arquivo_imagem,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(arquivo_imagem)
        self.image= pygame.transform.scale (image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    def move(self,Vx):
        self.rect.x += Vx




pontos= 0
ani = 4
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Jogo EP')
player = Personagem()
player.rect.x = 0
player.rect.y = 375
#power= Especial()
#power.rect.x= 400
#power.rect.y=480
steps = 12
steps2= 12
char_group = pygame.sprite.Group()
char_group.add(player)
power_group= pygame.sprite.Group()
#power_group.add(power)





#===============================Cria os Sprites =======================================


#========Zumbis=========
zumbi1 = Zumbi(700, 350, random.randrange(-4,-10,-1))
zumbi1_group = pygame.sprite.Group()
zumbi1_group.add(zumbi1)

zumbi2 = Zumbi(700, 350, random.randrange(-4,-10,-1))
zumbi2_group = pygame.sprite.Group()
zumbi2_group.add(zumbi2)

zumbi3 = Zumbi (700, 350, random.randrange(-4,-10,-1))
zumbi3_group = pygame.sprite.Group()
zumbi3_group.add(zumbi3)

zumbi4 = Zumbi(700, 350, random.randrange(-4,-10,-1))
zumbi4_group = pygame.sprite.Group()
zumbi4_group.add(zumbi4)

zumbi5 = Zumbi(700, 350, random.randrange(-4,-10,-1))
zumbi5_group = pygame.sprite.Group()
zumbi5_group.add(zumbi5)

#======== ZUMBIZÃO ==========
zumbizao= Zumbi(900, 10, -2)
zumbizao_group= pygame.sprite.Group()
zumbizao_group.add(zumbizao)

#========Corações=========
coracao1= Vida("heart.png",30,50)
coracao1_group= pygame.sprite.Group()
coracao1_group.add(coracao1)

coracao2= Vida("heart.png",70,50)
coracao2_group= pygame.sprite.Group()
coracao2_group.add(coracao2)

coracao3= Vida("heart.png",110,50)
coracao3_group= pygame.sprite.Group()
coracao3_group.add(coracao3)


#===========Fundo============
background = Background('fundo_bergao.png',0,0,3)
background1 = Background('fundo_bergao.png',0,3202,3)
background_group = pygame.sprite.Group()
background_group.add(background)
background_group.add(background1)


#==========Tiro=============
tiro= Tiro('Bullet.png',900, 10)
tiro_group= pygame.sprite.Group()
tiro_group.add(tiro)


#==========Obstáculo=============
obst1 = Prop('flame.png', 600, 420)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obst1)


relogio =pygame.time.Clock()
speed= 2
distancia=0
i=0
rodando = True

#============================== Loop principal ==========================================
while rodando:
    if player.rect.y < 375:
        player.gravity= 1.2
    else:
        player.rect.y = 375
        player.gravity= 0

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
    if pontos == 20 or pontos == 30:
          zumbizao.move()

    #=========== Pulo =============
    player.rect.y += player.velocity
    player.velocity += player.gravity

    #========Tiro e obstáculo (mexer)=======

    tiro.move(20)
    obst1.move(-2)
    if obst1.rect.x < 0:
        obst1 = Prop('flame.png', 900, 420)
        obstacle_group = pygame.sprite.Group()
        obstacle_group.add(obst1)

    #========== Loop das teclas ==========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            rodando = False


        #================= KeyDown ==============
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.controle(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.controle(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.controle(0,-steps2)


            #===== Pressionar barra de espaço ====
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi1):
                zumbi1.kill()
                zumbi1 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi1_group = pygame.sprite.Group()
                zumbi1_group.add(zumbi1)
                pontos+= 1
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi2):
                zumbi2.kill()
                zumbi2 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi2_group = pygame.sprite.Group()
                zumbi2_group.add(zumbi2)
                pontos+= 1
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi3):
                zumbi3.kill()
                zumbi3 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi3_group = pygame.sprite.Group()
                zumbi3_group.add(zumbi3)
                pontos+= 1
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi4):
                zumbi4.kill()
                zumbi4 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi4_group = pygame.sprite.Group()
                zumbi4_group.add(zumbi1)
                pontos+= 1
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbi5):
                zumbi5.kill()
                zumbi5 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi5_group = pygame.sprite.Group()
                zumbi5_group.add(zumbi5)
                pontos+= 1
            if event.key == pygame.K_SPACE and pygame.sprite.collide_rect(player,zumbizao):
                zumbizao= Zumbi(Zumbi.rect.x-10,100, -2)
                zumbizao_group = pygame.sprite.Group()
                zumbizao_group.add(zumbizao)


            #============= Barra de Espaço (Tiro) ==================
            if event.key == pygame.K_SPACE:
                tiro= Tiro('Bullet.png',player.rect.x, player.rect.y)
                tiro_group= pygame.sprite.Group()
                tiro_group.add(tiro)




        #===============KeyUp===============
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.controle(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.controle(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.controle(0,-steps)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

        #==============Collide=============
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
                pontos= 0
                i= 0

                zumbi1 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi1_group = pygame.sprite.Group()
                zumbi1_group.add(zumbi1)
                zumbi2 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi2_group = pygame.sprite.Group()
                zumbi2_group.add(zumbi2)
                zumbi3 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi3_group = pygame.sprite.Group()
                zumbi3_group.add(zumbi3)
                zumbi4 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
                zumbi4_group = pygame.sprite.Group()
                zumbi4_group.add(zumbi1)
                zumbi5 = Zumbi( 800, 350, random.randrange(-6,-15,-1))
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

                player = Personagem()
                player.rect.x = 0
                player.rect.y = 375
                char_group = pygame.sprite.Group()
                char_group.add(player)









#                tela.fill(vermelho)
#                font= pygame.font.SysFont(None,25)
#                text= font.render("Para jogar novamente pressione 'x'",True, black)
#                tela.blit(text,(30,90))
#                font= pygame.font.SysFont(None,25)
#                text= font.render(("Para sair pressione 'y'",True, black))
#                tela.blit(text,(30,90))
#                for event in pygame.event.get():
#                    if event.type == pygame.QUIT:
#                        pygame.quit()
#                    if event.key == pygame.K_x:
#                        score = 0
#                        i= 0

    pygame.display.update()

   #======================= Matar zombie com o tiro =======================
    if pygame.sprite.collide_rect(tiro, zumbi1):
        zumbi1 = Zumbi( 800, 350, random.randrange(-4,-10,-1))
        zumbi1_group = pygame.sprite.Group()
        zumbi1_group.add(zumbi1)
        pontos+= 1
        tiro= Tiro('Bullet.png',900, 10)
        tiro_group= pygame.sprite.Group()
        tiro_group.add(tiro)

    if pygame.sprite.collide_rect(tiro, zumbi2):
        zumbi2 = Zumbi( 800, 350, random.randrange(-4,-15,-1))
        zumbi2_group = pygame.sprite.Group()
        zumbi2_group.add(zumbi2)
        pontos+= 1
        tiro= Tiro('Bullet.png',900, 10)
        tiro_group= pygame.sprite.Group()
        tiro_group.add(tiro)

    if pygame.sprite.collide_rect(tiro, zumbi3):
        zumbi3 = Zumbi( 800, 350, random.randrange(-4,-15,-1))
        zumbi3_group = pygame.sprite.Group()
        zumbi3_group.add(zumbi3)
        pontos+= 1
        tiro= Tiro('Bullet.png',900, 10)
        tiro_group= pygame.sprite.Group()
        tiro_group.add(tiro)

    if pygame.sprite.collide_rect(tiro, zumbi4):
        zumbi4 = Zumbi( 800, 350, random.randrange(-4,-15,-1))
        zumbi4_group = pygame.sprite.Group()
        zumbi4_group.add(zumbi4)
        pontos+= 1
        tiro= Tiro('Bullet.png',900, 20)
        tiro_group= pygame.sprite.Group()
        tiro_group.add(tiro)

    if pygame.sprite.collide_rect(tiro, zumbi5):
        zumbi5 = Zumbi( 800, 350, random.randrange(-4,-15,-1))
        zumbi5_group = pygame.sprite.Group()
        zumbi5_group.add(zumbi5)
        pontos+= 1
        tiro= Tiro('Bullet.png',900, 20)
        tiro_group= pygame.sprite.Group()
        tiro_group.add(tiro)

    background.move()
    background1.move()












#================================ Gera as Saídas ===================================

    background_group.draw(tela)
#    tela.blit(fundo, (0, 0))
    zumbi1_group.draw(tela)
    zumbi2_group.draw(tela)
    zumbi3_group.draw(tela)
    zumbi4_group.draw(tela)
    zumbi5_group.draw(tela)
    zumbizao_group.draw(tela)
#    obstacle_group.draw(tela)
    tiro_group.draw(tela)
#    power.update()
    player.update()
    char_group.draw(tela)
    Pontuacao(pontos)
    coracao1_group.draw(tela)
    coracao2_group.draw(tela)
    coracao3_group.draw(tela)
    pygame.display.update()

pygame.display.quit()
