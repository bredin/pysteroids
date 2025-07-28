import pygame

import random

from constants import *

from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt
                # Remove the asteroidt if it goes off-screen
        if (self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position,self.radius,2)

    def split(self):
        # Split the asteroid into two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = self.velocity.rotate(angle) * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2.velocity = self.velocity.rotate(-angle) * 1.2
        self.kill()
        return
