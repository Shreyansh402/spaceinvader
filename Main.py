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
right_limit=735
left_limit=0
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
rewardimg=[pygame.image.load("dynamite.png"),pygame.image.load("money.png"),pygame.image.load("shotgun.png"),pygame.image.load("machine gun.png")]
reward_state=["ready","ready","ready","ready"]
rewardX=[0,0,0,0]
rewardY=[40,40,40,40]
rewardY_change=[2,2,2,2]
def reward():
     global reward_state,rewardY_change,rewardX,rewardY
     i=random.randint(1,500)
     if i<4 and reward_state[0]=="ready":
          reward_state[0]="fire"
          rewardY_change[0]=1
          rewardX[0]=random.randint(50,700)
          rewardY[0]=40
          screen.blit(rewardimg[0],(rewardX[0],rewardY[0]))
     elif  (i>100 and i<200) and reward_state[1]=="ready":
          reward_state[1]="fire"
          rewardY_change[1]=random.randint(1,3)
          rewardX[1]=random.randint(50,700)
          rewardY[1]=40
          screen.blit(rewardimg[1],(rewardX[1],rewardY[1]))
     elif i<10 and reward_state[2]=="ready":
          reward_state[2]="fire"
          rewardY_change[2]=2
          rewardX[2]=random.randint(50,700)
          rewardY[2]=40
          screen.blit(rewardimg[2],(rewardX[2],rewardY[2]))
     elif i<16 and reward_state[3]=="ready":
          reward_state[3]="fire"
          rewardY_change[3]=2
          rewardX[3]=random.randint(50,700)
          rewardY[3]=40
          screen.blit(rewardimg[3],(rewardX[3],rewardY[3]))
def reward_collision():
     global coins,reward_state,rewardY_change,rewardX,rewardY
     if collision(playerX,playerY,rewardX[1],rewardY[1]):
          coins=coins+(rewardY_change[1])
          rewardY[1]=0
          rewardX[1]=0
          reward_state[1]="ready"
     elif collision(playerX,playerY,rewardX[0],rewardY[0]):
          power_state[0]+=1
          rewardY[0]=0
          rewardX[0]=0
          reward_state[0]="ready"
     elif collision(playerX,playerY,rewardX[2],rewardY[2]):
          power_state[1]+=1
          rewardY[2]=0
          rewardX[2]=0
          reward_state[2]="ready"
     elif collision(playerX,playerY,rewardX[3],rewardY[3]):
          power_state[2]+=1
          rewardY[3]=0
          rewardX[3]=0
          reward_state[3]="ready"
          
#Blast power
num_enemy=6
power_state=[1,1,1]
blast_state=0
blastimg=pygame.image.load("blast.png")
def blast():
     global power_state,score,blast_state,playerX,playerY,blastimg
     power_state[0]=power_state[0]-1
     blast_state=40
     blastimg=pygame.image.load("blast.png")
     for i in range(len(enemyX)):
          if enemyY[i]>350:
               score += 1
               enemyX[i]= random.randint(0, 735)
               enemyY[i] = random.randint(40, 150)
               enemy(enemyX[i],enemyY[i],i)

#machine gun power
smg_state=0
def smg():
     global power_state,bulletY_change,smg_state,bulletimg1,bulletimg2,bulletimg3,bulletimg
     smg_state=1000
     power_state[2]=power_state[2]-1
     bulletY_change=2*bulletY_change
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
     power_state[1]=power_state[1]-1
     shotgun_state=1000

#thanos
stones_img={"soul":pygame.image.load("soul stone dead.png"),"power":pygame.image.load("power stone dead.png"),"space":pygame.image.load("space stone dead.png"),"time":pygame.image.load("time stone dead.png"),"reality":pygame.image.load("reality stone dead.png"),"mind":pygame.image.load("mind stone dead.png")}
stones_status={"soul":-1,"power":-1,"space":-1,"time":-1,"reality":-1,"mind":-1}
stones_life={"soul":200,"power":100,"space":100,"time":100,"reality":100,"mind":100}
stones_X={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400}
stones_X2={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400}
stones_Y={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150}
stones_Y2={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150}
laserimg=pygame.image.load("laser.png")
laserimg=pygame.transform.scale(laserimg,(10,500))
for i in stones_img.keys():
     stones_img[i]=pygame.transform.scale(stones_img[i],(40,40))
