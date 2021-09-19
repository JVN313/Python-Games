import pygame

# Intialize the pygame
pygame.init()

# creation of the screen/window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# The Game Code
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False