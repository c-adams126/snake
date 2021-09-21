import pygame
import random

# window
# initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
bg = pygame.image.load("dark_blood.jpg")

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
emeImg = pygame.image.load("virus_yellow.png")
eX = random.randint(0, 800)
eY = 50
enemyX_change = 0.08
enemyY_change = 40

# bullet
# ready is does not show
# fire means it is shown
bulletImg = pygame.image.load("hospital.png")
bulletX = 0
bulletY = 485
bullet_changeY = 0.3
bullet_changeX = 0
bullet_state = "ready"


def emeny(x, y):
    screen.blit(emeImg, (x, y))


def player(x, y):
    # blit means to draw
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y+5))


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
    eX += enemyX_change

    if eX <= 0:
        eX = 0
        enemyX_change = 0.08
        eY += enemyY_change
    elif eX >= 770:
        eX = 770
        enemyX_change = -0.08
        eY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 485
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_changeY




    emeny(eX, eY)
    player(playerX, playerY)
    pygame.display.update()