def stones_display():
     if stones_status["soul"]!="not":
          screen.blit(stones_img["soul"], (stones_X["soul"],stones_Y["soul"]))
     if stones_status["mind"]!="not":
          screen.blit(stones_img["mind"], (stones_X["mind"],stones_Y["mind"]))
     if stones_status["power"]!="not":
          screen.blit(stones_img["power"], (stones_X["power"],stones_Y["power"]))
     if stones_status["time"]!="not":
          screen.blit(stones_img["time"], (stones_X["time"],stones_Y["time"]))
     if stones_status["space"]!="not":
          screen.blit(stones_img["space"], (stones_X["space"],stones_Y["space"]))
     if stones_status["reality"]!="not":
          screen.blit(stones_img["reality"], (stones_X["reality"],stones_Y["reality"]))
stone_trigger_state=2500
def stone_trigger():
     global stones_status,stones_life,stone_trigger_state,stones_X,stones_Y
     a=True
     c=["soul","power","time","reality","mind","space","soul"]
     for i in stones_img.keys():
          if stones_status[i]==-2:
               c.remove(i)
          elif stones_status[i]!=-1:
               a=False
     if c==[]:
          stone_trigger_state=4000
          stones_status={"soul":-1,"power":-1,"space":-1,"time":-1,"reality":-1,"mind":-1}
          stones_life={"soul":200,"power":100,"space":100,"time":100,"reality":100,"mind":100}
          stones_X={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400}
          stones_Y={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150}
     elif a and score>10:
          d=random.choice(c)
          if d=="soul":
               soulstone()
          elif d=="power":
               powerstone()
          elif d=="space":
               spacestone()
          elif d=="time":
               timestone()
          elif d=="reality":
               realitystone()
          elif d=="mind":
               mindstone()
     
                    
def timestone():
     global stones_img,stones_status,bulletY_change,vel,stone_trigger_state
     stones_img["time"]=pygame.image.load("time stone.png")
     stones_img["time"]=pygame.transform.scale(stones_img["time"],(40,40))
     stones_status["time"]=2000
     stone_trigger_state=3000
     vel=vel/2
     bulletY_change=bulletY_change/2
def realitystone():
     global stones_img,stones_status,bulletY_change,bulletimg1,bulletimg,stone_trigger_state,bullet_limit
     stones_img["reality"]=pygame.image.load("reality stone.png")
     stones_img["reality"]=pygame.transform.scale(stones_img["reality"],(40,40))
     stones_status["reality"]=1000
     stone_trigger_state=2000
     bulletimg1=pygame.image.load("bubbles.png")
     bulletimg2=pygame.image.load("bubbles.png")
     bulletimg3=pygame.image.load("bubbles.png")
     bulletimg1=pygame.transform.scale(bulletimg1,(40,40))
     bulletimg2=pygame.transform.scale(bulletimg2,(40,40))
     bulletimg3=pygame.transform.scale(bulletimg3,(40,40))
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
     bulletY_change=1
     bullet_limit=360
def soulstone():
     global stones_img,stones_status,stone_trigger_state,stones_life,stones_X,stones_Y,stones_X2,stones_Y2
     c=[]
     for i in stones_img.keys():
          if stones_status[i]==-2 and i!="soul":
               c.append(i)
     if len(c)>0:
          stones_img["soul"]=pygame.image.load("soul stone.png")
          stones_img["soul"]=pygame.transform.scale(stones_img["soul"],(40,40))
          stones_status["soul"]=500
          d=random.choice(c)
          stones_status[d]=-1
          stones_X[d]=stones_X2[d]
          stones_Y[d]=stones_Y2[d]
          stones_life[d]=100
          stones_life["soul"]=200
          stone_trigger_state=500
def mindstone():
     global stones_img,stones_status,stone_trigger_state,left_limit,right_limit
     stones_img["mind"]=pygame.image.load("mind stone.png")
     stones_img["mind"]=pygame.transform.scale(stones_img["mind"],(40,40))
     stones_status["mind"]=2000
     stone_trigger_state=3000
     screen.blit(laserimg,(400,150))
     if playerX>=400:
          left_limit=424
     elif playerX<400:
          right_limit=350

portal=[pygame.image.load("portal.png"),pygame.image.load("portal.png"),pygame.image.load("portal.png"),pygame.image.load("portal.png")]
def spacestone():
      global stones_img,stones_status,stone_trigger_state
      stones_img["space"]=pygame.image.load("space stone.png")
      stones_img["space"]=pygame.transform.scale(stones_img["space"],(40,40))
      stones_status["space"]=2000
      stone_trigger_state=3000
      for i in range(num_enemy):
          enemyimg[i]=pygame.image.load("ufo.png")
          X_change[i]=4
