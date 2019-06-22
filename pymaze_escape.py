# PyMaze Escape Game by Christopher Rodriguez - 5th Period
# February 4, 2019 (completed Feb. 20, 2019)


# Imports
import pygame
import intersects
import os
import sys

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS + '/'
else:
    application_path = os.path.dirname(__file__) + '/'


# Initialize game engine
pygame.init()


# Window
HEIGHT = 720
WIDTH = 1280
TITLE = "PyMaze Escape v1.0a"
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TURQUOISE = (0, 255, 255)
BLUE = (0, 64, 255)
PURPLE = (128, 0, 255)
GREEN = (64, 255, 0)
ORANGE = (255, 128, 0)
GRAY = (91, 91, 91)
BABY_BLUE = (185, 209, 247)

# Stages
START = 0
PLAYING = 1
DEAD = 2
END = 3
PAUSE = 4
INSTRUCTIONS = 5


# Fonts
my_font = pygame.font.Font(application_path + "fonts/FengardoNeue_Regular.otf", 50)
my_font_small = pygame.font.Font(application_path + "fonts/FengardoNeue_Regular.otf", 30)
my_font_xsmall = pygame.font.Font(application_path + "fonts/FengardoNeue_Regular.otf", 24)
major_font = pygame.font.Font(application_path + "fonts/EQUIVALENT.ttf", 60)
major_font_sub = pygame.font.Font(application_path + "fonts/EQUIVALENT.ttf", 50)

# Images
startImg = pygame.image.load(application_path + "assets/explosion.png")
startImg_resample = pygame.transform.scale(startImg, (1280, 720))

# Sounds
pygame.mixer.music.load(application_path + "sounds/Bravely Default OST_Infiltrating Enemy Territory.ogg")
coinsfx = pygame.mixer.Sound(application_path + "sounds/coinsfx.ogg")
oversfx = pygame.mixer.Sound(application_path + "sounds/game_over.ogg")

