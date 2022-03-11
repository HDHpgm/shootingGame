import pygame
import random
from pygame.locals import *
import math
from time import sleep
#전역변수
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
white=(255,255,255)
red=(255,0,0)
screen_width=1024
screen_height=512
charx=screen_width*0.03
chary=screen_height*0.4
weapons=[] # 무기 각도
twpos=[[screen_width,random.randrange(0,screen_height-90)]] #타노스 공격위치
timer1=100;timer2=0;timer3=100;timer4=0
badtanos=[[screen_width,random.randrange(0,screen_height-90)]]  #맨처음 타노스 나오는 위치
died=False
charset=1  #처음시작 아이언맨
backx=0;backy=0
hit=False
score=0
stage=1
healthv=300
menu=True
stat=0
time=0
#이미지
iron=pygame.image.load('image/ironman.png')
iron1=pygame.image.load('image/ironman1.png')
iron2=pygame.image.load('image/ironman2.png')
captain=pygame.image.load('image/captain.png')
captain1=pygame.image.load('image/captain1.png')
captain2=pygame.image.load('image/captain2.png')
blackp=pygame.image.load('image/black.png')
blackp1=pygame.image.load('image/black1.png')
blackp2=pygame.image.load('image/black2.png')
tanosimg=pygame.image.load("image/tanos.png")
tanosweapon=pygame.image.load('image/tanosweapon.png')
tanossize=tanosimg.get_rect().size
charsize=iron.get_rect().size
twrect=pygame.Rect(tanosweapon.get_rect())
background1=pygame.image.load('image/backg.png')
gamebackground1=pygame.image.load('image/1rspace.jpg')
gamebackground2=pygame.image.load('image/1rspace.jpg')
gamebackground3=pygame.image.load('image/2rspace.jpg')
gamebackground4=pygame.image.load('image/2rspace.jpg')
gamebackground5=pygame.image.load('image/3rspace.jpg')
gamebackground6=pygame.image.load('image/3rspace.jpg')
ironweapon=pygame.image.load('image/ironweapon.png')
captainweapon=pygame.image.load('image/captainweapon.png')
blackweapon=pygame.image.load('image/blackweapon.png')
healthbar=pygame.image.load('image/healthbar.png')
health=pygame.image.load('image/health.png')
hitepect=pygame.image.load('image/hitepec.png')
helpimg=pygame.image.load('image/helpmenu.png')
ironmv=[iron,iron1,iron2]
captainmv=[captain,captain1,captain2]
blackpmv=[blackp,blackp1,blackp2]
#소리
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.mixer.music.load("sound/endgameost.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.3)
ironmansound=pygame.mixer.Sound("sound/iloveyou3000.wav")
ironmansound.set_volume(1)
ironmanbim=pygame.mixer.Sound("sound/bim.wav")
ironmanbim.set_volume(1)
blackpsound=pygame.mixer.Sound("sound/forever.wav")
blackpsound.set_volume(1)
captainsound=pygame.mixer.Sound("sound/avengersasemble.wav")
captainsound.set_volume(1)
captainshield=pygame.mixer.Sound("sound/shield.wav")
captainshield.set_volume(1)
boomsound=pygame.mixer.Sound("sound/boomsound.wav")
boomsound.set_volume(1)
#함수, 클래스
class avengers: #캐릭터 3가지의 슈퍼클래스
    global screen,iron
    img=None
    weapon=None
    def __init__(self):
        self.img=ironmv[0]
        self.weapon=ironweapon
    def screenset(self,x,y):
        pass
class ironman(avengers):
    
    def __init__(self):
        super().__init__()
    def screenset(self,x,y):
        global stat,time,charx,chary
        if stat:
            if self.img==ironmv[0]:
                self.img=ironmv[1]
            if stat==1 and time>7:
                if self.img==ironmv[1]:
                    self.img=ironmv[2]
                stat=2
                time=0
            elif stat==2 and time>7:
                if self.img==ironmv[2]:
                    self.img=ironmv[1]
                stat=3
                time=0
            elif stat==3 and time>7:
                if self.img==ironmv[1]:
                    self.img=ironmv[0]
                stat=0
                time=0
        playerpos=[charx,chary]
        position=pygame.mouse.get_pos()
        angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
        playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot,playerpos1)
        
