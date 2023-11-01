import pygame
import random

pygame.init()

# The main function
def main():
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = [800, 600]   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize[0], surfaceSize[1]))
    mainSurface.fill((0,0,255)) # Makes screen blue

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
           break

        


        pygame.display.flip()
    
        frameCount += 1
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.
# Running the main loop
main()