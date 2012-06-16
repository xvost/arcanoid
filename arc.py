import pygame, sys, pickle, os
from math import sqrt

def Win():
    global button_c_flag
    flag1 = True
    pygame.mouse.set_visible(True)
    tot = total()
    while flag1:
        screen.blit(loadimg, loadimg_rect)
        draw_button()
        font_get(font48, "You Win", (size[0] / 2 - 70, 20), red)
        font_get(font18, str(' '.join(['Reflections:', str(reflection)])), (size[0] / 2 - 100, size[1] / 2 + 20), red)
        font_get(font18, str(' '.join(['Score:', str(score)])), (size[0] / 2 - 100, size[1] / 2 + 40), red)
        if reflection != 0:
            font_get(font18, str(' '.join(['You`r efficiency:', "%6.2f" % (1.0 * score / reflection)])),
                (size[0] / 2 - 100, size[1] / 2 + 60), black)
        font_get(font18, str(' '.join(['Level score:', str(tot)])), (size[0] / 2 - 100, size[1] / 2 + 80), red)
        font_get(font18, str(' '.join(['Total:', str(total_score)])), (size[0] / 2 - 100, size[1] / 2 + 100), red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_app()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flag1 = False
                elif event.key == pygame.K_ESCAPE:
                    quit_app()
            elif event.type == pygame.MOUSEBUTTONUP:
                flag1 = button_press(pygame.mouse.get_pos(), 'up')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = button_press(pygame.mouse.get_pos(), 'down')
        pygame.display.flip()
    if button_c_flag == False: continue_app()
    if button_q_flag == True: quit_app()
    pygame.mouse.set_visible(False)


def Load():
    global button_c_flag
    flag1 = True
    pygame.mouse.set_visible(True)
    while flag1:
        screen.blit(loadimg, loadimg_rect)
        draw_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_app()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flag1 = False
                elif event.key == pygame.K_ESCAPE:
                    quit_app()
            elif event.type == pygame.MOUSEBUTTONUP:
                flag1 = button_press(pygame.mouse.get_pos(), 'up')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = button_press(pygame.mouse.get_pos(), 'down')
        if flag1 == None: flag1 = True
        pygame.display.flip()
    if button_q_flag == True: quit_app()
    pygame.mouse.set_visible(False)


def events():
    global angle_flag, stx, tmp_x, flag, square_list
    for event in pygame.event.get(): #get event list and check events
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN: #init event then any key is pressed
            if event.key == LEFT:
                stx = -3
            elif event.key == RIGHT:
                stx = 3
            elif event.key == pygame.K_ESCAPE: # pressing escape quits
                pygame.display.quit()
                sys.exit(0)
        elif event.type == pygame.KEYUP:#init event then any key is loosen
            stx = 0
        elif event.type == pygame.MOUSEMOTION: #init event move mouse
            tmp_x[0] = pygame.mouse.get_pos()[0]
            tmp_x[1] = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if angle_flag == False and Ball_rect.colliderect(stic_rect):
                angle()
                angle_flag = True


def continue_game():
    global x, y, angle_flag, score, FPS, reflection, flag
    x, y = 0, 0
    stic_rect.topleft = (size[0] / 2 - stic_rect.w / 2, size[1] - stic_rect.h - 1 - 50)
    screen.blit(stic, stic_rect)
    Ball_rect.midbottom = stic_rect.midtop
    Ball_rect.midbottom = (Ball_rect.midbottom[0], Ball_rect.midbottom[1] + 1)
    screen.blit(image, Ball_rect)
    pygame.mouse.set_visible(False)
    angle_flag = False
    flag = False


def continue_app():
    global x, y, angle_flag, score, FPS, reflection, flag
    x, y = 0, 0
    FPS = 120
    score = 0
    reflection = 0
    stic_rect.topleft = (size[0] / 2 - stic_rect.w / 2, size[1] - stic_rect.h - 1 - 50)
    screen.blit(stic, stic_rect)
    Ball_rect.midbottom = stic_rect.midtop
    Ball_rect.midbottom = (Ball_rect.midbottom[0], Ball_rect.midbottom[1] + 1)
    screen.blit(image, Ball_rect)
    CreateLevel(num)
    pygame.mouse.set_visible(False)
    angle_flag = False
    flag = False


def quit_app():
    pygame.display.quit()
    sys.exit(0)


def font_get(font, text, pos, color):
    text = font.render(text, 1, color)
    font_rect = text.get_rect(topleft=pos)
    screen.blit(text, font_rect)


def draw_button():
    if button_c_flag:
        screen.blit(button, button_continue)
    if button_q_flag:
        screen.blit(button, button_quit)


def button_press(pos, event):
    global button_c_flag, button_q_flag
    if button_continue.top < pos[1] < button_continue.bottom and button_continue.left < pos[0] < button_continue.right:
        if event == 'down':
            button_c_flag = True
            return button_c_flag
        elif event == 'up':
            button_c_flag = False
            return button_c_flag
    elif button_quit.top < pos[1] < button_quit.bottom and button_quit.left < pos[0] < button_quit.right:
        if event == 'down':
            button_q_flag = False
            return True
        elif event == 'up':
            button_q_flag = True
            return False


def angle():
    global x, y
    center_stick = stic_rect.center[0]
    center_ball = Ball_rect.center[0]
    center = center_stick - center_ball
    multiplier = stic_rect.w / 6
    if x > 0:
        if center < 0:
            multiplier_x = 1
        elif center > 0:
            multiplier_x = -1
    elif x < 0:
        if center < 0:
            multiplier_x = 1
        elif center > 0:
            multiplier_x = -1
    elif (x, y) == (0, 0):
        if center < 0:
            multiplier_x = 1
        elif center > 0:
            multiplier_x = -1
        elif center == 0:
            multiplier_x = 0
    else:
        multiplier_x = 1
    if center == 0:
        x, y = 0, -3
    elif 0 < abs(center) < multiplier:
        x, y = 1 * multiplier_x, -3
    elif multiplier < abs(center) < multiplier * 2:
        x, y = 2 * multiplier_x, -2
    elif multiplier * 2 < abs(center) < multiplier * 3:
        x, y = 3 * multiplier_x, -1


def CreateLevel(a):
    global qt, ql, num
    try:
        list_lev[a]
    except:
        a = 0
        num = 0
    levels = open(list_lev[a], 'rb')
    blocks = pickle.load(levels)
    levels.close()
    qt1 = qt
    for i, j in enumerate(blocks):
        qt1 = qt1 + 2
        for e, r in enumerate(j):
            if r != 0: square_list.append(pygame.Rect(ql + (qw * e) + e * 1, qt1 + (i * qh), qw, qh))


def lose_screen():
    global x, y, angle_flag, score, FPS, reflection, flag
    global button_c_flag
    flag1 = True
    tot = total()
    pygame.mouse.set_visible(True)
    while flag1:
        screen.blit(loadimg, loadimg_rect)
        draw_button()
        font_get(font48, "You lose", (size[0] / 2 - 70, 20), red)
        font_get(font20, str(' '.join(['reflections:', str(reflection)])), (size[0] / 2 - 100, size[1] / 2 + 20), red)
        font_get(font20, str(' '.join(['score:', str(score)])), (size[0] / 2 - 100, size[1] / 2 + 40), red)
        if reflection != 0:
            font_get(font18, str(' '.join(['You`r efficiency:', "%6.2f" % (1.0 * score / reflection)])),
                (size[0] / 2 - 100, size[1] / 2 + 60), black)
        font_get(font18, str(' '.join(['Level score:', str(tot)])), (size[0] / 2 - 100, size[1] / 2 + 80), red)
        font_get(font18, str(' '.join(['Total:', str(total_score)])), (size[0] / 2 - 100, size[1] / 2 + 100), red)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_app()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flag1 = False
                elif event.key == pygame.K_ESCAPE:
                    quit_app()
            elif event.type == pygame.MOUSEBUTTONUP:
                flag1 = button_press(pygame.mouse.get_pos(), 'up')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                flag1 = button_press(pygame.mouse.get_pos(), 'down')
        if flag1 == None: flag1 = True
        pygame.display.flip()
    if button_q_flag == True: quit_app()
    if button_c_flag == False: continue_app()
    pygame.mouse.set_visible(False)


def load_levels():
    path = os.getcwd()
    path = path + '/levels/'
    path = os.path.abspath(path)
    list_files = []
    for i in os.listdir(path):
        if i.split('.')[-1] == 'arc':
            list_files.append((path + '/' + i))
    return list_files


def total():
    global total_score
    if reflection != 0:
        a = 1.0 * score / reflection
    else:
        a = 0
    total = score * 10 + lives * 100 + a * 1000
    total = float("%6.2f" % total)
    total_score += total
    return "%6.2f" % total

#vars
total_score = 0
num = 0
lives = 3
flag = True
but_size = (92, 32)
FPS = 120
button_c_flag = False
button_q_flag = False
x, y = 0, 0
RIGHT, LEFT = pygame.K_RIGHT, pygame.K_LEFT
square_list = []
square = -1
size = 500, 550
qw = (size[0] - 40) / 10
ql, qt, qh = 20, 60, 20
game_back_color = (255, 255, 255)
square_color = (255, 125, 0)
back_color = (125, 125, 0)
font_color = (0, 0, 0)
tmp_x = [0, False]
angle_flag = False
#colors
red = (255, 0, 0)
magenta = (255, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
#files
#init python game
pygame.init()
fps = pygame.time.Clock()
#configure pygame & init pygame variable
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(size)
image = pygame.image.load('ball.gif')
stic = pygame.image.load('stic.bmp')
background = pygame.image.load('disp.jpg')
loadimg = pygame.image.load('back.png')
button = pygame.image.load('down.png')
game_back = pygame.image.load('game_back.png')
game_back = game_back.convert()
game_back_rect = game_back.get_rect(topleft=(0, 0))
loadimg.convert()
loadimg_rect = loadimg.get_rect(topleft=(0, 0))
stic_rect = stic.get_rect()
Ball_rect = image.get_rect()
background_rect = background.get_rect(midbottom=(size[0] / 2, size[1]))
button_continue = button.get_rect(topleft=(204, 204))
button_quit = button.get_rect(topleft=(204, 244))
amd = Ball_rect.h / 2
#init Fonts
pygame.font.init()
font10 = pygame.font.Font('Prestige Normal.ttf', 10)
font12 = pygame.font.Font('Prestige Normal.ttf', 12)
font14 = pygame.font.Font('Prestige Normal.ttf', 14)
font18 = pygame.font.Font('Prestige Normal.ttf', 18)
font20 = pygame.font.Font('Prestige Normal.ttf', 20)
font22 = pygame.font.Font('Prestige Normal.ttf', 22)
font48 = pygame.font.Font('Prestige Normal.ttf', 48)
#Calculate variable
score = 0
reflection = 0
stic_rect.topleft = (size[0] / 2 - stic_rect.w / 2, size[1] - stic_rect.h - 1 - 50)
stx, sty = size[0] / 2 - stic_rect.w / 2, 0
#
list_lev = load_levels()
#create blocks
CreateLevel(num)
#do visible stic & ball
Ball_rect.midbottom = stic_rect.midtop
Ball_rect.midbottom = (Ball_rect.midbottom[0], Ball_rect.midbottom[1] + 1)
screen.blit(stic, stic_rect)
screen.blit(image, Ball_rect)
#run game process
Load()
while 1:
    tmp_x[1] = False #set move mouse = false
    screen.fill(game_back_color) #fill visible screen to square_color *,*,*
    screen.blit(game_back, game_back_rect)
    events()
    Ball_rect = Ball_rect.move(x, y) #move ball
    for i in square_list: #draw blocks
        pygame.draw.rect(screen, square_color, i)
    if Ball_rect.colliderect(stic_rect): #check collides ball & stick
        if angle_flag:
            angle() #"GO away ball!"
            Ball_rect.bottom = stic_rect.top + 1
            FPS += 2 #go faster!
            reflection += 1
    square = Ball_rect.collidelist(square_list) #check collide ball & squares
    if square != -1: #if ball collides with square 'square'
        score += 1
        center_ball = Ball_rect.center #where square center of ball?
        if  square_list[square].midleft[0] <= center_ball[0] <= square_list[square].midright[0]:
            if square_list[square].centery < Ball_rect.centery:
                Ball_rect.top = square_list[square].bottom
            else:
                Ball_rect.bottom = square_list[square].top
            y = -y #"GO away ball!"
            del square_list[square] #remove square
        elif square_list[square].midtop[1] <= center_ball[1] <= square_list[square].midbottom[1]:
            if square_list[square].centerx < Ball_rect.centerx:
                Ball_rect.left = square_list[square].right
            else:
                Ball_rect.right = square_list[square].left
            x = -x
            del square_list[square]
        else:
            if square_list[square].left > Ball_rect.centerx:
                mx = square_list[square].left - Ball_rect.centerx
            elif square_list[square].right < Ball_rect.centerx:
                mx = Ball_rect.centerx - square_list[square].right
            if square_list[square].top > Ball_rect.centery:
                my = square_list[square].top - Ball_rect.centery
            elif square_list[square].bottom < Ball_rect.centery:
                my = Ball_rect.centery - square_list[square].bottom
            mx1 = mx * mx
            my1 = my * my
            mg = sqrt(mx1 + my1)
            if mg <= 4.7:
                if mx < my:
                    y = -y
                    del square_list[square]
                elif mx > my:
                    x = -x
                    del square_list[square]
                elif mx == my:
                    x = -x
                    del square_list[square]
        if square_list == []: # if list squares's is empty
            lives += 1
            num += 1
            pygame.mouse.set_visible(True)
            Win()     # do "Game over"
    if Ball_rect.left < 0 or Ball_rect.right > size[0]: ## next 4 strings checks collide ball & edges window
        x = -x
    if Ball_rect.top < 20:
        y = -y
    if  Ball_rect.bottom > size[1]: # do "Game over" if ball is loose
        if lives > 0:
            lives -= 1
            flag = True
            continue_game()
        else:
            square_list = []
            num = 0
            lives = 3
            flag = True
            total_score = 0
            lose_screen()
    if stic_rect.left < 0: # next 4 "if's" remove sticking ball to edges
        stx = 0
        stic_rect.left = stic_rect.left + 1
    if stic_rect.right > size[0]:
        stx = 0
        stic_rect.left = stic_rect.left - 1
    if stic_rect.top < 0 or stic_rect.bottom > size[1]:
        sty = 0
    if tmp_x[1]: # move stick by mouse
        stic_rect.centerx = tmp_x[0]
        if stic_rect.left < 0:
            stic_rect.left = 0
        if stic_rect.right > size[0]:
            stic_rect.right = size[0]
    stic_rect.move_ip(stx, sty) #move stick
    screen.blit(stic, stic_rect)
    screen.blit(image, Ball_rect)
    pygame.draw.line(screen, red, (0, 18), (size[0], 18))
    font_get(font14, str(' '.join(['score:', str(score)])), (3, 4), red)
    font_get(font14, str(' '.join(['reflections:', str(reflection)])), (75, 4), red)
    font_get(font14, str(' '.join(['speed: +', "%6.2f" % ((FPS / 120.0) * 100 - 100), '%'])), (195, 4), red)
    font_get(font14, str(' '.join(['lives:', str(lives)])), (315, 3), red)
    font_get(font14, str(' '.join(['level:', str(num + 1)])), (385, 3), red)
    pygame.display.flip()
    fps.tick(FPS)