class captainamerica(avengers):
    def __init__(self):
        self.img=captain
        self.weapon=captainweapon
    def screenset(self,x,y):
        global stat,time,charx,chary
        if stat:
            if self.img==captainmv[0]:
                self.img=captainmv[1]
            if stat==1 and time>7:
                if self.img==captainmv[1]:
                    self.img=captainmv[2]
                stat=2
                time=0
            elif stat==2 and time>7:
                if self.img==captainmv[2]:
                    self.img=captainmv[1]
                stat=3
                time=0
            elif stat==3 and time>7:
                if self.img==captainmv[1]:
                    self.img=captainmv[0]
                stat=0
                time=0
        playerpos=[charx,chary]
        position=pygame.mouse.get_pos()
        angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
        playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot,playerpos1)
        
class blackpanther(avengers):
    def __init__(self):
        self.img=blackp
        self.weapon=blackweapon
    def screenset(self,x,y):
        global stat,time,charx,chary
        if stat:
            if self.img==blackpmv[0]:
                self.img=blackpmv[1]
            if stat==1 and time>7:
                if self.img==blackpmv[1]:
                    self.img=blackpmv[2]
                stat=2
                time=0
            elif stat==2 and time>7:
                if self.img==blackpmv[2]:
                    self.img=blackpmv[1]
                stat=3
                time=0
            elif stat==3 and time>7:
                if self.img==blackpmv[1]:
                    self.img=blackpmv[0]
                stat=0
                time=0
        playerpos=[charx,chary]
        position=pygame.mouse.get_pos()
        angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
        playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
        playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
        screen.blit(playerrot,playerpos1)
        
def tanos(tanosspeed,timerminus):
    global timer1,timer2,badtanos,score,weapons,healthv,hit,died
    num=0
    tanosimgcopy=tanosimg.copy()
    if timer1==0:
        badtanos.append([screen_width,random.randrange(0,screen_height-90)])
        timer1=100-(timer2)
        if timer2>=35:
            timer2=35
        else:
            timer2+=15
    index=0
    for tanos in badtanos: #타노스 화면에 뿌려주기

        tanos[0]-=tanosspeed
        tanosrect=pygame.Rect(tanosimg.get_rect())
        tanosrect.top=tanos[1]
        tanosrect.left=tanos[0]
        if tanosrect.left<10:
            healthv-=40 #타노스가 화면 끝까지 오면/ 타노스를 놓치면 체력감소
            badtanos.pop(index)
            if healthv<=0:
                died=True
        index1=0
        # 무기와 타노스가 맞닿는지 체크해 닿으면 점수 1 추가 
        for wp in weapons:
            wprect=pygame.Rect(change.weapon.get_rect()) #무기 rect화
            wprect.left=wp[1]
            wprect.top=wp[2]
            if tanosrect.colliderect(wprect): #두개의 rect가 닿으면, (캐릭터가 날린 무기와 타노스가 닿으면)
                hit=True    
                score+=1
                hitxy=badtanos.pop(index)
                weapons.pop(index1)
            else:
                pass
            if hit==True:
                boomsound.play()
                screen.blit(hitepect,(hitxy[0],hitxy[1]))
                hit=False
            index1+=1
        index+=1    
    for tanos in badtanos:
        screen.blit(tanosimg,tanos)
    timer1-=timerminus

       
def backgr(x,y,background): #배경 넣어주기
    global screen
    screen.blit(background,(x,y))
    
def text_format(message, textFont, textSize, textColor): #텍스트 변환
    newFont=pygame.font.Font(textFont,textSize)
    newText=newFont.render(message,0,textColor)
    return newText

def gameover(): # 게임오버 시 화면
    global screen,stage,score,healthv,died
    while died:
        largetext=text_format("게임오버네요ㅠㅠ",'font/DX.ttf',35,red)
        submessage=text_format("다시시작 : 'r'  종료 : 'x'",'font/DX.ttf',20,white)
        screen=pygame.display.set_mode((screen_width,screen_height))
        screen.fill(black)
        screen.blit(iron,(screen_width/2/2-100,screen_height/2/2-50))
        screen.blit(captain,(screen_width/2/2,screen_height/2/2-50))
        screen.blit(blackp,(screen_width/2/2+100,screen_height/2/2-50))
        screen.blit(largetext,(screen_width/2/2+100,screen_height/2/2+100))
        screen.blit(submessage,(screen_width/2/2+100,screen_height/2/2+150))
        pygame.display.update()
        clock.tick(60)
        pygame.event.clear()
        
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_r:
                stage=1
                healthv=300
                score=0
                died=False
                round1()
            elif event.key==K_x:
                pygame.quit()
                quit()
    
