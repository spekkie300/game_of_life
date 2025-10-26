import pygame
import random

from constants import CELL_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH


class Grid:
    def __init__(self, cell_size):
        self.rows = SCREEN_WIDTH // cell_size
        self.columns = SCREEN_HEIGHT // cell_size
        self.__cell_size = cell_size
        self.cells = [[Cell() for _ in range(self.columns)] for _ in range(self.rows)]
        self.sim_running = False
        self.generation = 0

    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                x = row * self.__cell_size
                y = column * self.__cell_size
                rect = pygame.Rect(x, y, self.__cell_size, self.__cell_size)

                if cell.alive:
                    pygame.draw.rect(screen, CELL_COLOR, rect)
                else:
                    pygame.draw.rect(screen, CELL_COLOR, rect, 1)

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_row, mouse_column = pygame.mouse.get_pos()
            mouse_row //= self.__cell_size
            mouse_column //= self.__cell_size

            cell_under_mouse = self.cells[mouse_row][mouse_column]
            if cell_under_mouse.alive:
                cell_under_mouse.alive = False
            elif not cell_under_mouse.alive:
                cell_under_mouse.alive = True

    def check_neighbours(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                alive_neighbours = 0

                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if i == 0 and j == 0:
                            continue
                        neighbour_row = row + i
                        neighbouw_col = column + j

                        if (
                            0 <= neighbour_row < self.rows
                            and 0 <= neighbouw_col < self.columns
                        ):
                            if self.cells[neighbour_row][neighbouw_col].alive:
                                alive_neighbours += 1

                cell.neighbours = alive_neighbours

    def simulation(self):
        self.check_neighbours()
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                if cell.alive:
                    if cell.neighbours < 2:
                        cell.alive = False
                    elif 2 <= cell.neighbours <= 3:
                        cell.alive = True
                    elif cell.neighbours > 3:
                        cell.alive = False
                else:
                    if cell.neighbours == 3:
                        cell.alive = True

    def randomize(self):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                rand_choice = random.choice([True, False])
                cell.alive = rand_choice


class Cell:
    def __init__(self):
        self.alive = False
        self.neighbours = 0
