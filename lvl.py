import pygame
import random
from sprites import Pacman, Ghost

CELL_SIZE = 20

level_1 = [
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.#  #.#   #.##.#   #.#  #.#",
        "#.####.#####.##.#####.####.#",
        "#............G.............#",
        "############################",
    ]

level_2 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #.##.#   #.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_3 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#.###.####.#",
        "#.#....#   #....#...#.#  #.#",
        "#.#.##.#####.##.###.#.####.#",
        "#...#...#....G.............#",
        "############################",
    ]
level_4 = [
        "############################",
        "#..........................#",
        "#.#.##.#####.##.#####.####.#",
        "#.#.................#.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_5 = [
        "############################",
        "#......#####.##............#",
        "#..##..#...#.##.#####.####.#",
        "#..##..#   #.##.#   #.#  #.#",
        "#..##..#####.##.#####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_6 = [
        "############################",
        "#............##...##.......#",
        "#.#.##.#####.##.#.##..####.#",
        "#.#....#   #.##.#.# #.#  #.#",
        "#.#.##.#####.##.#.###.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_7 = [
        "############################",
        "#...........#.#............#",
        "#.#.##.######.#.#####.####.#",
        "#.#....#   #..#.#   #.#  #.#",
        "#.#.##.######.#.#####.####.#",
        "#...#.......#G#............#",
        "############################",
    ]
level_8 = [
        "############################",
        "#..........................#",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #.##.#   #.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#........G..#   ###    #",
        "############################",
    ]
level_9 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#...#.####.#",
        "#.#....#...#.##.#...#.#  #.#",
        "#.#.##.#...#.##.#####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_10 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #....#   #.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#..G#.......#.............#",
        "############################",
    ]
level_11 = [
        "############################",
        "#............##.....#......#",
        "#.........#...........#....#",
        "#............#.............#",
        "#.......#............#.....#",
        "#...#........G...#.........#",
        "############################",
    ]
level_12 = [
        "############################",
        "#..........................#",
        "#..........................#",
        "#..............G...........#",
        "#..........................#",
        "#..........................#",
        "############################",
    ]
level_13 = [
        "############################",
        "#............##............#",
        "#.#.########.##.#...#.####.#",
        "#.#....#.....##.#####.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_14 = [
        "############################",
        "#............##............#",
        "#.#.##..####.##..####..##..#",
        "#.#....#   #.##.#   #.#.##.#",
        "#.#.##.#####.##..####.#..#.#",
        "#...#........G.............#",
        "############################",
    ]
level_15 = [
        "############################",
        "#............##............#",
        "#.#.##.##.......#####.####.#",
        "#.#....##.#..#..#   #.#  #.#",
        "#.#.##.#####.##..####.####.#",
        "#...#........G.............#",
        "############################",
    ]
level_16 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #....#   #.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#..#.....G..#..........#",
        "############################",
    ]
level_17 = [
        "############################",
        "#............##............#",
        "#.##...#####.##.#####.##...#",
        "#.##...#   #..#.#   #.##...#",
        "#.##...#####.##.#####.##...#",
        "#............G.............#",
        "############################",
    ]
level_18 = [
        "############################",
        "#............##............#",
        "#.#.##................####.#",
        "#.#...................#  #.#",
        "#.#.##................####.#",
        "#...#........G.............#",
        "############################",
    ]
level_19 = [
        "############################",
        "#............##............#",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #.##.#   #.#  #.#",
        "#.#.##.#####.##.#####.####.#",
        "#...#####....G.............#",
        "############################",
    ]
level_20 = [
        "############################",
        "###.............############",
        "#.#.##.#####.##.#####.####.#",
        "#.#....#   #.##.#...#.#  #.#",
        "#.#.##.#####.##.#...#.####.#",
        "#...##.......G.............#",
        "############################",
    ]


def load_level_1():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_1

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


def load_level_2():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_2

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


def load_level_3():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_3

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


def load_level_4():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_4

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


def load_level_5():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_5

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


def load_level_6():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_6

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


def load_level_7():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_7

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


def load_level_8():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_8

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


def load_level_9():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_9

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


def load_level_10():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_10

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


def load_level_11():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_11

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


def load_level_12():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_12

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


def load_level_13():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_13

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


def load_level_14():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_14

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


def load_level_15():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_15

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


def load_level_16():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_16

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


def load_level_17():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_17

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


def load_level_18():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_18

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


def load_level_19():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_19

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


def load_level_20():
    walls, dots, ghosts, free_spaces = [], [], [], []
    level = level_20

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

