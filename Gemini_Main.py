# -*- coding: utf-8 -*-
import pygame
import sys
import random
from Gemini import Character, Obstacle


pygame.init()
pygame.display.init()

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
window = pygame.display.set_mode((1000,750))  #sets size of pygame window
pygame.display.set_caption("Gemini")   #caption on top of window

leftChar = Character()
obstacle1 = Obstacle(10,10,70,600)
contactDirection = ''

while True:
    window.fill(pygame.Color(53,72,75))
    fps = pygame.time.Clock()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        '''
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    leftChar.changeDirection('RIGHT')
                     
                elif event.key == pygame.K_LEFT:
                    leftChar.changeDirection('LEFT')
                    
                elif event.key == pygame.K_UP:
                    leftChar.changeDirection('UP')
                    
                elif event.key == pygame.K_DOWN:
                    leftChar.changeDirection('CROUCH')
                    
                print(leftChar.getDirection())   
        '''
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_UP]:
        leftChar.changeDirection('UP')
    elif keys[pygame.K_DOWN]:
        leftChar.changeDirection('CROUCH')
    elif keys[pygame.K_LEFT]:
        leftChar.changeDirection('LEFT')
    elif keys[pygame.K_RIGHT]: 
        leftChar.changeDirection('RIGHT')
            
    #---------------DRAWS CHARACTER SQUARE--------------------------            
    leftCharRect = leftChar.get_rect()
    pygame.draw.rect(window, pygame.Color(225,225,225), pygame.Rect(leftChar.getPositionX(), leftChar.getPositionY(), 10, 10))
    
    obstacle1Rect = obstacle1.get_rect()
    pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(obstacle1.getPositionX(), obstacle1.getPositionY(), obstacle1.getWidth(), obstacle1.getHeight()))
    
    if leftCharRect.colliderect(obstacle1Rect) == True:
        leftChar.setCollision(True)
        contactDirection = leftChar.getDirection()     
    else:
        leftChar.setCollision(False)
        contactDirection = ''
        
        
    if contactDirection == 'UP':
        leftChar.setPosition([leftChar.getPositionX(), leftChar.getPositionY() + .5])
    if contactDirection == 'CROUCH':
        leftChar.setPosition([leftChar.getPositionX(), leftChar.getPositionY() - .5])
    if contactDirection == 'RIGHT':
        leftChar.setPosition([leftChar.getPositionX() - .5, leftChar.getPositionY()])
    if contactDirection == 'LEFT':
        leftChar.setPosition([leftChar.getPositionX() + .5, leftChar.getPositionY()])
        
        
        
    
    
    
    
    
    
    #print(leftChar.getPosition())
    pygame.display.flip()
    