def largemessage(message,message1): #스테이지 클리어 후 나오는 화면
    global screen,stage,score,healthv
    while True:
        largetext=text_format(message,'font/DX.ttf',35,white)
        screen=pygame.display.set_mode((screen_width,screen_height))
        screen.fill(black)
        screen.blit(iron,(screen_width/2/2-100,screen_height/2/2-50))
        screen.blit(captain,(screen_width/2/2,screen_height/2/2-50))
        screen.blit(blackp,(screen_width/2/2+100,screen_height/2/2-50))
        screen.blit(largetext,(screen_width/2/2+100,screen_height/2/2+100))
        submessage=text_format(message1,'font/DX.ttf',20,white)
        screen.blit(submessage,(screen_width/2/2+100,screen_height/2/2+150))
        pygame.display.update()
        clock.tick(60)
        if stage==1:
             # 각 라운드마다 5초 설명화면 띄우고 3라운드 클리어하면 리플레이 묻는창  띄움
            healthv=300
            score=0
            stage=2
            sleep(5)
            round2()
        elif stage==2:
            healthv=300
            score=0
            stage=3
            sleep(5)
            round3()
        elif stage==3: #스테이지 3클리어면 재시작,종료 화면 띄움
            pygame.event.clear()
            event=pygame.event.wait()
            if event.type==KEYDOWN:
                if event.key==K_r:
                    stage=1
                    healthv=300
                    score=0
                    round1()
                elif event.key==K_x:
                    pygame.quit()
                    quit()
                elif event.key==K_s:
                    stage=1
                    healthv=300
                    score=0
                    main_menu()
def helpscreen(): #메뉴에서 도움말 선택시 나타나는 화면
    global screen,menu
    while True:
        screen=pygame.display.set_mode((screen_width,screen_height))
        screen.blit(helpimg,(0,0))
        re_text=text_format("뒤로가기 : 'r'","font/DX.ttf",30,black)
        screen.blit(re_text,(620,100))
        pygame.display.update()
        clock.tick(60)
        pygame.event.clear()
        event=pygame.event.wait()
        if event.type==KEYDOWN:
            if event.key==K_r:
                menu=True
                main_menu()
        
def xycheck(): #지정된 곳 안에서 움직이기 x축은 화면의 체력바 전까지 움직이게하고 y축은 height 비슷하게
    global charx,chary
    if charx<0+charsize[0]/2:
        charx=0+charsize[0]/2
    elif charx>screen_width/6:
        charx=screen_width/6            
    if chary<0+charsize[1]/2:
        chary=0+charsize[1]/2
    elif chary>screen_height-charsize[1]:
        chary=screen_height-charsize[1]

def tanosatt(): #타노스가 무기를 날림 
    global change,healthv,charx,chary,timer3,timer4,died,playerpos1
    if timer3==0:
        twpos.append([screen_width,random.randrange(0,screen_height-90)])
        timer3=100-(timer4)
        if timer4>=35:
            timer4=35
        else:
            timer4+=5
    index2=0
    for tweapon in twpos:
        tweapon[0]-=25 #속도 25 / 타노스보다 빠르게
        twrect.top=tweapon[1]
        twrect.left=tweapon[0]
        changerect=pygame.Rect(change.img.get_rect())
        changerect.top=chary
        changerect.left=charx
        if twrect.colliderect(changerect): #두개의 rect가 닿으면, (타노스무기가 캐릭터와 닿으면)
            healthv-=30 #체력 감소
            twpos.pop(index2)
            if healthv<=0:
                died=True
        index2+=1
    for tweapon in twpos:
        screen.blit(tanosweapon,(tweapon[0],tweapon[1]))
    timer3-=1
    