# Setup
def setup():
    global block, block_vx, block_vy, block_speed
    global stage, locked, key, score, points_needed, points_remaining
    global walls, enemy_wall1, enemy_walls, coins, keys, speed_boosters, speed_inhibitors, big_coins
    global end_point, end_gate, mid_gate, players
    
    ''' make player 1 '''
    block = [0, 344, 32, 32]
    block_vx = 0
    block_vy = 0
    block_speed = 2

    ''' set stage and gate states '''
    stage = START
    locked = True
    key = False

    ''' set score data and points needed to win '''
    score = 0
    points_needed = 25

    ''' make walls '''
    wall1 =  [0, 0, 32, 343]
    wall2 =  [0, 377, 32, 360]
    wall3 =  [0, 688, 1280, 32]
    wall4 =  [0, 0, 1280, 32]
    wall5 =  [1248, 0, 32, 309]
    wall6 =  [1248, 343, 32, 378]
    wall7 =  [1194, 343, 54, 32]
    wall8 =  [1194, 277, 54, 32]
    wall9 =  [32, 311, 32, 32]
    wall10 = [32, 377, 32, 32]
    wall11 = [64, 188.5, 32, 155]
    wall12 = [64, 377, 32, 32]
    wall13 = [128, 64, 32, 345.5]
    wall14 = [160, 64, 96, 32]
    wall15 = [256, 64, 32, 592]
    wall16 = [288, 624, 128, 32]
    wall17 = [320, 32, 32, 560]
    wall18 = [384, 64, 32, 592]
    wall19 = [128, 409, 32, 247]
    wall20 = [128, 624, 128, 32]
    wall21 = [64, 377, 32, 279]
    wall22 = [448, 32, 32, 528]
    wall23 = [458, 624, 54, 32]
    wall24 = [512, 624, 32, 64]
    wall25 = [512, 225, 32, 464]
    wall26 = [512, 32, 32, 159]
    wall27 = [544, 159, 32, 32]
    wall28 = [608, 159, 640, 32]
    wall29 = [1088, 277, 64, 32]
    wall30 = [1088, 343, 64, 32]
    wall31 = [608, 64, 32, 96]
    wall32 = [544, 225, 608, 32]
    wall33 = [640, 64, 544, 32]
    wall34 = [1088, 309, 34, 34]
    wall35 = [1136, 257, 16, 24]
    wall36 = [544, 407, 672, 32]
    wall37 = [576, 535, 704, 32]
    wall38 = [544, 615, 672, 32]
    

    walls = [wall1, wall2, wall3, wall4, wall5, wall6,
             wall7, wall8, wall9, wall10, wall11, wall12,
             wall13, wall14, wall15, wall16, wall17, wall18,
             wall19, wall20, wall21, wall22, wall23, wall24,
             wall25, wall26, wall27, wall28, wall29, wall30,
             wall31, wall32, wall33, wall34, wall35, wall36,
             wall37, wall38]

    ''' make enemy walls '''
    enemy_wall1 = [-1312, 0, 1280, 720]

    enemy_walls = [enemy_wall1]

    ''' make coins '''
    coin1 =  [38, 354, 8, 8]
    coin2 =  [72, 354, 8, 8]
    coin3 =  [106, 418, 8, 8]
    coin4 =  [106, 482, 8, 8]
    coin5 =  [106, 546, 8, 8]
    coin6 =  [106, 226, 8, 8]
    coin7 =  [298, 226, 8, 8]
    coin8 =  [298, 258, 8, 8]
    coin9 =  [298, 290, 8, 8]
    coin10 = [298, 322, 8, 8]
    coin11 = [362, 226, 8, 8]
    coin12 = [362, 258, 8, 8]
    coin13 = [362, 290, 8, 8]
    coin14 = [362, 322, 8, 8]
    coin15 = [362, 356, 8, 8]
    coin16 = [362, 390, 8, 8]
    coin17 = [362, 424, 8, 8]
    coin18 = [426, 226, 8, 8]
    coin19 = [426, 258, 8, 8]
    coin20 = [426, 290, 8, 8]
    coin21 = [426, 322, 8, 8]
    coin22 = [426, 356, 8, 8]
    coin23 = [426, 390, 8, 8]
    coin24 = [426, 424, 8, 8]
    coin25 = [576, 207, 8, 8]
    coin26 = [596, 207, 8, 8]
    coin27 = [616, 207, 8, 8]
    coin28 = [636, 207, 8, 8]
    coin29 = [1224, 224, 8, 8]
    coin30 = [1164, 325, 8, 8]
    coin31 = [764, 664, 8, 8]


    coins = [coin1, coin2, coin3, coin4, coin5,
             coin6, coin7, coin8, coin9, coin10,
             coin11, coin12, coin13, coin14, coin15,
             coin16, coin17, coin18, coin19, coin20,
             coin21, coin22, coin23, coin24, coin25,
             coin26, coin27, coin28, coin29, coin30,
             coin31]

    ''' make keys '''
    key1 = [478, 668, 8, 8]

    keys = [key1]

    ''' make 2 speed boosters 16x16 '''
    # speed boosters are + 1 speed
    speed_booster1 = [40, 214, 16, 16]
    speed_booster2 = [1200, 84, 16, 16]

    speed_boosters = [speed_booster1, speed_booster2]

    ''' make 2 speed inhibitors 8x8 '''
    # speed inhibitors are - 1 speed
    speed_inhibitor1 = [82, 667, 8, 8]
    speed_inhibitor2 = [1238, 84, 8, 8]
    

    speed_inhibitors = [speed_inhibitor1, speed_inhibitor2]

    ''' make big money coins here, all in right side '''
    big_money1 = [564, 356, 16, 16]
    big_money2 = [664, 500, 16, 16]
    big_money3 = [1184, 500, 16, 16]
    big_money4 = [664, 580, 16, 16]
    big_money5 = [664, 118, 16, 16]
    big_money6 = [624, 580, 16, 16]

    big_coins = [big_money1, big_money2, big_money3, big_money4,
                 big_money5, big_money6]

    ''' make end point '''
    end_point = [1248, 310, 32, 32]

    ''' make end gate '''
    end_gate = [1194, 310, 32, 32]

    ''' make midway gate '''
    mid_gate = [512, 192, 32, 32]


# Music
def music():
    if stage == PLAYING:
        pygame.mixer.music.play(-1)
    elif stage == START:
        pygame.mixer.music.stop()
    elif stage == PAUSE:
        pygame.mixer.music.pause()
    elif stage == END:
        pygame.mixer.music.stop()
    elif stage == DEAD:
        pygame.mixer.music.stop()
    elif stage == INSTRUCTIONS:
        pygame.mixer.music.stop()


# Game screens
def show_start():
    text1 = major_font.render("PyMaze Escape v1.0a", True, BLUE)
    text2 = major_font_sub.render("(Press SPACE to play and 'i' for instructions!)", True, BLUE)
    text0 = my_font_xsmall.render("Programming by Christopher Rodriguez", True, RED)
    w1 = text1.get_width()
    w2 = text2.get_width()
    w0 = text0.get_width()
    screen.blit(text1, [WIDTH/2 - w1/2, 260])
    screen.blit(text2, [WIDTH/2 - w2/2, 335])
    screen.blit(text0, [WIDTH/2 - w0/2, 680])

