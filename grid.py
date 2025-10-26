import pygame

from constants import CELL_COLOR, CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH
from cell import Cell


class Grid:
    def __init__(self, cell_size):
        self.rows = SCREEN_WIDTH // cell_size
        self.columns = SCREEN_HEIGHT // cell_size
        self.__cell_size = cell_size
        self.cells = [
            [Cell(row, column) for column in range(self.columns)]
            for row in range(self.rows)
        ]
        self.sim_running = False
        self.generation = 0

    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.cells[row][column]
                x = cell.row * self.__cell_size
                y = cell.column * self.__cell_size
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
                print("Turning alive cell dead")
            elif not cell_under_mouse.alive:
                cell_under_mouse.alive = True
                print("Turning dead cell alive!")
