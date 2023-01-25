import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        # создание пули
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 166, 166, 29
        self.speed = 1
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