def teleport():
     global enemyX,enemyY
     a=random.randint(1,200)
     for i in range(num_enemy):
          if a==i:
               if enemyY[i]<=350:
                    enemyX[i]=735-enemyX[i]
                    enemyY[i]=enemyY[i]+40
def powerstone():
      global stones_img,stones_status,stone_trigger_state
      stones_img["power"]=pygame.image.load("power stone.png")
      stones_img["power"]=pygame.transform.scale(stones_img["power"],(40,40))
      stones_status["power"]=2000
      stone_trigger_state=3000
      for i in range(num_enemy):
          enemyimg[i]=pygame.image.load("power_ufo.png")
          X_change[i]=4
power_blast_state=[0,0,0,0,0,0]
def power_shield():
     for i in range(num_enemy):
          for j in range(1,4):
                distance = math.sqrt(((enemyX[i] - bulletX[j])**2) + ((enemyY[i] - bulletY[j])**2))
                if distance < 50:
                     a=random.randint(1,100)
                     if a<20:
                          bulletY[j] = 480
                          bullet_state[j] = "ready"
                          power_blast_state[i] = 80
                          
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
     if power_blast_state[i]>0:
          power_shield_img=pygame.image.load("power_blast.png")
          screen.blit(power_shield_img, (x-30,y-30))
          power_blast_state[i]-=1
          