def round1():
        global charx,chary,died,charset,score,stage,change,died,healthv,playerpos1,stat,time,badtanos
        ychange=0
        xchange=0
        badtanos=[[screen_width,random.randrange(0,screen_height-90)]] 
        gback1x=0;gback2x=screen_width
        while not died:
            time+=stat
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    stat=1
                    position=pygame.mouse.get_pos() # 마우스 좌표읽음
                    playerpos=[charx,chary]
                    position=pygame.mouse.get_pos()
                    angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
                    playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
                    playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
                    weapons.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
                    if charset==1:
                        ironmanbim.play()
                    elif charset==2 or charset==3:
                        captainshield.play()

                        
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        ychange=-5
                    elif event.key==pygame.K_a:
                        xchange=-5
                    elif event.key==pygame.K_s:
                        ychange=5
                    elif event.key==pygame.K_d:
                        xchange=5
                    elif event.key==pygame.K_1: # 캐릭터 변경기능 구현 #
                        if charset==1:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=ironman()
                            change.screenset(charx,chary)
                            ironmansound.play()
                            charset=1
                    elif event.key==pygame.K_2: # 캐릭터 변경기능 구현 #
                        if charset==2:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=captainamerica()
                            change.screenset(charx,chary)
                            captainsound.play()
                            charset=2
                    elif event.key==pygame.K_3: # 캐릭터 변경기능 구현 #
                        if charset==3:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=blackpanther()
                            change.screenset(charx,chary)
                            blackpsound.play()
                            charset=3
                            
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_w or event.key==pygame.K_s:
                        ychange=0
                    if event.key==pygame.K_a or event.key==pygame.K_d:
                        xchange=0
            
            chary=chary+ychange
            charx=charx+xchange
            xycheck() # 지정된곳 안에서 움직이기 함수 
            screen.fill(white)
            gback1x-=2
            gback2x-=2
            if gback1x==-screen_width:  # 배경 계속 이어서 날아다니는 것처럼
                gback1x=0
                gback2x=screen_width
            backgr(gback1x,0,gamebackground1)
            backgr(gback2x,0,gamebackground2)
            # 삼각함수 응용해 각도조절하며 무기 발사하기
 #돌려진 이미지 좌표
            change.screenset(charx,chary)
            for bullet in weapons:
                index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<0 or bullet[1]>1024 or bullet[2]<0 or bullet[2]>512: #화면 밖 나가면 없앰
                    weapons.pop(index)
                index+=1
                for projectile in weapons:
                    weapon1=pygame.transform.rotate(change.weapon,360-projectile[0]*40.00) # 돌려진 무기 이미지
                    screen.blit(weapon1,(projectile[1],projectile[2]))
            
            #점수랑 스테이지 띄우기
            text_score=text_format("점수:"+str(score),"font/DX.ttf",30,white)
            screen.blit(text_score,(10,screen_height-43))
            text_stage=text_format("스테이지:"+str(stage),"font/DX.ttf",30,white)
            screen.blit(text_stage,(150,screen_height-43))
            text_help=text_format("교체기능 - 1:아이언맨 2:캡틴아메리카 3:블랙팬서","font/DX.ttf",20,white)
            screen.blit(text_help,(320,screen_height-30))
            tanos(6,1)
            screen.blit(healthbar,(5,5))
            for heal in range(0,healthv):
                screen.blit(health,(heal+8,8))
            pygame.display.update()
            clock.tick(60)
            if(score>=5):
                del(badtanos)
                largemessage("스테이지1 클리어! 5초후 2라운드 시작","2라운드에는 타노스가 2배로 빨라집니다.  클리어조건:20마리 잡기")
            if died==True:
                break
        del(badtanos)
        gameover()

