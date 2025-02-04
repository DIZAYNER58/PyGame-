import pygame
import time
from lvl import load_level_1, load_level_2, load_level_3, load_level_4, load_level_5, load_level_6, load_level_7, \
    load_level_8, load_level_9, load_level_10, load_level_11, load_level_12, load_level_13, \
    load_level_14, load_level_15, load_level_16, load_level_17, load_level_18, load_level_19, load_level_20, level_1, \
    level_2, level_16, level_17, level_18, level_19, level_20, level_3, level_4, level_5, level_6, level_7, level_8, \
    level_9, level_10, level_11, level_12, level_13, level_14, level_15


# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 560, 620
CELL_SIZE = 20
a = input('Введите номер уровня:')
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
if a == '1':
    walls, dots, ghosts, pacman = load_level_1()
if a == '2':
    walls, dots, ghosts, pacman = load_level_2()
if a == '3':
    walls, dots, ghosts, pacman = load_level_3()
if a == '4':
    walls, dots, ghosts, pacman = load_level_4()
if a == '5':
    walls, dots, ghosts, pacman = load_level_5()
if a == '6':
    walls, dots, ghosts, pacman = load_level_6()
if a == '7':
    walls, dots, ghosts, pacman = load_level_7()
if a == '8':
    walls, dots, ghosts, pacman = load_level_8()
if a == '9':
    walls, dots, ghosts, pacman = load_level_9()
if a == '10':
    walls, dots, ghosts, pacman = load_level_10()
if a == '11':
    walls, dots, ghosts, pacman = load_level_11()
if a == '12':
    walls, dots, ghosts, pacman = load_level_12()
if a == '13':
    walls, dots, ghosts, pacman = load_level_13()
if a == '14':
    walls, dots, ghosts, pacman = load_level_14()
if a == '15':
    walls, dots, ghosts, pacman = load_level_15()
if a == '16':
    walls, dots, ghosts, pacman = load_level_16()
if a == '17':
    walls, dots, ghosts, pacman = load_level_17()
if a == '18':
    walls, dots, ghosts, pacman = load_level_18()
if a == '19':
    walls, dots, ghosts, pacman = load_level_19()
if a == '20':
    walls, dots, ghosts, pacman = load_level_20()


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
