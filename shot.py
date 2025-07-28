import pygame

from constants import *

from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.rotation = 0
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        # Remove the shot if it goes off-screen
        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()