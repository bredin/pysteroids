import pygame

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #create clock
    clock = pygame.time.Clock()
    dt = 0
    # create player
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))  # Clear the screen with black
        for sprite in updateable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()  # Update the display

        dt = clock.tick(60)/1000  # Limit to 60 FPS


if __name__ == "__main__":
    main()
