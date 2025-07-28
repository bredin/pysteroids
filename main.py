import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #create clock
    clock = pygame.time.Clock()
    dt = 0
    #create containers
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    #create asteroids
    asteroid_field = AsteroidField()

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
