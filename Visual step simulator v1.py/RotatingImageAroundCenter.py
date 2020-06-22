"""
PyGame Library for Displaying Image and changing it's coordinates
"""

""" Import Lib"""
import pygame
import time

"""Variable for Brightness of Image"""
bright=100

""" Initialize Pygame"""
pygame.init()


""" Set the Dimension of the Screen"""
Width = 1000
Height = 800

""" Set the Screen"""
screen = pygame.display.set_mode((Width,Height))


""" Set The Title of Screen"""
pygame.display.set_caption("Display Image")

""" Load the Background Image"""
backImg = pygame.image.load("Images/Step Markings.png")

screen.blit(backImg,(0,0))

pygame.display.update()
time.sleep(0.1)

""" Load the Image"""
screenImg = pygame.image.load("Images/Stepper Motor Symbol.png")


""" Display Image at Specific Co-Ordinate"""

screen.blit(screenImg,(140,140))

""" Update the Display Continuously"""

EventStatus = "None"
angle = 0
BLACK =(0,0,0)

def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
    
while True:
    oldRect = screenImg.get_rect(center=(140,140))
    newImg,rot_rect = rot_center(screenImg,oldRect,angle)
    
    
    # screen.fill(BLACK)
    screen.blit(newImg,rot_rect.center)    
    pygame.display.flip()
    angle = angle+90
    
    angle%=360
    pygame.display.update()
    
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
        
        
    if EventStatus == "Quit":
        break
    
print("Closing")
    
    
        
    
     
            
        

    