def show_instructions():
    text9 = major_font.render("KEYS", True, ORANGE)
    text10 = my_font_xsmall.render("ARROW KEYS = move up/down/left/right", True, BLACK)
    text11 = my_font_xsmall.render("r = restart game", True, BLACK)
    text12 = my_font_xsmall.render("p = pause game", True, BLACK)
    text13 = my_font_xsmall.render("SPACEBAR = resume/proceed (when prompted)", True, BLACK)
    text14 = my_font_xsmall.render("ESC = emergency shutdown key (closes game)", True, BLACK)
    text15 = major_font.render("HOW TO PLAY", True, ORANGE)
    text16 = my_font_xsmall.render("Navigate the player (block) around the maze and try to aquire", True, BLACK)
    text17 = my_font_xsmall.render("the amount of points needed to unlock the purple gate blocking", True, BLACK)
    text18 = my_font_xsmall.render("the turquoise end point without getting hit by the wave of red", True, BLACK)
    text19 = my_font_xsmall.render("lava coming from the left side of the screen.", True, BLACK)
    text20 = my_font_xsmall.render("There are many ways to obtain points. Yellow coins award 1 point,", True, BLACK)
    text21 = my_font_xsmall.render("but be careful of the baby blue coins -- some will decrease your", True, BLACK)
    text22 = my_font_xsmall.render("speed, while others will increase your speed! Look closely and", True, BLACK)
    text23 = my_font_xsmall.render("you will be able to detect which ones are which.", True, BLACK)
    text_l = my_font_xsmall.render("Also, try to get the farthest coin if you dare! (only worth 1 point)", True, BLACK)
    text24 = my_font_small.render("Press SPACE to return!", True, BLACK)
    w9 = text9.get_width()
    w10 = text10.get_width()
    w11 = text11.get_width()
    w12 = text12.get_width()
    w13 = text13.get_width()
    w14 = text14.get_width()
    w15 = text15.get_width()
    w16 = text16.get_width()
    w17 = text17.get_width()
    w18 = text18.get_width()
    w19 = text19.get_width()
    w20 = text20.get_width()
    w21 = text21.get_width()
    w22 = text22.get_width()
    w23 = text23.get_width()
    w_l = text_l.get_width()
    w24 = text24.get_width()
    screen.blit(text9, [WIDTH/2 - w9/2, 32])
    screen.blit(text10, [WIDTH/2 - w10/2, 128])
    screen.blit(text11, [WIDTH/2 - w11/2, 152])
    screen.blit(text12, [WIDTH/2 - w12/2, 176])
    screen.blit(text13, [WIDTH/2 - w13/2, 200])
    screen.blit(text14, [WIDTH/2 - w14/2, 224])
    screen.blit(text15, [WIDTH/2 - w15/2, 320])
    screen.blit(text16, [WIDTH/2 - w16/2, 416])
    screen.blit(text17, [WIDTH/2 - w17/2, 440])
    screen.blit(text18, [WIDTH/2 - w18/2, 464])
    screen.blit(text19, [WIDTH/2 - w19/2, 488])
    screen.blit(text20, [WIDTH/2 - w20/2, 512])
    screen.blit(text21, [WIDTH/2 - w21/2, 536])
    screen.blit(text22, [WIDTH/2 - w22/2, 560])
    screen.blit(text23, [WIDTH/2 - w23/2, 584])
    screen.blit(text_l, [WIDTH/2 - w_l/2, 622])
    screen.blit(text24, [WIDTH/2 - w24/2, 664])


def show_pause():
    text3 = my_font.render("PAUSED", True, ORANGE)
    text4 = my_font.render("(Press SPACE to resume.)", True, ORANGE)
    w3 = text3.get_width()
    w4 = text4.get_width()
    screen.blit(text3, [WIDTH/2 - w3/2, 275])
    screen.blit(text4, [WIDTH/2 - w4/2, 325])

def show_win():
    text5 = major_font.render("YOU WIN!", True, ORANGE)
    text6 = major_font.render("(Press SPACE to play again.)", True, GREEN)
    w5 = text5.get_width()
    w6 = text6.get_width()
    screen.blit(text5, [WIDTH/2 - w5/2, 260])
    screen.blit(text6, [WIDTH/2 - w6/2, 335])

def show_lose():
    text7 = major_font.render("GAME OVER", True, ORANGE)
    text8 = major_font.render("(Press SPACE to play again.)", True, GREEN)
    w7 = text7.get_width()
    w8 = text8.get_width()
    screen.blit(text7, [WIDTH/2 - w7/2, 260])
    screen.blit(text8, [WIDTH/2 - w8/2, 335])