def round2():
        global charx,chary,died,charset,score,stage,change,died,healthv,playerpos1,stat,time,badtanos
        badtanos=[[screen_width,random.randrange(0,screen_height-100)]]
        ychange=0
        xchange=0
        gback1x=0;gback2x=screen_width
        while not died:
            time+=stat
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    stat=1
                    position=pygame.mouse.get_pos() # 마우스 좌표읽음
                    playerpos=[charx,chary]
                    position=pygame.mouse.get_pos()
                    angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
                    playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
                    playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
                    weapons.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
                    if charset==1:
                        ironmanbim.play()
                    elif charset==2 or charset==3:
                        captainshield.play()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        ychange=-5
                    elif event.key==pygame.K_a:
                        xchange=-5
                    elif event.key==pygame.K_s:
                        ychange=5
                    elif event.key==pygame.K_d:
                        xchange=5
                    elif event.key==pygame.K_1: # 캐릭터 변경기능 구현 #
                        if charset==1:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=ironman()
                            change.screenset(charx,chary)
                            ironmansound.play()
                            charset=1
                    elif event.key==pygame.K_2: # 캐릭터 변경기능 구현 #
                        if charset==2:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=captainamerica()
                            change.screenset(charx,chary)
                            captainsound.play()
                            charset=2
                    elif event.key==pygame.K_3: # 캐릭터 변경기능 구현 #
                        if charset==3:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=blackpanther()
                            change.screenset(charx,chary)
                            blackpsound.play()
                            charset=3
                            
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_w or event.key==pygame.K_s:
                        ychange=0
                    if event.key==pygame.K_a or event.key==pygame.K_d:
                        xchange=0
            
            chary=chary+ychange
            charx=charx+xchange
            xycheck() # 지정된곳 안에서 움직이기 함수 
            screen.fill(white)
            gback1x-=2
            gback2x-=2
            if gback1x==-screen_width:  # 배경 계속 이어서 날아다니는 것처럼
                gback1x=0
                gback2x=screen_width
            backgr(gback1x,0,gamebackground1)
            backgr(gback2x,0,gamebackground2)
            # 삼각함수 응용해 각도조절하며 무기 발사하기
 #돌려진 이미지 좌표
            change.screenset(charx,chary)
            for bullet in weapons:
                index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<0 or bullet[1]>1024 or bullet[2]<0 or bullet[2]>512: #화면 밖 나가면 없앰
                    weapons.pop(index)
                index+=1
                for projectile in weapons:
                    weapon1=pygame.transform.rotate(change.weapon,360-projectile[0]*40.00) # 돌려진 무기 이미지
                    screen.blit(weapon1,(projectile[1],projectile[2]))
            
            #점수랑 스테이지 띄우기
            text_score=text_format("점수:"+str(score),"font/DX.ttf",30,white)
            screen.blit(text_score,(10,screen_height-43))
            text_stage=text_format("스테이지:"+str(stage),"font/DX.ttf",30,white)
            screen.blit(text_stage,(150,screen_height-43))
            text_help=text_format("교체기능 - 1:아이언맨 2:캡틴아메리카 3:블랙팬서","font/DX.ttf",20,white)
            screen.blit(text_help,(320,screen_height-30))
            tanos(13,1)
            screen.blit(healthbar,(5,5))
            for heal in range(0,healthv):
                screen.blit(health,(heal+8,8))
            pygame.display.update()
            clock.tick(60)
            if(score>=5):
                del(badtanos)
                largemessage("스테이지2 클리어! 5초후 3라운드 시작","3라운드에는 타노스가 검을 날립니다.  클리어조건: 20마리잡기")
            if died==True:
                break
        del(badtanos)
        gameover()

