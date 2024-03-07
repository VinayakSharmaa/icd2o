import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Pac-Man class
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.direction = None
        self.speed = 3

    def update(self):
        if self.direction:
            self.rect.x += self.direction[0] * self.speed
            self.rect.y += self.direction[1] * self.speed

            if self.rect.left < 0:
                self.rect.right = WIDTH
            elif self.rect.right > WIDTH:
                self.rect.left = 0
            elif self.rect.top < 0:
                self.rect.bottom = HEIGHT
            elif self.rect.bottom > HEIGHT:
                self.rect.top = 0

# Ghost class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, COLS - 1) * GRID_SIZE
        self.rect.y = random.randint(0, ROWS - 1) * GRID_SIZE
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.speed = 2

    def update(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.rect.x -= self.direction[0] * self.speed
            self.rect.y -= self.direction[1] * self.speed
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

# Pellet class
class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    pellets = pygame.sprite.Group()
    ghosts = pygame.sprite.Group()

    pacman = Pacman()
    all_sprites.add(pacman)

    for _ in range(4):
        ghost = Ghost(RED)
        ghosts.add(ghost)
        all_sprites.add(ghost)

    # Create pellets
    for i in range(0, WIDTH, GRID_SIZE):
        for j in range(0, HEIGHT, GRID_SIZE):
            if (i > 2 * GRID_SIZE or j > 2 * GRID_SIZE) and (i < WIDTH - 2 * GRID_SIZE or j < HEIGHT - 2 * GRID_SIZE):
                pellets.add(Pellet(i, j))
                all_sprites.add(Pellet(i, j))

    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    pacman.direction = RIGHT
                elif event.key == pygame.K_UP:
                    pacman.direction = UP
                elif event.key == pygame.K_DOWN:
                    pacman.direction = DOWN

        # Check for collision with pellets
        pellets_hit = pygame.sprite.spritecollide(pacman, pellets, True)
        score += len(pellets_hit)

        # Check for collision with ghosts
        if pygame.sprite.spritecollideany(pacman, ghosts):
            running = False

        screen.fill(BLACK)
        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    print("Game Over")
    print("Score:", score)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()