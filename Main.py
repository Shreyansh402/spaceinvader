import pygame
import math
import random
from pygame import mixer 

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#background image and sound
bg= pygame.image.load("space.jpg")
'''mixer.music.load("background.mp3")
mixer.music.play(-1)'''

#PLAYER
playerimg = pygame.image.load("spaceship.png")
playerX= 370
playerY = 480
vel = 4
def player(x):
     screen.blit(playerimg , (x, playerY))

#Enemy
enemyimg = [ ]
enemyX = [ ]
enemyY = [ ]
X_change = [ ]
Y_change = [ ]
num_enemy = 6

for i in range(num_enemy):
     enemyimg.append(pygame.image.load("enemy.png"))
     enemyX.append(random.randint(0, 735))
     enemyY.append(random.randint(40, 150))
     X_change.append(3)
     Y_change.append(40)
     
def enemy(x , y, i):
     screen.blit(enemyimg[i] , (x, y))

#bullet (Ready = can't see bulet and Fire = bullet current moving)
bulletimg = pygame.image.load("bullet.png")
bulletX= 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"
def fire (x, y):
     global bullet_state
     bullet_state = "fire"
     screen.blit(bulletimg, (x+16, y+10))

#Collision
def collision (enemyX, enemyY, bulletX , bulletY):
     distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
     if distance < 27:
          return True
     else:
          return False

#Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
def show_score():
     score_v = font.render("Score: " + str(score), True, (255,255,255))
     screen.blit(score_v, (textX, textY))

#Game Over
over_text= pygame.font.Font('freesansbold.ttf', 70)
def game_over_text():
     game_over = over_text.render("GAME OVER", True, (255,255,255))
     screen.blit(game_over, (200, 250))

#Main Loop
run = True
while run:
     #RGB - Red, Green, Blue
     screen.fill((0,0,0))
     screen.blit(bg, (0,0))
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
                   
     #Keys Mechanism
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and playerX>0 :
          playerX -= vel
     if keys[pygame.K_RIGHT] and playerX<736 :
          playerX += vel
     if keys[pygame.K_SPACE]:
          if bullet_state is "ready" :
               # current coordinate of spaceship
               bulletX = playerX
               fire(bulletX, bulletY)
          
     # enemy movement
     for i in range(num_enemy):
          if enemyY[i] >= 440:
               for j in range (num_enemy):
                    enemyY[j] = 2000
                    game_over_text()
               break
     
          enemyX[i] = enemyX[i] + X_change[i]
          if enemyX[i] <= 0:
               X_change[i] = 3
               enemyY[i] = enemyY[i] + Y_change[i]
          elif enemyX[i] >= 736:
               X_change[i] = -3
               enemyY[i] = enemyY[i] + Y_change[i]
          #collision check
          collisions = collision (enemyX[i] , enemyY[i] , bulletX , bulletY)
          if collisions:
               bulletY = 480
               bullet_state = "ready"
               score += 1
               enemyX[i]= random.randint(0, 735)
               enemyY[i] = random.randint(40, 150)

          enemy(enemyX[i], enemyY[i], i)

     # Bullet movement
     if bullet_state is "fire":
          fire(bulletX, bulletY)
          bulletY -= bulletY_change
     if bulletY <= 0:
          bulletY = 480
          bullet_state = "ready"

     
     player(playerX)
     show_score()
     pygame.display.update()

pygame.quit()


