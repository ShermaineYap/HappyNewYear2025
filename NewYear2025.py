import pygame
import random
import time
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy New Year 2025")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
COLORS = [RED, YELLOW, BLUE, GREEN, PURPLE, CYAN, ORANGE]

font_large = pygame.font.Font(pygame.font.get_default_font(), 60)
font_small = pygame.font.Font(pygame.font.get_default_font(), 40)
font_medium = pygame.font.Font(pygame.font.get_default_font(), 50)

clock = pygame.time.Clock()

class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.radius = random.randint(1, 3)
        self.speed = random.uniform(0.5, 1.5)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

class Firework:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT // 2)
        self.color = random.choice(COLORS)
        self.radius = random.randint(2, 5)
        self.explosion_radius = 0
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.explosion_radius += 2
            if self.explosion_radius > 50:
                self.exploded = True
        else:
            self.explosion_radius -= 2

    def draw(self):
        if self.explosion_radius > 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.explosion_radius, 2)

def countdown_to_new_year():
    target_time = datetime(2025, 1, 1, 0, 0, 0)
    current_time = datetime.now()
    time_difference = target_time - current_time

    days, seconds = time_difference.days, time_difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{days}d {hours}h {minutes}m {seconds}s"

def main():
    running = True
    fireworks = []
    stars = [Star() for _ in range(100)]
    text_x = WIDTH

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for star in stars:
            star.update()
            star.draw()

        countdown_text = font_small.render(f"Countdown to 2025: {countdown_to_new_year()}", True, WHITE)
        screen.blit(countdown_text, (20, 20))

        text = font_large.render("Happy New Year 2025!", True, random.choice(COLORS))
        text_x -= 2  # Move text to the left
        if text_x < -text.get_width():
            text_x = WIDTH
        screen.blit(text, (text_x, HEIGHT // 2))

        subtext = font_medium.render("Wishing You Joy and Prosperity!", True, random.choice(COLORS))
        screen.blit(subtext, (WIDTH // 2 - subtext.get_width() // 2, HEIGHT // 2 + 80))

        if random.randint(0, 20) == 0:  
            fireworks.append(Firework())

        for firework in fireworks[:]:
            firework.update()
            firework.draw()
            if firework.explosion_radius <= 0:
                fireworks.remove(firework)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
