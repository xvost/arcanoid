__author__ = 'Xvost'
import   pygame, color

class BALL:
    self.x = 0
    self.y = 0
    self.X_vect = 0
    self.Y_vect = 0
    self.radius = 5
    self.color = color.black

    def __init__(self, Surface, color, pos, radius):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.draw.circle(Surface, color, pos, radius)
