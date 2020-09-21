import pygame
import math
import random
from pygame import mixer
import time
import csv

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
mixer.music.load("background.mp3")
#mixer.music.play(-1)

#texts
over_text= pygame.font.Font('freesansbold.ttf', 70)
font = pygame.font.Font('freesansbold.ttf', 32)
font_small = pygame.font.Font('freesansbold.ttf', 25)

#PLAYER
playerimg = pygame.image.load("spaceship.png")
playerX= 370
playerY = 480
vel = 3
def player(x):
     screen.blit(playerimg , (x, playerY))
#start page
def start():
     global run
     start = True
     while start:
          for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()
                  elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                         run = True
                         start = False
                    elif event.key == pygame.K_q:
                         pygame.quit()
                         quit()
                    elif event.key == pygame.K_s:
                         shop()
          screen.fill((255,255,255))
          start_text = over_text.render("SPACE INVADERS", True, (0,0,0))
          screen.blit(start_text, (100, 50))
          obj_text_1 = font_small.render('The objective of Space Invaders, is to pan across a screen and', True, (0,0,0))
          obj_text_2 = font_small.render("shoot descending swarms of aliens, preventing them from", True, (0,0,0))
          obj_text_3 = font_small.render("reaching the bottom of the screen.", True, (0,0,0))
          screen.blit(obj_text_1, (20,200))
          screen.blit(obj_text_2, (20,230))
          screen.blit(obj_text_3, (20,260))
          instruction_text_1 = font_small.render("Instructions: ",True, (0,0,255))
          instruction_text_2 = font_small.render("1. Use Side Keys to Move Spaceship. ",True, (0,0,255))
          instruction_text_3 = font_small.render("2. Use Spacebar Key to fire Bullet. ",True, (0,0,255))
          instruction_text_4 = font_small.render("3. Press P Key to Pause the Game. ",True, (0,0,255))
          screen.blit(instruction_text_1, (20,320))
          screen.blit(instruction_text_2, (80,350))
          screen.blit(instruction_text_3, (80,380))
          screen.blit(instruction_text_4, (80,410))
          shop_text = font.render("Press S to Shop", True, (155, 105, 50))
          screen.blit(shop_text, (20, 470))
          shopcart = pygame.image.load("shop.png")
          screen.blit(shopcart , ( 273 , 477))
          game_text = font.render("Press A to Start the Game", True, (255,0,0))
          screen.blit(game_text, (180,550))
          pygame.display.update()
     
#pause
def pause():
     paused = True
     while paused:
        for event in pygame.event.get():
             global run
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    paused = False
                    run = True
               elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
     
        screen.fill((255,255,255))
        pause_text = over_text.render("PAUSED", True, (0,0,0))
        screen.blit(pause_text, (250, 200))
        inst_text = font.render("Press C to Continue and Press Q to Quit", True, (0,0,0))
        screen.blit(inst_text, (90,300))
        pygame.display.update()
