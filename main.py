import pygame
import sys
import time


import preset_builds as p
import game_functions as gf
from settings import Settings


golsettings = Settings()
alive = []
sleeptime = 0.1


def surrounding_cells(cell):
    (x, y) = cell
    yield (x - 1, y + 1)
    yield (x    , y + 1)
    yield (x + 1, y + 1)
    yield (x - 1, y)
    yield (x + 1, y)
    yield (x - 1, y - 1)
    yield (x    , y - 1)
    yield (x + 1, y - 1)


def count_alive_neighbors(cell):
    return sum(1 for neighbor in surrounding_cells(cell) if neighbor in alive)


def update():
    deadclosetoalive = []
    nextalive = []

    for cell in alive:
        for neighbor in surrounding_cells(cell):
            if neighbor in alive:
               continue
            if neighbor not in deadclosetoalive:
                deadclosetoalive.append(neighbor)

    for cell in alive:
        alive_num = count_alive_neighbors(cell)
        if alive_num == 2 or alive_num == 3:
            nextalive.append(cell)

    for cell in deadclosetoalive:
        alive_num = count_alive_neighbors(cell)
        if alive_num == 3:
            nextalive.append(cell)

    alive.clear()
    alive.extend(nextalive)


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life")

    while True:
        gf.eventcheck(golsettings)

        if golsettings.gamerunning:
            update()
            gf.update_screen(screen, alive, golsettings)
            time.sleep(sleeptime)


run_game()
