__author__ = 'Xvost'
import pygame,\
    color, sys, os, pickle

class BALL:
    x = 0
    y = 0
    X_vect = 0
    Y_vect = 0
    radius = 5
    color = color.black

    def __init__(self, surface, color, pos, radius):
        self.x = pos[0]
        self.y = pos[1]
        self.rect = pygame.draw.circle(surface, color, pos, radius)


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

    def UpToDate(self):
        pygame.display.flip()


class block:
    type = None
    pos = ()

    def __init__(self, pos, type=None):
        self.pos = pos
        self.type = type
        self.rect = pygame.Rect(pos[0] - block_w / 2, pos[1] - block_h / 2, block_w, block_h)

    def __call__(self):
        return self.rect


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit(0)


def load_levels():
    path = os.getcwd()
    path = path + '/levels/'
    path = os.path.abspath(path)
    list_files = []
    for i in os.listdir(path):
        if i.split('.')[-1] == 'arc':
            list_files.append((path + '/' + i))
    return list_files


def CreateLevel(LevelNum):
    global block_t, block_l, num, block_w, color_list
    size = Main.get_size()
    try:
        LevelFiles[LevelNum]
    except:
        LevelNum = 0
        num = 0
    levels = open(LevelFiles[LevelNum], 'rb')
    blocks = pickle.load(levels)
    levels.close()
    block_tmp = block_t
    number_w = len(blocks[0])
    block_w = (size[0] - 40 - (number_w / 2)) / number_w
    for i, j in enumerate(blocks):
        block_tmp = block_tmp + 1
        for e, r in enumerate(j):
            if r != 0:
                tmp = block((block_l + (block_w * e) + e * 1, block_tmp + (i * block_h)))
                Blocks.append(tmp)
                Blocks[-1].type = Types[r - 1]

####################################################
colors = [color.red,
          color.magenta,
          color.blue
]
Types = {'Break': 0, 'Block': 1, 'Wood': 2, 2: 'Wood', 1: 'Block', 0: 'Break'}
NumberOfLevel = 0
Blocks = []
pygame.init()
background = pygame.image.load('game_back.png')
Main = window((500, 550), background)
block_l = 20
block_w = (Main.get_size()[0] - 40) / 10
block_h = 20
block_t = 20
LevelFiles = load_levels()
CreateLevel(NumberOfLevel)
######################################################
while 1:
    events()
    Main()
    for now_block in Blocks:
        pygame.draw.rect(Main.disp, colors[Types[now_block.type]], now_block())
    Main.UpToDate()