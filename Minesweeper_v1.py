import pygame
import random
import math
#custom modules
import Assets.Colors as C
from Assets.Z import RectButtons,DisplayText

pygame.init()

#Game Variables
rows=15
cols=10
grid=[[None for x in range(cols)] for y in range(rows)]
flags=[]
mines=[]
total_mines=int((rows*cols)/8)

#Screen
ScreenWidth=300
ScreenHeight=700
CellWidth=25
CellHeight=35
GridWidth=cols*CellWidth
GridHeight=rows*CellHeight
GridX=30
GridY=60

color={1:C.Cyan,2:C.Green,3:C.Magenta,4:C.Blue,5:C.Red,0:C.White}

screen=pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Z_Minesweeper")

icon=pygame.image.load('Assets/Z.ico')
pygame.display.set_icon(icon)

Font=pygame.font.Font('Assets/Minesweeper/PlayAgain.ttf',32)
play_again=RectButtons(C.White,GridX+cols,GridY+GridHeight-8*CellHeight+330,220,50,border=3,text="Play Again",textX=GridX+cols+7,textY=330+GridY+GridHeight-8*CellHeight+12,text_color=C.Yellow,font=Font)
Font=pygame.font.Font('Assets/Minesweeper/numbers.ttf',25)
flag=RectButtons(C.Green,20,10,150,35,border=3,text="FLAGS : "+str(total_mines),textX=GridX-6,textY=6,text_color=C.Blue,font=Font)
clock=RectButtons(C.Green,170,10,110,35,border=3,text='0',textX=GridX+230,textY=6,text_color=C.White,font=Font)
class Cursor:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.clickable=True
        self.locked=False
        
    def display(self):
        pygame.draw.rect(screen,self.color,(self.x*(CellWidth-1)+GridX,self.y*(CellHeight-1)+GridY,CellWidth,CellHeight),3)
        pygame.display.update()
                         
    def get(self):
        X,Y=False,False
        cur=pygame.mouse.get_pos()
        position=[cur[0],cur[1]]
        if position[0]<GridX:position[0]=GridX
        elif position[0]>GridX+GridWidth-3:position[0]=GridX+GridWidth-CellWidth
        else:X=True
        if position[1]<GridY:position[1]=GridY
        elif position[1]>GridY+GridHeight-3:position[1]=GridY+GridHeight-CellHeight
        else:Y=True
        self.x=math.floor((position[0]-GridX)/CellWidth)
        self.y=math.floor((position[1]-GridY)/CellHeight)
        self.display()
        if X and Y:self.clickable=True
        else:self.clickable=False

def DisplayGrid():
    pygame.draw.rect(screen,C.Green,(GridX-10,GridY-10,GridWidth+10,GridHeight+10),3)
    for y in range(rows):
        for x in range(cols):
            if grid[y][x]=='*':
                pygame.draw.rect(screen,C.White,(x*(CellWidth-1)+GridX,y*(CellHeight-1)+GridY,CellWidth,CellHeight),1)
            elif grid[y][x]:
                    font=pygame.font.SysFont(None,30)
                    DisplayText(screen,str(grid[y][x]),color[grid[y][x]],x*(CellWidth-1)+GridX+8,y*(CellHeight-1)+GridY+9,font)

def GenerateMines():
    global mines
    cur=pygame.mouse.get_pos()
    while len(mines)!=total_mines:
        x=random.randrange(cols)
        y=random.randrange(rows)
        if [x,y] not in (mines and [[cur[0],cur[1]]]):mines.append([x,y])

def DisplayMines():
    for pos in mines:
        font=pygame.font.Font('Assets/Minesweeper/numbers.ttf',20)
        DisplayText(screen,"O",C.Blue if [pos[0],pos[1]] in flags else C.Red,pos[0]*(CellWidth-1)+GridX+2,pos[1]*(CellHeight-1)+GridY+2,font)

