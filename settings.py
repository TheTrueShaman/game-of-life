import pygame


class Settings:

    def __init__(self):
        # Keybinds
        self.shiftleft = pygame.K_LEFT
        self.shiftright = pygame.K_RIGHT
        self.shiftup = pygame.K_UP
        self.shiftdown = pygame.K_DOWN
        self.zoomin = pygame.K_z
        self.zoomout = pygame.K_x

        # Other settings
        # Sets the game to running. If gamerunning = false, the game is paused
        self.gamerunning = True

        self.movingleft = False
        self.movingright = False
        self.movingup = False
        self.movingdown = False
        self.moverate = 10
        self.zoom = 1
