import pygame

COLOR = (0,0,0)

def update_screen(screen, alive):
    screen.fill((230, 230, 230))
    (w_width, w_height) = pygame.display.get_window_size()
    for position in alive:
        rect = pygame.Rect(10 * position[0] + w_width/2, -10 * position[1] + w_height/2, 8, 8)
        pygame.draw.rect(screen, COLOR, rect)
    pygame.display.flip()
