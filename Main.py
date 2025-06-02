import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the height and width
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Screen title
pygame.display.set_caption("Sprite Movement")

# Background color
bg_color = pygame.Color('black')

# Create the sprite class
class Sprite:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 100]
        self.velocity = [1, 1]  # Use integers

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create sprite instance
picture = Sprite("Sprite.png")

# Clock to control frame rate
clock = pygame.time.Clock()
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    picture.move()

    screen.fill(bg_color)
    picture.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate

pygame.quit()
