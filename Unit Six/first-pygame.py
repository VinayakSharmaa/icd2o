import sys
import pygame
pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([1280, 720])

pygame.display.set_caption("SUPER POTATO BRUH")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255,0,0), pygame.Rect(100,100,50,50))

    # Redraw screen
    pygame.display.flip()

pygame.quit()