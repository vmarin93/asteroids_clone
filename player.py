import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Original Boot.dev code
            #right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            #a = self.position + forward * self.radius
            # b = self.position - forward * self.radius - right
            # c = self.position - forward * self.radius + right
        # The code I wrote to satisfy lsp complaints about doing mathematical operations between a vector(composed of 2 floats) and a single float value
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        a = self.position + pygame.Vector2(forward.x * self.radius, forward.y * self.radius)
        b = self.position - pygame.Vector2(forward.x * self.radius, forward.y * self.radius) - pygame.Vector2(right.x * (self.radius / 1.5), right.y * (self.radius / 1.5))
        c = self.position - pygame.Vector2(forward.x * self.radius, forward.y * self.radius) + pygame.Vector2(right.x * (self.radius / 1.5), right.y * (self.radius / 1.5))
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
