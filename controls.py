import pygame, sys


def events(gun):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            # влево
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            # влево
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, gun):
    """обновление экрана"""
    screen.fill(bg_color)
    gun.output()
    pygame.display.flip()