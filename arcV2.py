__author__ = 'Xvost'
import pygame,\
    color,\
    sys,\
    os,\
    pickle

class BALL:
    x = 0
    y = 0
    X_vect = 0
    Y_vect = 0
    radius = 2
    color = color.black

    def __init__(self, surface, color, pos, radius):
        #(surface, color, pos, radius)
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.surface = surface
        self.color = color
        self.radius = radius
        self.rect = pygame.draw.circle(self.surface, self.color, self.pos, self.radius)
        Balls.append(self)
    def __call__(self):
        if self.rect.left < block_l or self.rect.right + 1 > Main.size[0]:
            self.X_vect = -self.X_vect
        if self.rect.top <= 0 or self.rect.bottom + 1 > Main.size[1]:
            self.Y_vect = -self.Y_vect
        self.pos = (self.pos[0] + self.X_vect, self.pos[1] + self.Y_vect)
        self.rect = pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

class window:
    def __init__(self, size, background):
        self.size = size
        self.background = background
        self.back_rect = background.get_rect(topleft=(0, 0))
        self.disp = pygame.display.set_mode(size)
        self.background = self.background.convert()

    def __call__(self):
        self.disp.fill(color.white)
        self.disp.blit(self.background, self.back_rect)

    def UpToDate(self):
        pygame.display.flip()

class block:
    type = None
    pos = ()

    def __init__(self, pos, type=None):
        global Balls
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Ball.X_vect += 1
            if event.key == pygame.K_LEFT:
                Ball.X_vect -= 1
            if event.key == pygame.K_UP:
                Ball.Y_vect -= 1
            if event.key == pygame.K_DOWN:
                Ball.Y_vect += 1
    for ball_index,ball in enumerate(Balls):
        for block_index,block in enumerate(Blocks):
            if ball.rect.colliderect(block.rect):
                if Blocks[block_index].rect.left < Balls[ball_index].rect.centerx < Blocks[block_index].rect.right:
                    Balls[ball_index].Y_vect=-Balls[ball_index].Y_vect
                if Blocks[block_index].rect.top < Balls[ball_index].rect.centery < Blocks[block_index].rect.bottom:
                    Balls[ball_index].X_vect=-Balls[ball_index].X_vect
                del Blocks[block_index]
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
    size = Main.size
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
FPS = 40
fps = pygame.time.Clock()
colors = [color.red,
          color.magenta,
          color.blue
]
Types = {'Break': 0, 'Block': 1, 'Wood': 2, 2: 'Wood', 1: 'Block', 0: 'Break'}
NumberOfLevel = 0
Blocks = []
Balls=[]
pygame.init()
background = pygame.image.load('game_back.png')
Main = window((500, 550), background)
block_l = 70
block_w = (Main.size[0] - 40) / 10
block_h = 20
block_t = 20
LevelFiles = load_levels()
CreateLevel(NumberOfLevel)
Ball = BALL(Main.disp, color.red, (Main.size[0] / 2, Main.size[1] / 2 + 50), 4)
######################################################
while 1:
    events()
    Main()
    for now_block in Blocks:
        pygame.draw.rect(Main.disp, colors[Types[now_block.type]], now_block())
    Ball()
    Main.UpToDate()
    fps.tick(FPS)