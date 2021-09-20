import pygame
import sys


COLOR = (0, 0, 0)
screencenter = [0, 0]


def eventcheck(golsettings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keydowneventcheck(event, golsettings)
        if event.type == pygame.KEYUP:
            keyupeventcheck(event, golsettings)


def keydowneventcheck(event, golsettings):
    if event.key == golsettings.shiftleft:
        golsettings.movingleft = True
    if event.key == golsettings.shiftright:
        golsettings.movingright = True
    if event.key == golsettings.shiftup:
        golsettings.movingup = True
    if event.key == golsettings.shiftdown:
        golsettings.movingdown = True


def keyupeventcheck(event, golsettings):
    if event.key == golsettings.shiftleft:
        golsettings.movingleft = False
    if event.key == golsettings.shiftright:
        golsettings.movingright = False
    if event.key == golsettings.shiftup:
        golsettings.movingup = False
    if event.key == golsettings.shiftdown:
        golsettings.movingdown = False


def update_screen(screen, alive, golsettings):
    if golsettings.movingleft and not golsettings.movingright:
        screencenter[0] += golsettings.moverate
    elif golsettings.movingright and not golsettings.movingleft:
        screencenter[0] -= golsettings.moverate
    if golsettings.movingdown and not golsettings.movingup:
        screencenter[1] -= golsettings.moverate
    elif golsettings.movingup and not golsettings.movingdown:
        screencenter[1] += golsettings.moverate

    screen.fill((230, 230, 230))
    (w_width, w_height) = pygame.display.get_window_size()
    for position in alive:
        rect = pygame.Rect(10 * position[0] + w_width/2 + screencenter[0],
                           -10 * position[1] + w_height/2 + screencenter[1], 8, 8)
        pygame.draw.rect(screen, COLOR, rect)
    pygame.display.flip()
