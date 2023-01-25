import pygame

class Gun():

    def __init__(self, screen):
        """Инициализация пушки"""

        # получение экрана
        self.screen = screen
        # загрузка изображения
        self.image = pygame.image.load('images/pixil-frame-0.png')
        # получение поверностей экрана и изображения
        self.rect = self.image.get_rect()
        # получение объекта экрана
        self.screen_rect = screen.get_rect()
        # координаты центра пушки
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        # координаты низа пушки
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """Рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.mleft and self.rect.left > 0:
            self.center -= 1
        self.rect.centerx = self.center