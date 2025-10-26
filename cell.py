import pygame


class Cell:
    def __init__(self, row, column):
        self.alive = False
        self.row = row
        self.column = column
        self.position = (row, column)

    def set_alive(self, alive):
        if alive:
            self.alive = True
