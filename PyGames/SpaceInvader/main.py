import pygame
from pygame import mixer
import random
import math

# Intialize the pygame
pygame.init()
mixer.init()

# creation of the screen/window
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\background.png")
mixer.music.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\backgroundMusic.wav")
mixer.music.set_volume(0.5)
mixer.music.play()

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\battleship.png")
playerX = 370
playerY = 480
playerX_movement = 0

#Enemy
enemyImg = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\enemy.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50, 150)
enemyX_movement = 4
enemyY_movement = 40

#Laser
laserImg = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\laser.png")
laserX = 0
laserY = 480
laserX_movement = 0
laserY_movement = 10
laser_state = "ready"

#Scoreboard
player_score = 0
font = pygame.font.Font("freesansbold.ttf",34)
scoreX = 10
scoreY = 10

#sounds
explosion_sound = mixer.Sound(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\explosionSound.wav")
laser_sound = mixer.Sound(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\LaserSound.wav")

#Object Functions

def score_board(x,y):
    score = font.render("SCORE: " + str(player_score), True, (255,255,255))
    screen.blit(score, (x,y))

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x+24,y-10))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def isCollision(enemyX,enemyY,laserX,laserY):
    distance = (math.sqrt(math.pow(enemyX-laserX,2)) + (math.pow(enemyY-laserY,2)))
    if distance < 35:
        return True
    else:
        return False

# The Game Loop/Master Loop
running = True
while running:
    # Screen Color in RGB Values
    screen.fill((67, 59, 103))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       #Movement/Actions  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_movement = -5

            if event.key == pygame.K_RIGHT:
                playerX_movement = + 5

            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    laserX = playerX
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_movement = 0

    #Setting Boudaries
    playerX += playerX_movement
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_movement
    
    if enemyX <= 0:
        enemyX_movement = 4
        enemyY += enemyY_movement
    elif enemyX >= 736:
        enemyX_movement = -4
        enemyY += enemyY_movement
    #Laser Movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state == "fire":
        fire_laser(laserX, laserY)
        #laser_sound.set_volume(0.1)
        #laser_sound.play()
        laserY-= laserY_movement

    collision = isCollision(enemyX,enemyY,laserX,laserY)
    if collision:
        laserY = 480
        laser_state = "ready"
        player_score+= 1
        explosion_sound.play()
        enemyX = random.randint(0,736)
        enemyY = random.randint(50, 150)
        
    #Calling Functions
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    score_board(scoreX,scoreY)
    pygame.display.update()