def DisplayFlags():
    for pos in flags:
        font=pygame.font.Font('Assets/Minesweeper/numbers.ttf',20)
        DisplayText(screen,"F",C.Blue,pos[0]*(CellWidth-1)+GridX+6,pos[1]*(CellHeight-1)+GridY+2,font)

def proxy_calc(x,y):
    count=0
    for pos in mines:
        if (pos[0] in [x-1,x,x+1]) and (pos[1] in [y-1,y,y+1]) and (pos[0]!=x or pos[1]!=y):
            count+=1
    return count
	
def reveal_blank(x,y):
    global grid
    if x in range(cols) and y in range(rows):
        if [x,y] not in mines and grid[y][x]=='*':
            grid[y][x]=proxy_calc(x,y)
            if not grid[y][x]:
                reveal_blank(x-1,y-1)
                reveal_blank(x-1,y)
                reveal_blank(x-1,y+1)
                reveal_blank(x,y-1)
                reveal_blank(x,y+1)
                reveal_blank(x+1,y-1)
                reveal_blank(x+1,y)
                reveal_blank(x+1,y+1)
            if [x,y] in flags:grid[y][x]='*'

def reveal(x,y):
    running=True
    if [x,y] in flags:pass
    elif [x,y] in mines:running=False
    elif grid[y][x]=='*':reveal_blank(x,y)
    return running

def GameOver(status):
    Font=pygame.font.Font('Assets/Minesweeper/numbers.ttf',50)
    DisplayText(screen,str("You "+status),C.Green if status=='Won' else C.Red,GridX-25,330+GridY+GridHeight-10*CellHeight,Font)

def NewGame():
    global grid,flags,mines
    cursor=Cursor(0,0,C.Yellow)
    for y in range(rows):
        for x in range(cols):grid[y][x]='*'
    cursor.get()
    flags.clear()
    mines.clear()
    running=True
    not_clicked=True
    timer=False
    start_time=0
    end=False
    while running and not end:
        screen.fill(C.Black)
        DisplayGrid()
        DisplayFlags()
        flag.create(screen)
        clock.create(screen)
        cursor.display()
        cursor.get()
        if flag.hit():
            flag.change(bg_color=C.White,text_color=C.Light(C.Blue,100))
        else:flag.change(bg_color=C.Green,text_color=C.Blue)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end=True
            if event.type==pygame.MOUSEBUTTONDOWN and not_clicked and cursor.clickable:
                if not timer:
                    timer=True
                    GenerateMines()
                    start_time=pygame.time.get_ticks()
                not_clicked=False
                if event.button==1:
                    running=reveal(cursor.x,cursor.y)
                elif event.button==3:
                    if [cursor.x,cursor.y] in flags:flags.remove([cursor.x,cursor.y])
                    elif grid[cursor.y][cursor.x]=='*' and len(flags)<total_mines:
                        flags.append([cursor.x,cursor.y])
                    Text='FLAGS : '+str(total_mines-len(flags))
                    flag.change(text=Text)
            if event.type==pygame.MOUSEBUTTONUP:
                not_clicked=True
        pygame.display.update()
        vacancy=rows*cols-total_mines
        for y in range(rows):
            for x in range(cols):
                if grid[y][x]!='*' and [x,y] not in mines:vacancy-=1
        if not vacancy:
            running=False
        time=(pygame.time.get_ticks()-start_time-(pygame.time.get_ticks()-start_time)%100)/1000
        clock.change(text=str(time if start_time  else 0),textX=260-len(str(time))*12)
    while not running and not end:
        DisplayGrid()
        DisplayMines()
        if vacancy:GameOver('Lost')
        else:GameOver('Won')
        play_again.create(screen)
        pygame.display.update()
        if play_again.hit():
            play_again.change(bg_color=C.Green,text_color=C.Light(C.Green,150))
            mouse_button=pygame.mouse.get_pressed()
            if mouse_button[0]:
                NewGame()
                running=True
        else:
            play_again.change(bg_color=C.White,text_color=C.Yellow)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=True
                
NewGame()
pygame.display.quit()
pygame.quit()
