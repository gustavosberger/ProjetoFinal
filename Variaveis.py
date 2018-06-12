# -*- coding: utf-8 -*-
"""
Created on Fri May  4 06:38:48 2018

@author: Gustavo Berger
"""
import pygame
import sys
from pygame.locals import *
import os
import classeZumbi.py as Zumbi
import classePersonagem.py as Personagem



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
Altura_maxima= 10
salto= 0
falling= 0


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