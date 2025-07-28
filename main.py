import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.flip()  # Update the display

        dt = clock.tick(60)/1000  # Limit to 60 FPS


if __name__ == "__main__":
    main()
