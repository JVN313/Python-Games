import pygame
from pygame import mixer
import random
import math

from pygame.constants import K_KP_ENTER, K_q

# Intialize the pygame
pygame.init()
mixer.init()

# creation of the screen/window
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\background.png")
mixer.music.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\backgroundMusic.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\battleship.png")
playerX = 370
playerY = 480
playerX_movement = 0

#Enemy/Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_movement = []
enemyY_movement = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50, 150))
    enemyX_movement.append(4)
    enemyY_movement.append(40)

#Laser
laserImg = pygame.image.load(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\laser.png")
laserX = 0
laserY = 480
laserX_movement = 0
laserY_movement = 10
laser_state = "ready"

#Scoreboard
player_score = 0
font = pygame.font.Font("freesansbold.ttf",32)
scoreX = 10
scoreY = 10
rankX = 10
rankY = 40
rank_font = pygame.font.Font("freesansbold.ttf",20)

game_over_font = pygame.font.Font("freesansbold.ttf",70)
game_overX = 200
game_overY = 230

replay_font = pygame.font.Font("freesansbold.ttf",40)
replayX = 125
replayY = 430

#sounds
explosion_sound = mixer.Sound(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\explosionSound.wav")
laser_sound = mixer.Sound(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\LaserSound.wav")

#Object Functions

def score_board(x,y):
    score = font.render("SCORE: " + str(player_score), True, (255,255,255))
    screen.blit(score, (x,y))

def player_rank(x,y):
    global player_score, background
    if player_score >= 50:
        rank = rank_font.render("SPACE RANGER", True, (255,255,255))
        screen.blit(rank, (x,y))

def game_over_message(x,y):
    game_over = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over, (x,y))

def reset(x,y):
    replay = replay_font.render("Fire to replay and ESC to exit", True, (255,255,255))
    screen.blit(replay, (x,y))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_SPACE]:
        exec(open(r"C:\Users\jaebo\Desktop\Projects\Python-Games\PyGames\SpaceInvader\main.py").read())

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x+24,y-10))

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX,enemyY,laserX,laserY):
    distance = (math.sqrt(math.pow(enemyX-laserX,2)) + (math.pow(enemyY-laserY,2)))
    if distance < 38:
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
                    laser_sound.set_volume(0.1)
                    laser_sound.play()
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
    
    #Enemey Actions/Movement
    for i in range(num_of_enemies):
        
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_message(game_overX,game_overY)
            reset(replayX,replayY)

        enemyX[i] += enemyX_movement[i]
        if enemyX[i] <= 0:
            enemyX_movement[i] = 4
            enemyY[i] += enemyY_movement[i]
        elif enemyX[i] >= 736:
            enemyX_movement[i] = -4
            enemyY[i] += enemyY_movement[i]

        collision = isCollision(enemyX[i],enemyY[i],laserX,laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            player_score+= 1
            explosion_sound.play()
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    
    #Laser Movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state == "fire":
        fire_laser(laserX, laserY)
        laserY-= laserY_movement
        
    #Calling Functions
    player(playerX, playerY)
    player_rank(rankX,rankY)
#    enemy(enemyX, enemyY)
    score_board(scoreX,scoreY)
    pygame.display.update()
pygame.quit()