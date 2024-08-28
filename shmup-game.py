import pygame
import sys
import random
import os
from time import sleep

BLACK=(0, 0, 0)
padWidth=1550
padHeight=875
rockImage=[r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock1.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock2.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock3.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock4.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock5.png",
           r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock6.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock7.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock8.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock9.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock10.png",
           r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock11.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock12.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock13.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock14.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock15.png",
           r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock16.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock17.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock18.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock19.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock20.png",
           r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock21.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock22.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock23.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock24.png", r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\rock25.png"]
enemyImage=r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\enemy.png"

def initGame():
    global gamePad, clock, background, fighter, missile, explosion, heart
    pygame.init()
    gamePad=pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption("CO;DE shoot'em up game")
    background=pygame.image.load(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\space.jpg")
    background = pygame.transform.scale(background, (padWidth, padHeight))
    fighter=pygame.image.load(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\fighter.png")
    fighter_width=95
    fighter_height=95
    fighter=pygame.transform.scale(fighter, (fighter_width, fighter_height))
    missile=pygame.image.load(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\missile.png")
    missle_width=50
    missile_height=40
    missile=pygame.transform.scale(missile, (missle_width, missile_height))
    explosion=pygame.image.load(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\explosion.png")
    explosion_width=200
    explosion_height=200
    explosion=pygame.transform.scale(explosion, (explosion_width, explosion_height))
    heart=pygame.image.load(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\heart.png")
    heart_width=80
    heart_height=60
    heart=pygame.transform.scale(heart, (heart_width, heart_height))
    clock=pygame.time.Clock()

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def load_image(image_path, size=None):
    if not os.path.isfile(image_path):
        print(f"Error: File {image_path} does not exist.")
        return None
    
    try:
        image = pygame.image.load(image_path)
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def getRock():
    rock_width=140
    rock_height=140
    image_path=random.choice(rockImage)
    rock=load_image(image_path, (rock_width, rock_height))
    return rock

def getenemy():
    enemy_width=60
    enemy_height=90
    enemy=load_image(enemyImage, (enemy_width, enemy_height))
    return enemy

def load_heart_image():
    heart_image_path = r"C:\Users\user\OneDrive\바탕 화면\shmup-game\image\heart.png"
    heart_width = 100
    heart_height = 289
    return load_image(heart_image_path, (heart_width, heart_height))

def writeScore(count):
    global gamePad
    font=pygame.font.Font(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\DungGeunMo TTF\DungGeunMo.ttf", 30)
    text=font.render("점수: "+str(count), True, (255, 255, 255))
    gamePad.blit(text, (30, 20))

def writeMessage_gameClear(text):
    global gamePad
    textfont=pygame.font.Font(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\DungGeunMo TTF\DungGeunMo.ttf", 80)
    text=textfont.render(text, True, (0, 0, 255))
    textpos=text.get_rect()
    textpos.center=(padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()

def writeMessage_gameOver(text):
    global gamePad
    textfont=pygame.font.Font(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\DungGeunMo TTF\DungGeunMo.ttf", 80)
    text=textfont.render(text, True, (255, 0, 0))
    textpos=text.get_rect()
    textpos.center=(padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()

def restart(text):
    global gamePad
    textfont=pygame.font.Font(r"C:\Users\user\OneDrive\바탕 화면\shmup-game\DungGeunMo TTF\DungGeunMo.ttf", 30)
    text=textfont.render(text, True, (255, 255, 255))
    textpos=text.get_rect()
    textpos.center=(padWidth/2, padHeight/2+60)
    gamePad.blit(text, textpos)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    runGame()
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def gameClear():
    global gamePad
    writeMessage_gameClear("GAME CLEAR!")
    restart("다시 시작하기 (R)")


def gameOver():
    global gamePad
    writeMessage_gameOver("GAME OVER...")
    restart("다시 시작하기 (R)")

def runGame():
    global gamePad, clock, background, fighter, missile, explosion, heart

    missileXY=[]

    lives=5

    fighterSize=fighter.get_rect().size
    fighterWidth=fighterSize[0]
    fighterHeight=fighterSize[1]
    x=padWidth*0.48
    y=padHeight*0.85
    fighterX=0

    rock=getRock()
    rockSize=rock.get_rect().size
    rockWidth=rockSize[0]
    rockHeight=rockSize[1]
    rockX=random.randrange(0, padWidth-rockWidth)
    rockY=0
    rockSpeed=3

    enemy=getenemy()
    enemySize=enemy.get_rect().size
    enemyWidth=enemySize[0]
    enemyHeight=enemySize[1]
    enemyX=random.randrange(0, padWidth-enemyWidth)
    enemyY=0
    enemySpeed=3.5

    isShot=False
    shotCount=0
    rockPassed=0

    onGame=False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_LEFT:
                    fighterX=-5
                elif event.key==pygame.K_RIGHT:
                    fighterX=5

                elif event.key==pygame.K_SPACE:
                    missileX=x+fighterWidth/2
                    missileY=y-fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    fighterX=0

        drawObject(background, 0, 0)

        x+=fighterX
        if x<0:
            x=0
        elif x>padWidth-fighterWidth:
            x=padWidth-fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY)!=0:
            for i, bxy in enumerate(missileXY):
                bxy[1]-=10
                missileXY[i][1]=bxy[1]

                if bxy[1]<rockY:
                    if bxy[0]>rockX and bxy[0]<rockX+rockWidth:
                        missileXY.remove(bxy)
                        isShot=True
                        shotCount+=1

                if bxy[1]<=0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
                
        if len(missileXY)!=0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        writeScore(shotCount)

        rockY+=rockSpeed

        if rockY>padHeight:
            lives-=1
            if lives==0:
                gameOver()
            else:
                rock=getRock()
                rockSize=rock.get_rect().size
                rockWidth=rockSize[0]
                rockHeight=rockSize[1]
                rockX=random.randrange(0, padWidth-rockWidth)
                rockY=0
                  
        enemyY+=enemySpeed

        if enemyY>padHeight:
                enemy=getenemy()
                enemySize=enemy.get_rect().size
                enemyWidth=enemySize[0]
                enemyHeight=enemySize[1]
                enemyX=random.randrange(0, padWidth-enemyWidth)
                enemyY=0

        if isShot:
            drawObject(explosion, rockX, rockY)

            rock=getRock()
            rockSize=rock.get_rect().size
            rockWidth=rockSize[0]
            rockHeight=rockSize[1]
            rockX=random.randrange(0, padWidth-rockWidth)
            rockY=0
            isShot=False

            rockSpeed+=0.07
            if rockSpeed>=10:
                rockSpeed=10

            enemySpeed+=0.07
            if enemySpeed>=10:
                enemySpeed=10

        if y<enemyY+enemyHeight:
            if(enemyX>x and enemyX<fighterWidth) or (enemyX+enemyWidth>x and enemyX+enemyWidth<x+fighterWidth):
                drawObject(explosion, x, y)
                pygame.display.update()
                lives-=1
                if lives==0:
                    gameOver()
                else:
                    enemy=getenemy()
                    enemySize=enemy.get_rect().size
                    enemyWidth=enemySize[0]
                    enemyHeight=enemySize[1]
                    enemyX=random.randrange(0, padWidth-enemyWidth)
                    enemyY=0

        if shotCount==25:
            gameClear()

        for i in range(lives):
            drawObject(heart, 1220+i*60, 10)

        drawObject(rock, rockX, rockY)
        drawObject(enemy, enemyX, enemyY)
        pygame.display.update()

initGame()
runGame()