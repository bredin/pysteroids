import pygame

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

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.position,self.radius,2)