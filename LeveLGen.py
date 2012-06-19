__author__ = 'Xvost'
import os, sys, pygame, color, pickle

size = (500, 300)
sq_h = 20
number_w = 20
number_h = 12
sq_w = (size[0] - 40 - (number_w / 2)) / number_w
line_list = []
square_list = []
list_color = [
    color.green,
    color.red,
    color.magenta
]
push_flag = False
get = False
block_color = 0

def create_level(list, blocks):
    files = 0
    path = os.getcwd()
    #    path = path + '/levels/'
    path = os.path.abspath(path)
    list_files = []
    for i in os.listdir(path):
        if i.split('.')[-1] == 'arc':
            files += 1
    level = []
    NUM = 0
    for x, i in enumerate(line_list):
        level.append([])
        for y, e in enumerate(i):
            level[x].append(square_list[NUM][0])
            NUM += 1
    file = open('level%s.arc' % files, 'wb')
    pickle.dump(level, file)
    file.close()


def quit_app():
    create_level(line_list, square_list)
    pygame.display.quit()
    sys.exit(0)

for n, i in enumerate(range(0, number_h, 1)):
    line_list.append([])
    for j in range(0, number_w, 1):
        line_list[n].append(0)
i, j = 0, 0

def select(pos, block):
    if block.left < pos[0] < block.right and block.top < pos[1] < block.bottom:
        return True

#def chouse(button,pos,mouse_action):
#    if button == 1:
#        one=1
#    else:
#        one=0
#    for i,block in enumerate(square_list):
#        if select(pos,block[1]):
#            if 0 <= block[0] < len(list_color)-1:
#                square_list[i]=(block[0]+one,block[1])
#            else:
#                square_list[i]=(0,block[1])
def give_color(pos):
    for i, block in enumerate(square_list):
        if select(pos, block[1]):
            square_list[i] = (block_color, block[1])


def set_color(Bcolor, button):
    global block_color
    if button == 1:
        Bcolor += 1
        print Bcolor
    else:
        Bcolor -= 1
    if 0 <= Bcolor <= len(list_color) - 1:
        return Bcolor
    else:
        return 0


def choice(button, pos):
    global block_color, get
    for block in square_list:
        if select(pos, block[1]):
            print block[0]
            block_color = set_color(block[0], button)
    get = True


def event():
    global push_flag, get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_app()
        if event.type == pygame.MOUSEBUTTONDOWN:
            push_flag = True
            if get == False:
                choice(event.button, event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            push_flag = False
            if get == True:
                get = False


def draw(list):
    qt = 20
    ql = 25
    qt1 = qt
    for i, j in enumerate(list):
        qt1 = qt1 + 2
        for e, r in enumerate(j):
            if r == 0:
                square_list.append((0, pygame.Rect(ql + (sq_w * e) + e * 1, qt1 + (i * sq_h), sq_w, sq_h)))

pygame.init()
screen = pygame.display.set_mode(size)
draw(line_list)
while 1:
    event()
    screen.fill(color.white)
    if push_flag == True:
        give_color(pygame.mouse.get_pos())
    for i in square_list: #draw blocks
        pygame.draw.rect(screen, list_color[i[0]], i[1])
    pygame.display.flip()