#bullet (Ready = can't see bulet and Fire = bullet current moving)
bulletimg1 = pygame.image.load("bullet.png")
bulletX=[0,0,0,0]
bulletY =[480,480,480,480]
bulletY_change = 10
bullet_limit=0
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
               save_coins()
          elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_p:
                          run = False
                          pause()
                  elif event.key == pygame.K_q:
                          pygame.quit()
                          save_coins()
                          quit()
                   
     #alternate mechanic and continous method
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and playerX>left_limit :
          playerX -= vel
     if keys[pygame.K_RIGHT] and playerX<right_limit :
          playerX += vel
     if keys[pygame.K_SPACE]:
          if shotgun_state>0:
               if bullet_state==["ready","ready","ready","ready"]:
                    for p in range(1,4):                         
                         if smg_state==0 and (stones_status["reality"]==-1 or stones_status["reality"]==-2):
                              bulletX[p] = playerX
                         elif stones_status["reality"]>0:
                              bulletX[p]=playerX
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
          if power_state[0]>=1 and blast_state==0:
               blast()
     if keys[pygame.K_n] and smg_state==0 and stones_status["reality"]==-1:
          if power_state[2]>=1:
               smg()
     if keys[pygame.K_s] and shotgun_state==0:
          if power_state[1]>=1:
               shotgun()
     if keys[pygame.K_t] and stones_status["time"]==-1:
          timestone()
     if keys[pygame.K_r] and stones_status["reality"]==-1:
          realitystone()
     if keys[pygame.K_m] and stones_status["mind"]==-1:
          mindstone()
     if keys[pygame.K_y] and stones_status["space"]==-1:
          spacestone()
     if keys[pygame.K_u] and stones_status["power"]==-1:
          powerstone()

     #stone trigger
     if stone_trigger_state==0:
          stone_trigger()
     elif stone_trigger_state>0:
          stone_trigger_state-=1
     #blast animation
     if blast_state<=0:
          None
     elif blast_state>0:
          screen.blit(blastimg,(playerX-30,playerY-30))
          blast_state=blast_state-1
          
     #smg timer
     if smg_state>0 :
          smg_state=smg_state-1
     elif smg_state==0 and stones_status["time"]<=0:
          not_smg()
     elif smg_state==0 and stones_status["time"]>0:
          not_smg()
          bulletY_change=5
          
     stones_display()
     #shotgun timer
     if shotgun_state>0:
          shotgun_state=shotgun_state-1
     elif shotgun_state==0:
          bullet_state[2]="ready"
          bullet_state[3]="ready"
          bulletY[2]=480
          bulletY[3]=480

     #life of stones
     for t in stones_X.keys():
          for j in range(1,4):
               collisions = collision (stones_X[t] , stones_Y[t] , bulletX[j] , bulletY[j])
               if collisions and score>25:
                    bulletY[j] = 480
                    bullet_state[j] = "ready"
                    if stones_status[t]==-1:
                         stones_life[t]-=5
                    if stones_life[t]==0:
                         stones_X[t]=-50
                         stones_Y[t]=-50
                         stones_status[t]=-2

     #timestone
     if stones_status["time"]>0:
          stones_status["time"]=stones_status["time"]-1
     elif stones_status["time"]==0:
          stones_img["time"]=pygame.image.load("time stone dead.png")
          stones_img["time"]=pygame.transform.scale(stones_img["time"],(40,40))
          stones_status["time"]=-1
          vel=3
          bulletY_change=10

     #realitystone
     if stones_status["reality"]>0:
          stones_status["reality"]=stones_status["reality"]-1
          bulletimg1=pygame.image.load("bubbles.png")
          bulletimg2=pygame.image.load("bubbles.png")
          bulletimg3=pygame.image.load("bubbles.png")
          bulletimg1=pygame.transform.scale(bulletimg1,(40,40))
          bulletimg2=pygame.transform.scale(bulletimg2,(40,40))
          bulletimg3=pygame.transform.scale(bulletimg3,(40,40))
          bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
          bulletY_change=1
          bullet_limit=360
     elif stones_status["reality"]==0:
          stones_img["reality"]=pygame.image.load("reality stone dead.png")
          stones_img["reality"]=pygame.transform.scale(stones_img["reality"],(40,40))
          stones_status["reality"]=-1
          bulletY_change=10
          bulletimg1=pygame.image.load("bullet.png")
          bulletimg2=pygame.image.load("bullet.png")
          bulletimg3=pygame.image.load("bullet.png")
          bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
          bullet_limit=0

     #soul stone
     if stones_status["soul"]>0:
          stones_status["soul"]-=1
     elif stones_status["soul"]==0:
          stones_status["soul"]=-1
          stones_img["soul"]=pygame.image.load("soul stone dead.png")
          stones_img["soul"]=pygame.transform.scale(stones_img["soul"],(40,40))
          
     #mind stone
     if stones_status["mind"]>0:
          screen.blit(laserimg,(415,128))
          stones_status["mind"]=stones_status["mind"]-1
     elif stones_status["mind"]==0:
          stones_status["mind"]=-1
          stones_img["mind"]=pygame.image.load("mind stone dead.png")
          stones_img["mind"]=pygame.transform.scale(stones_img["mind"],(40,40))
          if playerX>=400:
               left_limit=0
          elif playerX<400:
               right_limit=735

     #space stone
     if stones_status["space"]>0:
          teleport()
          stones_status["space"]-=1
     elif stones_status["space"]==0:
          stones_status["space"]=-1
          stones_img["space"]=pygame.image.load("space stone dead.png")
          stones_img["space"]=pygame.transform.scale(stones_img["space"],(40,40))
          for i in range(num_enemy):
               enemyimg[i]=pygame.image.load("enemy.png")
               X_change[i]=3

     #power stone
     if stones_status["power"]>0:
          power_shield()
          stones_status["power"]-=1
     elif stones_status["power"]==0:
          stones_status["power"]=-1
          stones_img["power"]=pygame.image.load("power stone dead.png")
          stones_img["power"]=pygame.transform.scale(stones_img["power"],(40,40))
          for i in range(num_enemy):
               enemyimg[i]=pygame.image.load("enemy.png")
               X_change[i]=3
     
     # enemy movement
     for i in range(len(enemyX)):
          if enemyY[i] >= 440:
               for j in range (len(enemyX)):
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
               if bulletY[1] <= bullet_limit:
                    bulletY[1] = 480
                    bullet_state[1] = "ready"
          if q==2 and shotgun_state>0:
               if bullet_state[2] is "fire":
                    bulletY[2] -= bulletY_change
                    bulletX[2] -=bulletY_change/2
                    fire(bulletX[2], bulletY[2],bulletimg[2],2)
               if bulletY[2] <= bullet_limit or bulletX[2]<=left_limit:
                    bulletY[2] = 480
                    bullet_state[2] = "ready"
          if q==3 and shotgun_state>0:
               if bullet_state[3] is "fire":
                    bulletY[3] -= bulletY_change
                    bulletX[3] +=bulletY_change/2
                    fire(bulletX[3], bulletY[3],bulletimg[3],3)
               if bulletY[3] <= bullet_limit or bulletX[3]>=right_limit:
                    bulletY[3] = 480
                    bullet_state[3] = "ready"
                    
     # Reward movement
     try:
          for p in range(4):
               if reward_state[p] is "fire":
                    rewardY[p]+=rewardY_change[p]
                    screen.blit(rewardimg[p],(rewardX[p],rewardY[p]))
               if rewardY[p]>=480:
                    rewardY[p]=0
                    reward_state[p]="ready"
     except TypeError:
          pass
                    
     player(playerX)
     show_score()
     show_highscore()
     show_coins()
     pygame.display.update()
     
pygame.quit()


