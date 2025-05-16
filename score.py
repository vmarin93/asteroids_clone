import pygame


class Score():
    def __init__(self) -> None:
        self.score = 0

    def add_to_score(self) -> None:
        self.score += 1

    def display_score(self, screen):
        if pygame.font:
            font = pygame.font.SysFont("VictorMonoNerdFont", 36)
            score_text = font.render(f"Current Score: {self.score}", True, "blue")
            score_position = score_text.get_rect(x=10, y=10)
            screen.blit(score_text, score_position)

    def get_score(self):
        return self.score
