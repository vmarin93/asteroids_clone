import pygame
import random


from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            position = self.position
            first_split = Asteroid(position.x, position.y, new_radius)
            first_split.velocity = self.velocity.rotate(angle)
            second_split = Asteroid(position.x, position.y, new_radius)
            second_split.velocity = self.velocity.rotate(-angle)