# Moving walls code
def move_enemy_walls(player, vx, vy):
    global stage
    ''' move only in PLAYING stage '''
    if stage == PLAYING:
        for e in enemy_walls:
            ''' intersecting with player results in a GAME OVER '''
            if intersects.rect_rect(player, e):
                if vx > 0:
                    player[0] = e[0] - player[2]
                elif vx < 0:
                    player[0] = e[0] + e[2]
                if vy > 0:
                    player[1] = e[1] - player[3]
                elif vy < 0:
                    player[1] = e[1] + e[3]
                stage = DEAD
                music()
                pygame.mixer.Sound.play(oversfx)
            else:
                enemy_wall1[0] += 0.20

        
# Logic Functions
def move_and_check_walls(player, vx, vy):

        
    ''' move the block in horizontal direction '''
    player[0] += vx

    ''' resolve collision '''
    for wall in walls:
        if intersects.rect_rect(player, wall):
            if vx > 0:
                player[0] = wall[0] - player[2]
            elif vx < 0:
                player[0] = wall[0] + wall[2]

    ''' resolve horizontal collision with end_gate blocking end_point '''       
    if locked == True:
        if intersects.rect_rect(player, end_gate):
            if vx > 0:
                player[0] = end_gate[0] - player[2]
            elif vx < 0:
                player[0] = end_gate[0] + end_gate[2]

    ''' resolve horizontal collision with mid_gate '''       
    if key == False:
        if intersects.rect_rect(player, mid_gate):
            if vx > 0:
                player[0] = mid_gate[0] - player[2]
            elif vx < 0:
                player[0] = mid_gate[0] + mid_gate[2]

    ''' move the block in vertical direction '''
    player[1] += vy
    
    ''' resolve collision '''
    for wall in walls:
        if intersects.rect_rect(player, wall):
            if vy > 0:
                player[1] = wall[1] - player[3]
            elif vy < 0:
                player[1] = wall[1] + wall[3]

            
    ''' resolve vertical collision with end_gate '''
    if locked == True:
        if intersects.rect_rect(player, end_gate):
            if vy > 0:
                player[1] = end_gate[1] - player[3]
            elif vy < 0:
                player[1] = end_gate[1] + end_gate[3]

    ''' resolve vertical collision with mid_gate '''
    if locked == True:
        if intersects.rect_rect(player, mid_gate):
            if vy > 0:
                player[1] = mid_gate[1] - player[3]
            elif vy < 0:
                player[1] = mid_gate[1] + mid_gate[3]



def check_edge(player):
    ''' detect collisions with edges '''
    if player[0] < 0:
            player[0] = 0
    elif player[0] > WIDTH - player[2]:
        player[0] = WIDTH - player[2]


def check_coin(player):
    ''' detect coin colisions '''
    points = 0
    hit_list = []
    for coin in coins:
        if intersects.rect_rect(player, coin):
            points += 1
            pygame.mixer.Sound.play(coinsfx)
            hit_list.append(coin)
            
    ''' remove collected coins '''
    for hit in hit_list:
        coins.remove(hit)

    return points


def check_big_coin(player):
    ''' detect big coin colisions '''
    points = 0
    hit_list_bc = []
    for bc in big_coins:
        if intersects.rect_rect(player, bc):
            points += 5
            pygame.mixer.Sound.play(coinsfx)
            hit_list_bc.append(bc)
            
    ''' remove collected coins '''
    for q in hit_list_bc:
        big_coins.remove(q)

    return points


def check_key(player):
    ''' detect collision with keys '''
    hit_list_k = []
    for k in keys:
        if intersects.rect_rect(player, k):
            pygame.mixer.Sound.play(coinsfx)
            hit_list_k.append(k)

    ''' remove collected keys '''
    for h in hit_list_k:
        keys.remove(h)


def check_speed_status(player):
    global block_speed
    
    ''' detect collision with speed boosters '''
    hit_list_sb = []
    for s in speed_boosters:
        if intersects.rect_rect(player, s):
            pygame.mixer.Sound.play(coinsfx)
            block_speed = block_speed + 1
            hit_list_sb.append(s)

    ''' remove collected boosters '''
    for i in hit_list_sb:
        speed_boosters.remove(i)

    ''' detect collision with speed inhibitors '''
    hit_list_sd = []
    for d in speed_inhibitors:
        if intersects.rect_rect(player, d):
            pygame.mixer.Sound.play(coinsfx)
            block_speed = block_speed - 1
            hit_list_sd.append(d)

    ''' remove collected decreasers '''
    for z in hit_list_sd:
        speed_inhibitors.remove(z)


