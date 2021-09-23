import pygame
import random
import math

from pygame import mixer

# window
# initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
bg = pygame.image.load("dark_blood.jpg")

# bg sound
mixer.music.load("inspiring-8-bit-563.wav")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load("game-console.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("mask _Blue.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy
emeImg = []
eX = []
eY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    emeImg.append(pygame.image.load("virus_yellow.png"))
    eX.append(random.randint(0, 765))
    eY.append(50)
    enemyX_change.append(0.08)
    enemyY_change.append(40)

# bullet
# ready is does not show
# fire means it is shown
bulletImg = pygame.image.load("hospital.png")
bulletX = 0
bulletY = 485
bullet_changeY = 0.3
bullet_changeX = 0
bullet_state = "ready"

# score
score = 0
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
tx = 10
ty = 10
# bullet 2

def show_score(x, y):
    s = font.render("score:"+ str(score_value), True, (255, 255, 255))
    screen.blit(s, (x, y))

def emeny(x, y, i):
    screen.blit(emeImg[i], (x, y))


def player(x, y):
    # blit means to draw
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y + 5))


# collision
def is_collision(ex, bx, ey, by):
    d = math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    if d < 27:
        return True
    else:
        return False


# crash
def crash(ex, px, ey, py):
    d = math.sqrt((math.pow(ex - px, 2)) + (math.pow(ey - py, 2)))
    if d < 10:
        return True
    else:
        return False

# game loop
running = True
while running:
    # color or rgb
    screen.fill("Black")

    # background display
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if press key to check left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            # bullet button

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundires
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 770:
        playerX = 770

    # enemy moment
    for i in range(num_of_enemy):
        eX[i] += enemyX_change[i]
        if eX[i] <= 0:
            enemyX_change[i] = 0.08
            eY[i] += enemyY_change[i]
        elif eX[i] >= 770:
            enemyX_change[i] = -0.08
            eY[i] += enemyY_change[i]
        # collision
        collision = is_collision(eX[i], bulletX, eY[i], bulletY)
        if collision:
            bulletY = 485
            bullet_state = "ready"
            score_value += 1
            eX[i] = random.randint(0, 800)
            eY[i] = 50

        print("they arre here", eX[i], eY[i], i)
        emeny(eX[i], eY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 485
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_changeY

    player(playerX, playerY)
    show_score(tx, ty)
    pygame.display.update()