def round3():
        global charx,chary,died,charset,score,stage,change,died,healthv,playerpos1,stat,time,badtanos
        ychange=0
        xchange=0
        badtanos=[[screen_width,random.randrange(0,screen_height-70)]]
        gback1x=0;gback2x=screen_width
        while not died:
            time+=stat
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    stat=1
                    position=pygame.mouse.get_pos() # 마우스 좌표읽음
                    playerpos=[charx,chary]
                    position=pygame.mouse.get_pos()
                    angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
                    playerrot=pygame.transform.rotate(change.img,360-angle*10) # 캐릭터 이미지를 돌려 저장
                    playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
                    weapons.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
                    if charset==1:
                        ironmanbim.play()
                    elif charset==2 or charset==3:
                        captainshield.play()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        ychange=-5
                    elif event.key==pygame.K_a:
                        xchange=-5
                    elif event.key==pygame.K_s:
                        ychange=5
                    elif event.key==pygame.K_d:
                        xchange=5
                    elif event.key==pygame.K_1: # 캐릭터 변경기능 구현 #
                        if charset==1:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=ironman()
                            change.screenset(charx,chary)
                            ironmansound.play()
                            charset=1
                    elif event.key==pygame.K_2: # 캐릭터 변경기능 구현 #
                        if charset==2:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            
                            change=captainamerica()
                            change.screenset(charx,chary)
                            captainsound.play()
                            charset=2
                    elif event.key==pygame.K_3: # 캐릭터 변경기능 구현 #
                        if charset==3:
                            pass
                        else:
                            charx=screen_width*0.03
                            chary=screen_height*0.4
                            change=blackpanther()
                            change.screenset(charx,chary)
                            blackpsound.play()
                            charset=3
                            
                elif event.type==pygame.KEYUP:
                    if event.key==pygame.K_w or event.key==pygame.K_s:
                        ychange=0
                    if event.key==pygame.K_a or event.key==pygame.K_d:
                        xchange=0
            
            chary=chary+ychange
            charx=charx+xchange
            xycheck() # 지정된곳 안에서 움직이기 함수 
            screen.fill(white)
            gback1x-=2
            gback2x-=2
            if gback1x==-screen_width:  # 배경 계속 이어서 날아다니는 것처럼
                gback1x=0
                gback2x=screen_width
            backgr(gback1x,0,gamebackground1)
            backgr(gback2x,0,gamebackground2)
            # 삼각함수 응용해 각도조절하며 무기 발사하기
 #돌려진 이미지 좌표
            change.screenset(charx,chary)
            for bullet in weapons:
                index=0
                velx=math.cos(bullet[0])*10
                vely=math.sin(bullet[0])*10
                bullet[1]+=velx
                bullet[2]+=vely
                if bullet[1]<0 or bullet[1]>1024 or bullet[2]<0 or bullet[2]>512: #화면 밖 나가면 없앰
                    weapons.pop(index)
                index+=1
                for projectile in weapons:
                    weapon1=pygame.transform.rotate(change.weapon,360-projectile[0]*40.00) # 돌려진 무기 이미지
                    screen.blit(weapon1,(projectile[1],projectile[2]))
            
            #점수랑 스테이지 띄우기
            text_score=text_format("점수:"+str(score),"font/DX.ttf",30,white)
            screen.blit(text_score,(10,screen_height-43))
            text_stage=text_format("스테이지:"+str(stage),"font/DX.ttf",30,white)
            screen.blit(text_stage,(150,screen_height-43))
            text_help=text_format("교체기능 - 1:아이언맨 2:캡틴아메리카 3:블랙팬서","font/DX.ttf",20,white)
            screen.blit(text_help,(320,screen_height-30))
            tanos(13,1)
            tanosatt() #타노스 무기 날리기
            screen.blit(healthbar,(5,5))
            for heal in range(0,healthv):
                screen.blit(health,(heal+8,8))
            pygame.display.update()
            clock.tick(60)
            if(score>=10):
                break
            if died==True:
                break
        if died==True:
            del(badtanos)
            gameover()
        else:
            largemessage("스테이지3 클리어!","다시시작 : 'r'  종료 : 'x' 메인화면 : 's'")
def main_menu(): #초기화면
    global backx,backy,background1,menu
    selected="게임시작"
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and selected=="나가기":
                    selected="도움말"
                elif event.key==pygame.K_UP and selected=="도움말":
                    selected="게임시작"
                elif event.key==pygame.K_DOWN and selected=="게임시작":
                    selected="도움말"
                elif event.key==pygame.K_DOWN and selected=="도움말":
                    selected="나가기"
                if event.key==pygame.K_RETURN:
                    if selected=="게임시작":
                        round1()
                    elif selected=="도움말":
                        menu=False
                    elif selected=="나가기":
                        pygame.quit()
                        quit()
        screen.fill(white)
        backgr(backx,backy,background1)
        if selected=="게임시작":
            text_start=text_format("게임시작","font/DX.ttf",60,white)
        else:
            text_start = text_format("게임시작","font/DX.ttf",60,black)
            
        if selected=="도움말":
            text_helpm=text_format("도움말","font/DX.ttf",60,white)
        else:
            text_helpm=text_format("도움말","font/DX.ttf",60,black)
            
        if selected=="나가기":
            text_quit=text_format("나가기","font/DX.ttf",60,white)
        else:
            text_quit = text_format("나가기","font/DX.ttf",60,black)
            
        text_title=text_format("Avengers:Endgame","font/hanspunch.ttf",150,black)
        start_rect=text_start.get_rect()
        helpm_rect=text_helpm.get_rect()
        quit_rect=text_quit.get_rect()
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_helpm, (screen_width/2 - (helpm_rect[2]/2), 360))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 420))
        screen.blit(text_title,(80,50))
        pygame.display.update()
        clock.tick(60)
    helpscreen()
#메인

pygame.display.set_caption('Avengers:Endgame')
clock=pygame.time.Clock()
change=ironman()
while not died:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            died=True
    main_menu()
pygame.quit()