#Shop
def shop():
     global select_status
     buy = True
     start = False
     select_status=False
     while buy:
          screen.fill((255,255,255))
          img1 = pygame.image.load("spaceship1 view.png")
          img2 = pygame.image.load("spaceship2 view.png")
          img3 = pygame.image.load("spaceship3 view.png")
          img4 = pygame.image.load("spaceship4 view.png")
          img5 = pygame.image.load("spaceship5 view.png")
          shop_text = font.render("Shop ", True, (255,0,0))
          screen.blit(shop_text, (10, 10))
          shopcart = pygame.image.load("shop.png")
          screen.blit(shopcart , ( 95 , 16))
          screen.blit(img1 , ( 50 , 100))
          num1_text = font_small.render("Press 1", True, (0,0,0))
          screen.blit(num1_text, (70, 230))
          screen.blit(img2 , ( 350 , 100))
          num2_text = font_small.render("Press 2", True, (0,0,0))
          screen.blit(num2_text, (370, 230))
          screen.blit(img3 , ( 650 , 100))
          num3_text = font_small.render("Press 3", True, (0,0,0))
          screen.blit(num3_text, (670, 230))
          screen.blit(img4 , ( 50 , 350))
          num4_text = font_small.render("Press 4", True, (0,0,0))
          screen.blit(num4_text, (70, 480))
          screen.blit(img5 , ( 350 , 350))
          num5_text = font_small.render("Press 5", True, (0,0,0))
          screen.blit(num5_text, (370, 480))
          inst_text2 = font.render("Press C to Continue", True, (255,0,0))
          screen.blit(inst_text2, (250,550))
          for event in pygame.event.get():
             global run
             global playerimg
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
               elif event.key == pygame.K_1:
                    i="1"
                    select("1")
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
               elif event.key == pygame.K_2:
                    i="2"
                    select("2")
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
               elif event.key == pygame.K_3:
                    i="3"
                    select("3")
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
               elif event.key == pygame.K_4:
                    i="4"
                    select(i)
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
               elif event.key == pygame.K_5:
                    i="5"
                    select("5")
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
               elif event.key == pygame.K_c:
                    buy = False
                    run = True
               elif select_status:
                    global t
                    t=event.key
                    print(t)
                    select(i)

          try:
               screen.blit(inst_text,(210,50))
               pygame.display.update()
          except NameError:
               None
          pygame.display.update()
          
#select spaceship and start
def select(i):
     global select_status
     global run,buy,coins
     global inst_text
     global t,playerimg
     select_status=True
     if i in ships["bought"]:
          inst_text = font.render("Press D to select spaceship"+str(i), True, (0,0,255))
          global run
          global buy
          try:
               if t== pygame.K_d:
                    playerimg = pygame.image.load("spaceship"+str(i)+".png")
                    inst_text = font.render(str(i)+"th spaceship selected", True, (0,0,255))
                    screen.blit(inst_text,(210,50))
                    pygame.display.update()
                    ships["selected"]=i
                    buy = False
                    run= True
                    select_status=False
                    t=0
          except NameError:
               None
     elif i not in ships["bought"]:
          cost=str((int(i))*100)
          inst_text=font.render("Press B to buy it  Price:"+cost, True,(0,0,255))
          screen.blit(inst_text, (210, 50))
          pygame.display.update()
          try:
               if t== pygame.K_b:
                    if coins>=int(cost):
                         coins=coins-int(cost)
                         ships["bought"]=ships["bought"]+str(i)
                         ships["selected"]=str(i)
                         save_ships()
                         playerimg = pygame.image.load("spaceship"+str(i)+".png")
                         buy=False
                         run=True
                         select_status=False
                         t=0
                    else:
                         inst_text=font.render("Not Enough Coins", True,(0,0,255))
                         screen.blit(inst_text, (210, 50))
                         pygame.display.update()
                         select_status=False
                         t=0
          except NameError:
               None
               
#loading last selected spaceship and bought spaceships
f=open("shops.csv")
ships={}
list_2=[]
r=csv.reader(f)
for row in r:
     list_2.append(row)
ships["selected"]=list_2[0][0]
ships["bought"]=list_2[0][1]
def save_ships():
     f=open("shops.csv","w")
     w=csv.DictWriter(f,{"selected","bought"})
     w.writerow({"selected":ships["selected"],"bought":ships["bought"]})
     
#Reward
rewardimg=pygame.image.load("money.png")
reward_state="ready"
rewardX=0
rewardY=40
rewardY_change=2
def reward():
     global reward_state,rewardY_change,rewardX,rewardY
     i=random.randint(1,10)
     if i==4 :
          reward_state="fire"
          rewardY_change=random.randint(1,3)
          rewardX=random.randint(50,700)
          rewardY=40
          screen.blit(rewardimg,(rewardX,rewardY))
def reward_collision():
     global coins,reward_state,rewardY_change,rewardX,rewardY
     if collision(playerX,playerY,rewardX,rewardY):
          coins=coins+(rewardY_change)
          rewardY=0
          rewardX=0
          reward_state="ready"

