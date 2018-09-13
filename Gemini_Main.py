# -*- coding: utf-8 -*-
import pygame
import sys
import random
from Gemini import Character, Obstacle
import time


pygame.init()
pygame.display.init()

fps = pygame.time.Clock()

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
window = pygame.display.set_mode((1000,750))  #sets size of pygame window
pygame.display.set_caption("Gemini")   #caption on top of window

leftChar = Character()
obstacle1 = Obstacle(400,10,40,700)
obstacle2 = Obstacle(200, 10, 500, 500)


contactDirection = ''

jumpTime = 0

while True:
    
    
    
    window.fill(pygame.Color(53,72,75))
    fps = pygame.time.Clock()

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
            
        
        
        elif event.type == pygame.KEYDOWN:
            '''
                if event.key == pygame.K_RIGHT:
                    leftChar.changeDirection('RIGHT')
                     
                elif event.key == pygame.K_LEFT:
                    leftChar.changeDirection('LEFT')
                    '''
            if event.key == pygame.K_UP:
                leftChar.changeDirection('UP')
                leftChar.setDirection('DOWN')
                
                '''
                elif event.key == pygame.K_DOWN:
                    leftChar.changeDirection('CROUCH')
                '''
                    
        
    
    
    
    keys = pygame.key.get_pressed()
    
   
    #if keys[pygame.K_UP]:
        #leftChar.changeDirection('UP')    
    if keys[pygame.K_DOWN]:
        leftChar.changeDirection('STAND')
    elif keys[pygame.K_LEFT]:
        leftChar.changeDirection('LEFT')
        print('went')
    elif keys[pygame.K_RIGHT]: 
        leftChar.changeDirection('RIGHT')
    
        
        
    
            
    #---------------DRAWS CHARACTER SQUARE--------------------------            
    leftCharRect = leftChar.get_rect()
    pygame.draw.rect(window, pygame.Color(225,225,225), pygame.Rect(leftChar.getPositionX(), leftChar.getPositionY(), 10, 10))
    
    obstacle1Rect = obstacle1.get_rect()
    #pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(obstacle1.getPositionX(), obstacle1.getPositionY(), obstacle1.getWidth(), obstacle1.getHeight()))
    obstacle1.draw(window)
    
    obstacle2Rect = obstacle2.get_rect()
    obstacle2.draw(window)
    
    obstacleList = [obstacle1Rect, obstacle2Rect]
    
    
    if leftCharRect.colliderect(obstacle1Rect) == True or leftCharRect.colliderect(obstacle2Rect):
        leftChar.setCollision(True)
          
    else:
        leftChar.setCollision(False)
        leftChar.position[1] += .15 + 
        contactDirection = ''
        contactDirection = leftChar.getDirection()   
        
        
        
    '''
    if contactDirection == 'UP':
        leftChar.setPosition([leftChar.getPositionX(), leftChar.getPositionY() + .5])
    if contactDirection == 'CROUCH':
        leftChar.setPosition([leftChar.getPositionX(), leftChar.getPositionY() - .5])
    if contactDirection == 'RIGHT':
        leftChar.setPosition([leftChar.getPositionX() - .5, leftChar.getPositionY()])
    if contactDirection == 'LEFT':
        leftChar.setPosition([leftChar.getPositionX() + .5, leftChar.getPositionY()])
        '''
        
        
    
    
    
    
    
    
    #print(leftChar.getPosition())
    pygame.display.flip()
    