def check_gate():
    global locked
    global key

    ''' check end_gate '''
    if score >= points_needed:
        locked = False
    else:
        locked = True

    ''' check mid_gate '''
    if len(keys) == 0:
        key = True
    else:
        key = False


def check_goal(player, vx, vy):
    ''' end game '''
    global stage
    if intersects.rect_rect(player, end_point):
        if vx > 0:
                player[0] = end_point[0] - player[2]
        elif vx < 0:
            player[0] = end_point[0] + end_point[2]
        if vy > 0:
                player[1] = end_point[1] - player[3]
        elif vy < 0:
            player[1] = end_point[1] + end_point[3]
        stage = END
        music()
    

# Drawing Functions
def draw_background():
    if stage == START or stage == INSTRUCTIONS:
        screen.fill(WHITE)
        if stage == START:
            screen.blit(startImg_resample, (0, 0))
    else:
        screen.fill(GRAY)

def draw_objects():
    if stage != START and stage != INSTRUCTIONS:
        if locked == True:
            pygame.draw.rect(screen, PURPLE, end_gate)
        else:
            pass

        if key == False:
            pygame.draw.rect(screen, RED, mid_gate)
        else:
            pass

        pygame.draw.rect(screen, TURQUOISE, end_point)
        pygame.draw.rect(screen, GREEN, block)

        for coin in coins:
            pygame.draw.rect(screen, YELLOW, coin)

        for k in keys:
            pygame.draw.rect(screen, RED, k)

        for sb in speed_boosters:
            pygame.draw.rect(screen, BABY_BLUE, sb)

        for si in speed_inhibitors:
            pygame.draw.rect(screen, BABY_BLUE, si)

        for bigcoin in big_coins:
            pygame.draw.rect(screen, YELLOW, bigcoin)

        for w in walls:
            pygame.draw.rect(screen, WHITE, w)

        for e in enemy_walls:
            pygame.draw.rect(screen, RED, e)




def draw_text(stage, score):
    points_remaining = points_needed - score
        
    if stage == PLAYING:
        score_txt = my_font_xsmall.render("Score: " + str(score), 1, BLUE)
        screen.blit(score_txt, [8, 6])

        if score < points_needed:
            remaining_txt = my_font_xsmall.render("Points remaining: " + str(points_remaining), 1, BLUE)
            screen.blit(remaining_txt, [1068, 6])
        else:
            remaining_txt = my_font_xsmall.render("GATE UNLOCKED!", 1, BLUE)
            screen.blit(remaining_txt, [1068, 6])

    if stage == PAUSE:
        show_pause()
    elif stage == START:
        show_start()
    elif stage == INSTRUCTIONS:
        show_instructions()
    elif stage == DEAD:
        show_lose()
    elif stage == END:
        show_win()



# Game loop
setup()
done = False

music()

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' check to see if the X or ESC key is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    music()
                elif event.key == pygame.K_i:
                    stage = INSTRUCTIONS
            elif stage == INSTRUCTIONS:
                if event.key == pygame.K_SPACE:
                    setup()
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
            elif stage == DEAD:
                if event.key == pygame.K_SPACE:
                    setup()
            elif stage == PAUSE:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    pygame.mixer.music.unpause()

    ''' get key states '''
    state = pygame.key.get_pressed()
    
    if stage == PLAYING:
        
        ''' player 1 controls '''
        up = state[pygame.K_UP]
        down = state[pygame.K_DOWN]
        left = state[pygame.K_LEFT]
        right = state[pygame.K_RIGHT]

        ''' player 1 velocity code '''
        if up:
            block_vy = -block_speed
        elif down:
            block_vy = block_speed
        else:
            block_vy = 0
            
        if left:
            block_vx = -block_speed
        elif right:
            block_vx = block_speed
        else:
            block_vx = 0

        if event.type == pygame.KEYDOWN:
            ''' pause game with p key and reset game with r key '''
            if event.key == pygame.K_p:
                stage = PAUSE
                music()
            elif event.key == pygame.K_r:
                setup()
                music()

    # Moving walls function
    move_enemy_walls(block, block_vx, block_vy)

    # Game logic (Check for collisions, update points, etc.)
    ''' player 1 logic '''
    move_and_check_walls(block, block_vx, block_vy)
    check_edge(block)
    score += check_coin(block)
    score += check_big_coin(block)
    check_key(block)
    check_speed_status(block)
    check_gate()
    check_goal(block, block_vx, block_vy)

    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    draw_background()
    draw_objects()
    draw_text(stage, score)

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()



    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
