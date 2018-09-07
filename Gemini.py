# -*- coding: utf-8 -*-
import pygame


class Character():
    def __init__(self):
        self.position = [50,600]
        self.direction = 'STAND'
        self.collide = False
        self.dead = False
        self.width = 10
        self.height = 10
    
        
    def changeDirection(self, direction):
        if direction == 'RIGHT':
            self.direction = 'RIGHT'
            self.position[0] += .5
          
        elif direction == 'LEFT':
            self.direction = 'LEFT'
            self.position[0] -= .5
            
        elif direction == 'UP':
            self.direction = 'UP'
            self.position[1] -= .5
            
        elif direction == 'CROUCH':
            self.direction = 'CROUCH'
            self.position[1] += .5
            
        elif direction == 'STAND':
            self.direction = 'STAND'
            
            #position doesn't change
            
    def setCollision(self, collision):
        if collision == True:
            self.collide = True
        elif collision == False:
            self.collide = False
            
    def getCollision(self):
        return self.collide
            
    def setDead(self, dead):
        if dead == True:
            self.dead = True
        elif dead == False:
            self.dead = False
            
    def getDead(self):
        return self.dead
    
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position
    
    def getPositionX(self):
        return self.position[0]
    
    def getPositionY(self):
        return self.position[1]
    
    def getDirection(self):
        return self.direction
    
    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.width, self.height )
    
    def setDirection(self, direction):
        self.direction = direction
        
    
            
class Obstacle():
    def __init__(self, width, height, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.position = [x_position, y_position]
        self.width = width
        self.height = height
        
    def hasCollided(self, characterPosition):
        '''
        for x in range(50):
            for y in range(50):
                threshold1 = [characterPosition[0] + x, characterPosition[1] + y]
                threshold2 = [characterPosition[0] - x, characterPosition[1] - y]
                threshold3 = [characterPosition[0] + x, characterPosition[1] - y]
                threshold4 = [characterPosition[0] - x, characterPosition[1] + y]
                #print(threshold1)
                #print('thresh1')
                #print(self.position)
        '''
        if characterPosition[0] == self.x_position - 10 and characterPosition[0] == self.y_position:
            return True
        elif characterPosition[0] == self.x_position + 10 and characterPosition[0] == self.y_position:
            return True
        else:
            return False

    def getPositionX(self):
        return self.x_position
    
    def getPositionY(self):
        return self.y_position
    
    def getPosition(self):
        return self.position
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def get_rect(self):
        return pygame.Rect(self.x_position, self.y_position, self.width, self.height)
    
        
        
        