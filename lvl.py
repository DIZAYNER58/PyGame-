import pygame
import random
from sprites import Pacman, Ghost

CELL_SIZE = 20

levels = [
    [
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.#  #.#   #.##.#   #.#  #.#",
        "#.####.#####.##.#####.####.#",
        "#............G.............#",
        "############################",
    ]
]


def load_level(level_index):
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = levels[level_index]

    for row_idx, row in enumerate(level):
        for col_idx, col in enumerate(row):
            x, y = col_idx * CELL_SIZE, row_idx * CELL_SIZE
            if col == "#":
                walls.append(pygame.Rect(x, y, CELL_SIZE, CELL_SIZE))
            elif col == ".":
                dots.append(pygame.Rect(x + CELL_SIZE // 4, y + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))
                free_spaces.append((x, y))
            elif col == "G":
                ghosts.append(Ghost(x, y))

    pacman_spawn = random.choice(free_spaces) if free_spaces else (CELL_SIZE, CELL_SIZE)
    pacman = Pacman(pacman_spawn[0], pacman_spawn[1])

    return walls, dots, ghosts, pacman