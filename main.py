import pygame

from constants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from grid import Grid


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    grid = Grid(CELL_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            grid.handle_mouse(event)

        screen.fill("white")

        grid.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