#Blast power
num_enemy=6
power_state=100
def blast():
     global power_state,score
     power_state=power_state-20
     for i in range(num_enemy):
          if enemyY[i]>350:
               score += 1
               enemyX[i]= random.randint(0, 735)
               enemyY[i] = random.randint(40, 150)
               power_state+=1
               enemy(enemyX[i],enemyY[i],i)

#machine gun power
smg_state=0
def smg():
     global power_state,bulletY_change,smg_state,bulletimg1,bulletimg2,bulletimg3,bulletimg
     smg_state=1000
     power_state=power_state-40
     bulletY_change=20
     bulletimg1 = pygame.image.load("smg.png")
     bulletimg3 = pygame.image.load("smg.png")
     bulletimg2 = pygame.image.load("smg.png")
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
def not_smg():
     global power_state,bulletY_change,bulletimg1,bulletimg2,bulletimg3,bulletimg
     bulletY_change=10
     bulletimg1 = pygame.image.load("bullet.png")
     bulletimg2 = pygame.image.load("bullet.png")
     bulletimg3 = pygame.image.load("bullet.png")
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]

#shotgun
shotgun_state=0
bulletimg2 = pygame.image.load("bullet.png")
bulletimg3 = pygame.image.load("bullet.png")
def shotgun():
     global power_state,shotgun_state
     power_state=power_state-30
     shotgun_state=1000

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
bulletimg1 = pygame.image.load("bullet.png")
bulletX=[0,0,0,0]
bulletY =[480,480,480,480]
bulletY_change = 10
bullet_state =["ready","ready","ready","ready"]
bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
def fire (x, y,p,i):
     global bullet_state
     bullet_state[i] = "fire"
     screen.blit(p, (x+16, y+10))

#Collision
def collision (enemyX, enemyY, bulletX , bulletY):
     distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
     if distance < 27:
          return True
     else:
          return False

#Score
score = 0
def show_score():
     score_v = font.render("Score: " + str(score), True, (255,255,255))
     screen.blit(score_v, (10, 10))

#Highscore
list_1=[]
highscore= {}
f=open("highscore.csv", "r")
r=csv.reader(f)
for row in r:                 #Loading the saved data of highscore
     list_1.append(row)
highscore["coins"]=list_1[0][0]
highscore["score"]=list_1[0][1]
f.close()
def show_highscore():
     highscore_v=font.render("Highscore: "+ str(highscore["score"]),True,(255,255,255))
     screen.blit(highscore_v,(280,10))
def save_highscore():         #Saves new highscore
     if int(score)>=int(highscore["score"]):
          over_text= pygame.font.Font('freesansbold.ttf', 50)
          new_highscore=over_text.render("!!! NEW HIGHSCORE !!!",True,(255,255,255))
          screen.blit(new_highscore,(150,350))
          f=open("highscore.csv","w",newline='')
          w=csv.DictWriter(f,{"coins","score"})
          w.writerow({"coins":coins,"score":score})
          f.close()
          show_highscore()
     else:
          save_coins()
          
#coins
coins=int(highscore["coins"])
def show_coins():
     coins_v = font.render("Coins: " + str(coins), True, (255,255,255))
     screen.blit(coins_v, (620, 10))
def save_coins():
     f=open("highscore.csv","w",newline='')
     w=csv.DictWriter(f,{"coins","score"})
     w.writerow({"coins":coins,"score":highscore["score"]})
     f.close()

#Game Over
def game_over_text():
     game_over = over_text.render("GAME OVER", True, (255,255,255))
     screen.blit(game_over, (200, 250))
     
