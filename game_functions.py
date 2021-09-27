import pygame
import sys


COLOR = (0, 0, 0)
COLOR1 = (255, 255, 255)
screencenter = [0, 0]


# Function to help so that things are placed correctly when zooming in and out.
def roundthingy(axis, golsettings):
    return round((round((axis/2)/10) * 10)/(10 * golsettings.zoom)) * 10 * golsettings.zoom


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
    if event.key == golsettings.zoomin:
        if golsettings.zoom >= 1:
            golsettings.zoom += 1
        else:
            golsettings.zoom += 0.1
    if event.key == golsettings.zoomout:
        if golsettings.zoom > 1:
            golsettings.zoom -= 1
        elif golsettings.zoom > 0.3:
            golsettings.zoom -= 0.1


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
    if golsettings.dynamicmovement == False:
        if golsettings.movingleft and not golsettings.movingright:
            screencenter[0] += golsettings.moverate
        elif golsettings.movingright and not golsettings.movingleft:
            screencenter[0] -= golsettings.moverate
        if golsettings.movingdown and not golsettings.movingup:
            screencenter[1] -= golsettings.moverate
        elif golsettings.movingup and not golsettings.movingdown:
            screencenter[1] += golsettings.moverate
    else:
        if golsettings.movingleft and not golsettings.movingright:
            screencenter[0] += golsettings.moverate * 1/golsettings.zoom
        elif golsettings.movingright and not golsettings.movingleft:
            screencenter[0] -= golsettings.moverate * 1/golsettings.zoom
        if golsettings.movingdown and not golsettings.movingup:
            screencenter[1] -= golsettings.moverate * 1/golsettings.zoom
        elif golsettings.movingup and not golsettings.movingdown:
            screencenter[1] += golsettings.moverate * 1/golsettings.zoom

    screen.fill((230, 230, 230))
    (w_width, w_height) = pygame.display.get_window_size()

    if golsettings.gridshown == True and golsettings.zoom >= 1:
        x = 0
        while x < (golsettings.zoom/10 * w_width):
            x += 1
            rect = pygame.Rect((x - 1) * golsettings.zoom * 10 - golsettings.zoom, 0, golsettings.zoom, w_height)
            pygame.draw.rect(screen, COLOR1, rect)
        x = 0
        while x < (golsettings.zoom/10 * w_height):
            x += 1
            rect = pygame.Rect(0, (x - 1) * golsettings.zoom * 10 - golsettings.zoom, w_width, golsettings.zoom)
            pygame.draw.rect(screen, COLOR1, rect)

    for position in alive:
        rect = pygame.Rect(
            (10 * position[0] + screencenter[0]) * golsettings.zoom  + roundthingy(w_width, golsettings),
            (-10 * position[1] + screencenter[1]) * golsettings.zoom + roundthingy(w_height, golsettings),
            golsettings.zoom * 9, golsettings.zoom * 9)
        pygame.draw.rect(screen, COLOR, rect)
    pygame.display.flip()
