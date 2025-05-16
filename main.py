import pygame
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from score import Score
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = asteroids, updateable, drawable
    AsteroidField.containers = (updateable,)
    Player.containers = updateable, drawable
    Shot.containers = shots, updateable, drawable
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    score = Score()
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    score.add_to_score()
                    shot.kill()
                    asteroid.split()
            if asteroid.collide(player):
                print("Game over!")
                print(f"Highscore: {score.get_score()}")
                sys.exit()
        screen.fill("black")
        for member in drawable:
            member.draw(screen)
        score.display_score(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
