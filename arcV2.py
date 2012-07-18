__author__ = 'Xvost'
import   pygame

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
        self.display = pygame.display.set_mode(size)
        self.background = self.background.convert()
        self.back_rect = self.background.get_rect(topleft=(0, 0))

    def get_size(self):
        return self.size

    def __call__(self, *args, **kwargs):
        self.display.blit(self.back_rect, self.display)
        self.display.flip()

background = pygame.image.load('disp.jpg')
Main = window((300, 500), background)
while 1:
    Main()