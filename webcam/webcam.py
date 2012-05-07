
'''
Created on Apr 12, 2012

@author: Bogdan
'''

if __name__ == '__main__':
    pass
import pygame, sys
import pygame.camera
from pygame import *
import pygame.surface
import pygame.draw
import pygame.display
import pygame.event
import pygame.image
import subprocess

pygame.init()
pygame.camera.init()
 
pygame.display.set_caption('LogMeIn!')
screen= pygame.display.set_mode((660,480),0)

surface = pygame.surface.Surface((660,480),0,screen)

button1 = Rect (640,20,660,50)
cam = pygame.camera.Camera(0,(640,480))
cam.start()
#def handleMouseDown():
i=0
while 1:
    i=i+1
    im = cam.get_image(surface)
    if i in range (300,320):
        surf2=pygame.image.load("F:\\3.bmp")
        surface.blit(surf2,(220,50))
    if i in range (330,350):
        surf2=pygame.image.load("F:\\2.bmp")
        surface.blit(surf2,(220,50))
    if i in range (360,380):
        surf2=pygame.image.load("F:\\1.bmp")
        surface.blit(surf2,(220,50))
    if i==400:
        pygame.image.save(im, "F:\\a.bmp")
        #subprocess.call("F:\\random.bat")
        #print(123)
        sys.exit()    
    screen.blit(im,(0,0))
    #top
    pygame.draw.line(screen, (255, 0, 0), (220, 50), (460, 50))
    #left
    pygame.draw.line(screen, (255, 0, 0), (220, 50), (220, 340))
    #bottom
    pygame.draw.line(screen, (255, 0, 0), (220, 340), (460, 340))
    #right
    pygame.draw.line(screen, (255, 0, 0), (460, 340), (460, 50))
    

    pygame.display.update()
    
    for event in pygame.event.get():
        # Shutdown with X button
        if event.type==pygame.QUIT:
            sys.exit()
        # Shutdown with ESC 
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        #primitive button check
#        elif event.type == MOUSEBUTTONDOWN:
#            a=handleMouseDown(pygame.mouse.get_pos())
        