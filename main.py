import pygame

from constants import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from grid import Grid


# TODO: Add option to change Total grid size
# TODO: Rate limit simulation
# TODO: Make spacebar play and arrow to the right run once


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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    grid.simulation()
                    grid.generation += 1
                elif event.key == pygame.K_r:
                    grid.randomize()
                    grid.generation = 0
                elif event.key == pygame.K_SPACE:
                    grid.sim_running = not grid.sim_running

        if grid.sim_running:
            grid.simulation()
            grid.generation += 1

        screen.fill("white")

        grid.draw(screen)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
