import pygame
import random

CELL_SIZE = 20
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

directions = [UP, DOWN, LEFT, RIGHT]


class Pacman:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        self.direction = RIGHT
        self.next_dir = RIGHT

    def move(self, walls):
        new_pos = self.rect.move(self.next_dir[0] * CELL_SIZE, self.next_dir[1] * CELL_SIZE)
        if not any(new_pos.colliderect(wall) for wall in walls):
            self.direction = self.next_dir
        new_pos = self.rect.move(self.direction[0] * CELL_SIZE, self.direction[1] * CELL_SIZE)
        if not any(new_pos.colliderect(wall) for wall in walls):
            self.rect.update(new_pos)

    def check_collision(self, ghosts):
        return any(self.rect.colliderect(ghost.rect) for ghost in ghosts)


class Ghost:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

    def move(self, walls):
        random_dir = random.choice(directions)
        new_pos = self.rect.move(random_dir[0] * CELL_SIZE, random_dir[1] * CELL_SIZE)
        if not any(new_pos.colliderect(wall) for wall in walls):
            self.rect.update(new_pos)
