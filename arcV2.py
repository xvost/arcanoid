__author__ = 'Xvost'
import pygame, color, sys

class BALL:
    x = 0
    y = 0
    X_vect = 0
    Y_vect = 0
    radius = 5
    color = color.black

    def __init__(self, Surface, color, pos, radius):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.draw.circle(Surface, color, pos, radius)


class window:
    def __init__(self, size, background):
        self.size = size
        self.background = background
        self.back_rect = background.get_rect(topleft=(0, 0))
        self.disp = pygame.display.set_mode(size)
        self.background = self.background.convert()

    def get_size(self):
        return self.size

    def __call__(self):
        self.disp.fill(color.white)
        self.disp.blit(self.background, self.back_rect)
        pygame.display.flip()


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit(0)

pygame.init()
background = pygame.image.load('game_back.png')
Main = window((500, 550), background)
print type(Main.disp)
while 1:
    events()
    Main()