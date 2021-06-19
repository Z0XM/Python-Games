import pygame
import random
import math
from Assets.Colors import*
from Assets.Z import DisplayText


SnakeHead=[]
Snake=[]
snake_width=25
ScreenWidth=500
ScreenHeight=500
GridWidth=450
GridHeight=450
GridX=25
GridY=25
pygame.init()
screen=pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Z_Snake")
pygame.display.set_icon(pygame.image.load('Assets/Z.ico'))
score_font=pygame.font.SysFont('Comic Sans MS',20)
game_over_font=pygame.font.SysFont('AGENCY FB',40)
play_again_font=pygame.font.SysFont('Comic Sans MS',30)

def PlayArea():
    pygame.draw.rect(screen,Green,(GridX-3+12,GridY-3+12,GridWidth+6-24,GridHeight+6-24),3)

def DisplaySnake():
    pygame.draw.rect(screen,Orange,(SnakeHead[0]+1,SnakeHead[1]+1,snake_width-2,snake_width-2),2)
    for pos in Snake:
        pygame.draw.rect(screen,Cyan,(pos[0]+1,pos[1]+1,snake_width-2,snake_width-2),2)

def Food(x,y):
    pygame.draw.circle(screen,Light(Blue,70),(x,y),int(snake_width/2))

def Collison(move):
    if move=='left' and ([SnakeHead[0]-snake_width,SnakeHead[1]] in Snake or SnakeHead[0]-snake_width<GridX):
        return True
    elif move=='right' and ([SnakeHead[0]+snake_width,SnakeHead[1]] in Snake or SnakeHead[0]+snake_width>GridWidth):
        return True
    elif move=='down' and ([SnakeHead[0],SnakeHead[1]+snake_width] in Snake or SnakeHead[1]+snake_width>GridHeight):
        return True
    elif move=='up' and ([SnakeHead[0],SnakeHead[1]-snake_width] in Snake or SnakeHead[1]-snake_width<GridY):
        return True
    else:return False
    
def new_game():
    global Snake
    global SnakeHead
    score=0
    Snake=[[int(GridX+(GridWidth+snake_width)/2+snake_width),int(GridY+(GridHeight-snake_width)/2)],[int(GridX+(GridWidth+snake_width)/2),int(GridY+(GridHeight-snake_width)/2)]]
    SnakeHead=[int(GridX+(GridWidth-snake_width)/2),int(GridY+(GridHeight-snake_width)/2)]
    move=''
    running=True
    speed=60
    dt=0.3
    food=False
    fx,fy=0,0
    highlight=[]
    highlight_speed=30
    stop_for_once=False
    game_over=False
    check=False
    pause=False
    can_press=True
    key_pressed=False
    while running:
        if not game_over:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    running=False
                if e.type==pygame.KEYDOWN and can_press:
                    can_press=False
                    if e.key==pygame.K_p:pause=not pause
                    if not pause:
                        if e.key in [pygame.K_a,pygame.K_LEFT,pygame.K_d,pygame.K_RIGHT,pygame.K_s,pygame.K_DOWN,pygame.K_w,pygame.K_UP]:
                            key_pressed=True
                        if e.key in [pygame.K_a,pygame.K_LEFT] and move!='right':move='left'
                        elif e.key in [pygame.K_d,pygame.K_RIGHT] and  move!='left' and move:move='right'
                        elif e.key in [pygame.K_s,pygame.K_DOWN] and move!='up':move='down'
                        elif e.key in [pygame.K_w,pygame.K_UP] and move!='down':move='up'
                if e.type==pygame.KEYUP and key_pressed:
                    can_press=True
                    key_pressed=False
            if not pause:
                if move and speed<=60:
                    speed-=dt
                if speed<=0:
                    x=SnakeHead[0]
                    y=SnakeHead[1]
                    if not stop_for_once:
                        Snake.pop(0)
                    stop_for_once=False
                    Snake.append([x,y])
                    if move=='left':SnakeHead=[x-snake_width,y]
                    if move=='right':SnakeHead=[x+snake_width,y]
                    if move=='down':SnakeHead=[x,y+snake_width]
                    if move=='up':SnakeHead=[x,y-snake_width]
                    speed=60
                    if check:game_over=Collison(move)
                    check=Collison(move)
                if not food:
                    while(1):
                        fx=math.floor(random.randrange(GridX+snake_width,GridX+GridWidth)/snake_width)*snake_width
                        fy=math.floor(random.randrange(GridY+snake_width,GridY+GridHeight)/snake_width)*snake_width
                        if [fx-13,fy-13] not in Snake and [fx-13,fy-13]!=SnakeHead:break
                    food=True
                if food and [fx-13,fy-13]==SnakeHead:
                    dt+=0.05
                    food=False
                    Snake.append([0,0])
                    score+=100*(len(highlight)+1)
                    for pos in range(len(Snake)-1):
                        Snake[len(Snake)-pos-1]=Snake[len(Snake)-pos-2]
                    Snake[0]=Snake[1]
                    stop_for_once=True
                    highlight.append(Snake[len(Snake)-1])
                screen.fill(Black)
                DisplaySnake()
                if highlight and highlight_speed<=30:
                    highlight_speed-=dt
                if highlight_speed<=0:
                    for pos in range(len(highlight)):
                        if highlight[pos] in Snake and Snake.index(highlight[pos])!=0:
                            highlight[pos]=Snake[Snake.index(highlight[pos])-1]
                    highlight_speed=30  
                for pos in highlight:
                    if pos in Snake:
                        pygame.draw.rect(screen,Magenta,(pos[0]+1,pos[1]+1,snake_width-2,snake_width-2),2)
                    else:highlight.remove(pos)
                   
                Food(fx,fy)
                PlayArea()
                DisplayText(screen,str(score),Gold, 25, 475, score_font)

            pygame.display.update()
        if game_over:
            DisplayText(screen, 'Game Over', White, 200,200, game_over_font)
            if speed<=60:
                speed-=0.2
            if speed>=30:
                pygame.draw.rect(screen,Black,(50,250,410,100))
            if speed>=0:
                DisplayText(screen, 'Press Any Key To Play Again...', Green, 50,250,play_again_font)
            if speed<=0:
                speed=60
            pygame.display.update()
            pygame.time.wait(2000)
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    running=False
                if e.type==pygame.KEYDOWN:
                    new_game()
                    running=False
            
new_game()
pygame.quit()
