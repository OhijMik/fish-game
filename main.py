import pygame
import random

pygame.init()
font = pygame.font.SysFont("Roboto", 26)
title = pygame.font.SysFont("Roboto", 100)

# The main function
def main():
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [800, 600]   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred

    programState = "start"
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))
    mainSurface.fill((0,0,255)) # Makes screen blue

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
           break

        # Getting the position of the mouse
        mousePos = pygame.mouse.get_pos()

        # Program is at start screen
        if programState == 'start':
            
            # Words on the screen
            renderedText = title.render("Fish Game", 1, pygame.Color(255, 255, 255))
            mainSurface.blit(renderedText, (220,150))
            renderedText = pygame.font.SysFont("Roboto", 60).render("Start", 1, pygame.Color(255, 255, 255))
            mainSurface.blit(renderedText, (360,260))
            renderedText = pygame.font.SysFont("Roboto", 60).render("Quit", 1, pygame.Color(255, 255, 255))
            mainSurface.blit(renderedText, (360,350))
            
            # Button rectangle
            for i in range(250, 410, 90):
                pygame.draw.rect(mainSurface, [255, 255, 255], [310,i,200,60], 2)
                
            # If the mouse is touching the button
            if mousePos[0] >= 310 and mousePos[0] <= 510:
                if mousePos[1] >= 250 and mousePos[1] <= 310:
                    pygame.draw.rect(mainSurface, (255, 170, 0), [310,250,200,60], 2)
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        programState = 'game'
                elif mousePos[1] >= 340 and mousePos[1] <= 400:
                    pygame.draw.rect(mainSurface, (255, 170, 0), [310,340,200,60], 2)
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        break

        pygame.display.flip()
        
        frameCount += 1
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.
# Running the main loop
main()