#Main Loop
start()
while run:
     #RGB - Red, Green, Blue
     screen.fill((0,0,0))
     screen.blit(bg, (0,0))

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
          elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_p:
                          run = False
                          pause()
                  elif event.key == pygame.K_q:
                          pygame.quit()
                          quit()
                   
     #alternate mechanic and continous method
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and playerX>0 :
          playerX -= vel
     if keys[pygame.K_RIGHT] and playerX<736 :
          playerX += vel
     if keys[pygame.K_SPACE]:
          if shotgun_state>0:
               if bullet_state==["ready","ready","ready","ready"]:
                    for p in range(1,4):                         
                         if smg_state==0:
                              bulletX[p] = playerX
                         elif smg_state>0:
                              bulletX[p]=playerX-47
                              bulletY[p]=playerY-30
                         fire(bulletX[p],bulletY[p],bulletimg[p],p)
          else:
               if bullet_state[1] is "ready" :
                    # current coordinate of spaceship
                    if smg_state==0:
                         bulletX[1] = playerX
                    elif smg_state>0:
                         bulletX[1]=playerX-47
                         bulletY[1]=playerY-30
                    fire(bulletX[1], bulletY[1],bulletimg1,1)
     if keys[pygame.K_b] :
          if power_state>=20:
               blast()
     if keys[pygame.K_n] and smg_state==0:
          if power_state>=40:
               smg()
     if keys[pygame.K_s] and shotgun_state==0:
          if power_state>=30:
               shotgun()
               
     #smg timer
     if smg_state>0:
          smg_state=smg_state-1
     elif smg_state==0:
          not_smg()

     #shotgun timer
     if shotgun_state>0:
          shotgun_state=shotgun_state-1
     elif shotgun_state==0:
          bullet_state[2]="ready"
          bullet_state[3]="ready"
          bulletY[2]=480
          bulletY[3]=480
          
     # enemy movement
     for i in range(num_enemy):
          if enemyY[i] >= 440:
               for j in range (num_enemy):
                    enemyY[j] = 2000
                    game_over_text()
                    save_highscore()
                    rewardY_change=0
               break
     
          enemyX[i] = enemyX[i] + X_change[i]
          if enemyX[i] <= 0:
               X_change[i] = 3
               enemyY[i] = enemyY[i] + Y_change[i]
          elif enemyX[i] >= 736:
               X_change[i] = -3
               enemyY[i] = enemyY[i] + Y_change[i]
          #collision check
          for j in range(1,4):
               collisions = collision (enemyX[i] , enemyY[i] , bulletX[j] , bulletY[j])
               if collisions:
                    bulletY[j] = 480
                    bullet_state[j] = "ready"
                    score += 1
                    power_state+=1
                    reward()
                    enemyX[i]= random.randint(0, 735)
                    enemyY[i] = random.randint(40, 150)

          enemy(enemyX[i], enemyY[i], i)
     reward_collision()
     
     # Bullet movement
     for q in range(1,4):
          if q==1:
               if bullet_state[1] is "fire":
                    fire(bulletX[1], bulletY[1],bulletimg[1],1)
                    bulletY[1] -= bulletY_change
               if bulletY[1] <= 0:
                    bulletY[1] = 480
                    bullet_state[1] = "ready"
          if q==2 and shotgun_state>0:
               if bullet_state[2] is "fire":
                    bulletY[2] -= bulletY_change
                    bulletX[2] -=bulletY_change/2
                    fire(bulletX[2], bulletY[2],bulletimg[2],2)
               if bulletY[2] <= 0 or bulletX[2]<=0:
                    bulletY[2] = 480
                    bullet_state[2] = "ready"
          if q==3 and shotgun_state>0:
               if bullet_state[3] is "fire":
                    bulletY[3] -= bulletY_change
                    bulletX[3] +=bulletY_change/2
                    fire(bulletX[3], bulletY[3],bulletimg[3],3)
               if bulletY[3] <= 0 or bulletX[3]>=735:
                    bulletY[3] = 480
                    bullet_state[3] = "ready"
                    
     # Reward movement
     if reward_state is "fire":
          rewardY+=rewardY_change
          screen.blit(rewardimg,(rewardX,rewardY))
     if rewardY>=480:
          rewardY=0
          reward_state="ready"

     player(playerX)
     show_score()
     show_highscore()
     show_coins()
     pygame.display.update()

pygame.quit()


