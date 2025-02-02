import pygame
import random
import time
from lvl import load_level, levels
from sprites import Pacman, Ghost

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 560, 620
CELL_SIZE = 20

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Загрузка уровня
current_level = 0
walls, dots, ghosts, pacman = load_level(current_level)


# Главный игровой цикл
def show_start_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, WHITE)
    screen.blit(text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def show_game_over():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press any key to exit", True, WHITE)
    screen.blit(text, (WIDTH // 6, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    exit()


show_start_screen()
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman.next_dir = UP
            elif event.key == pygame.K_DOWN:
                pacman.next_dir = DOWN
            elif event.key == pygame.K_LEFT:
                pacman.next_dir = LEFT
            elif event.key == pygame.K_RIGHT:
                pacman.next_dir = RIGHT

    pacman.move(walls)
    for ghost in ghosts:
        ghost.move(walls)

    if pacman.check_collision(ghosts):
        show_game_over()

    for dot in dots[:]:
        if pacman.rect.colliderect(dot):
            dots.remove(dot)

    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 255), wall)
    for dot in dots:
        pygame.draw.rect(screen, WHITE, dot)
    for ghost in ghosts:
        pygame.draw.rect(screen, (255, 0, 0), ghost.rect)
    pygame.draw.circle(screen, (255, 255, 0), (pacman.rect.centerx, pacman.rect.centery), CELL_SIZE // 2)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
