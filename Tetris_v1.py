import pygame
import random
import math
#custom modules
from Assets.Z import DisplayText
import Assets.Colors as C

#Game variables
cols=10
rows=20
shapes=[['.X..',
         '.X..',
         '.X..',
         '.X..',],
        ['....',
         '.XX.',
         '.XX.',
         '....',],
        ['....',
         '.X..',
         '.X..',
         '.XX.',],
        ['....',
         '..X.',
         '..X.',
         '.XX.',],
        ['....',
         '.XX.',
         '..XX',
         '....',],
        ['....',
         '.XX.',
         'XX..',
         '....',],
        ['....',
         'XXXX',
         '....',
         '....',],
        ['.X.',
         'XXX',
         '...']]

shape_color=[C.Magenta,C.Yellow,C.Blue,C.Cyan,C.Red,C.Orange,C.Magenta,C.Green]
fallen=[]
fallen_color=[]
#Screen
ScreenWidth=440
ScreenHeight=580
CellWidth=25
CellHeight=25
GridWidth=cols*CellWidth
GridHeight=rows*CellHeight
GridX=25
GridY=25
pygame.init()
screen=pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Z_Tetris")
pygame.display.set_icon(pygame.image.load('Assets/Z.ico'))

class Shape:
    def __init__(self):
        var=random.randrange(len(shapes))
        self.shape=shapes[var]
        self.calc_range()
        self.x=11
        self.y=4
        self.color=shape_color[var]
        self.touchdown=False

    def calc_range(self):
        self.minX=4
        self.maxX=-1
        self.minY=4
        self.maxY=-1
        for line in self.shape:
            if 'X' in line:
                if line.index('X')<self.minX:
                    self.minX=line.index('X')
        for line in self.shape:
            for pos in range(len(line)-1,0,-1):
                if line[pos]=='X' and pos>self.maxX:
                    self.maxX=pos
        for pos in range(len(self.shape)):
            if 'X' in self.shape[pos] and pos<self.minY:
                self.minY=pos
        for pos in range(len(self.shape)-1,0,-1):
            if 'X' in self.shape[pos] and pos>self.maxY:
                self.maxY=pos
    def display(self):
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if self.shape[y][x]=='X':
                    pygame.draw.rect(screen,self.color,(self.x*CellWidth+x*CellWidth+GridX+1,y*CellHeight+GridY+1+CellHeight*self.y,CellWidth-2,CellHeight-2),2)
    def shadow(self):
        Y=self.y
        stop=False
        while not stop :
            var=False
            Y+=1
            if Y+self.maxY>rows-1:
                stop=True
                Y-=1
            for y in range(len(self.shape)):
                for x in range(len(self.shape)):
                    if self.shape[y][x]=='X' and [x+self.x,Y+y] in fallen:
                        Y-=1
                        var=True
            if var:
                something=False
                for y in range(len(self.shape)):
                    for x in range(len(self.shape)):
                        if self.shape[y][x]=='X' and [x+self.x,Y+y]in fallen:
                            something=True
                if not something:stop=True
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if self.shape[y][x]=='X':
                   pygame.draw.rect(screen,C.Light(self.color,50),(self.x*CellWidth+x*CellWidth+GridX+1,y*CellHeight+GridY+CellHeight*(Y)+1,CellWidth-2,CellHeight-2),1)

    def down(self):
        if self.y+self.maxY<rows-1:
            self.y+=1
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if [self.x+x,self.y+y] in fallen and self.shape[y][x]=='X':
                    self.y-=1
                    self.touchdown=True
        if self.y+self.maxY==rows-1:
            self.touchdown=True

    def left(self):
        if self.x+self.minX>0:
            self.x-=1
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if [self.x+x,self.y+y] in fallen and self.shape[y][x]=='X':
                    self.x+=1

    def right(self):
        if self.x+self.maxX<cols-1:
            self.x+=1
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if [self.x+x,self.y+y] in fallen and self.shape[y][x]=='X':
                    self.x-=1

    def rotate(self):
        Y=self.maxY+self.y
        N=len(self.shape[0])
        temp_list=self.shape.copy()
        restore=self.shape.copy()
        for pos in range(N):
            temp_list[pos]=list(temp_list[pos])
        for x in range(0, int(N/2)):
            for y in range(x,N-x-1):
                temp=temp_list[x][y]
                temp_list[x][y]=temp_list[y][N-1-x]
                temp_list[y][N-1-x]=temp_list[N-1-x][N-1-y]
                temp_list[N-1-x][N-1-y]=temp_list[N-1-y][x]
                temp_list[N-1-y][x]=temp
        for y in range(len(temp_list)):
            temp_list[y]=''.join(map(str,temp_list[y]))
        self.shape=temp_list.copy()
        self.calc_range()
        while self.maxY+self.y<Y:
            self.y+=1
        while self.maxY+self.y>rows-1:
            self.y-=1     
        do=False
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if self.shape[y][x]=='X' and [self.x+x,self.y+y] in fallen:
                    do=True
        if self.x+self.minX<0 or self.x+self.maxX>cols-1 or self.y+self.maxY>rows-1 or self.y+self.minY<0 or do:
            self.shape=restore.copy()
            self.calc_range()
        
    def use(self):
        self.x=3
        self.y=-self.minY


def PlayArea():
    pygame.draw.rect(screen,C.Green,(GridX-1,GridY-1,GridWidth+2,GridHeight+2),3)
    for pos in fallen:
        pygame.draw.rect(screen,fallen_color[pos[1]][pos[0]],(pos[0]*CellWidth+GridX+1,GridY+CellHeight*pos[1]+1,CellWidth-2,CellHeight-2))

def FillFallen(S):
    for y in range(len(S.shape)):
        for x in range(len(S.shape)):
            if S.shape[y][x]=='X':
                fallen.append([S.x+x,S.y+y])
                fallen_color[S.y+y][S.x+x]=S.color
def RemoveLine(score):
    rows_in_fallen=[]
    rows_to_remove=[]
    for xy in fallen:
        rows_in_fallen.append(xy[1])
    for y in range(rows):
        if rows_in_fallen.count(y)==cols:
            rows_to_remove.append(y)
    for y in rows_to_remove:
        for x in range(cols):
            fallen.remove([x,y])
    for Y in rows_to_remove:
         for y in range(Y-1,0,-1):
            for x in range(cols):
                if [x,y] in fallen:
                    fallen.remove([x,y])
                    fallen.append([x,y+1])
    return ((len(rows_to_remove)**2)*(100*((len(rows_to_remove)))))//1

def new_game():
    level=1
    fallen.clear()
    global fallen_color
    fallen_color=[[(0,0,0) for x in range(cols)]for y in range(rows)]
    score=0
    score_limit=5000
    current=Shape()
    Next=Shape()
    current.use()
    running=False
    time_limit=30
    t=60
    dt=0.1
    pause=False
    pause_start_time=0
    pause_end_time=0
    color_no=-1
    game_over=False
    randomS=[Shape()]
    randomS[0].x=random.randrange(0,10)
    randomS[0].y=1
    pygame.mixer.music.load('Assets/Tetris/bgm.wav')
    move_gfx=pygame.mixer.Sound('Assets/Tetris/move.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    display_high=0
    welcome_font=pygame.font.SysFont('Comic Sans MS',20)
    any_key_font=pygame.font.SysFont('Comic Sans MS',30)
    score_font=pygame.font.SysFont('Comic Sans MS',40)
    next_font=pygame.font.SysFont('Showcard Gothic',30)
    time_font=pygame.font.SysFont('Copperplate Gothic',30)
    level_font=pygame.font.SysFont('Papyrus',20)
    score_2_font=pygame.font.SysFont('Comic Sans MS',40)
    time_2_font=pygame.font.SysFont('Copperplate Gothic',30)
    while not running and pygame.get_init():
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN and pygame.get_init():
                running=True
        if pygame.get_init():
            screen.fill(C.Black)
            if randomS[len(randomS)-1].y>4:
                randomS.append(Shape())
                randomS[len(randomS)-1].x=random.randrange(0,10)
                randomS[len(randomS)-1].y=1
            if t==60:
                for pos in range(len(randomS)):
                    if not randomS[pos].touchdown:
                        randomS[pos].down()
                t=0
            if t<60:t+=dt
            if t>60:t=60
            for pos in range(len(randomS)):
                randomS[pos].display()
            DisplayText(screen,'Welcome to another version of Tetris',C.White,40,150,welcome_font)
            DisplayText(screen,'Press Any Key To Start...',C.Green,50,250,any_key_font)
            pygame.display.update()
    fallen.clear()
    start_time=pygame.time.get_ticks()
    while running:
        if not game_over:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        pause=not pause
                        if pause:
                            pause_start_time=pygame.time.get_ticks()
                            screen.fill(current.color)
                        if not pause:
                            pause_end_time=pygame.time.get_ticks()
                    if not pause:
                        move_gfx.play()
                        if event.key in [pygame.K_a,pygame.K_LEFT]:
                            current.left()
                        if event.key in [pygame.K_d,pygame.K_RIGHT]:
                            current.right()
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            current.rotate()
                        if event.key in [pygame.K_a,pygame.K_LEFT,pygame.K_d,pygame.K_RIGHT,pygame.K_SPACE]:
                            if current.y+current.maxY!=rows-1:
                                current.touchdown=False
                            for x in range(len(current.shape)):
                                if [current.x+x,current.y+current.maxY] in fallen and current.shape[current.maxY][x]=='X':
                                    current.touchdown=True
                        if event.key in [pygame.K_s,pygame.K_DOWN] and not current.touchdown:
                            current.down()
                        if event.key==pygame.K_SPACE:
                            if current.touchdown:
                                FillFallen(current)
                                score+=RemoveLine(score)
                                current=Next
                                current.use()
                                for y in range(len(current.shape)):
                                    for x in range(len(current.shape)):
                                        if current.shape[y][x]=='X' and [current.x+x,current.y+y] in fallen:
                                            game_over=True
                                Next=Shape()
                            else:
                                while not current.touchdown:
                                    current.down()
                        
            if not pause:
                screen.fill(C.Black)
                PlayArea()
                if score>score_limit:
                    level+=1
                    score_limit+=level*5000
                    dt+=0.1
                if t==60:
                    current.down()
                    t=0
                if t<60:t+=dt
                if t>60:t=60
                if current.touchdown:
                    time_limit-=0.1
                if time_limit<0:time_limit=0
                if time_limit==0:
                    FillFallen(current)
                    score+=RemoveLine(score)
                    current.touchdown=False
                    current=Next
                    current.use()
                    for y in range(len(current.shape)):
                        for x in range(len(current.shape)):
                            if current.shape[y][x]=='X' and [current.x+x,current.y+y] in fallen:
                                game_over=True
                    Next=Shape()
                    time_limit=30
                current.display()
                if not game_over:current.shadow()
                
                DisplayText(screen,str(level),C.White,1,1,level_font)
                pygame.draw.rect(screen,C.Gold,(11*CellWidth+GridX-10,3*CellHeight+GridY-10,5*CellWidth,5*CellHeight+10),2)
                DisplayText(screen,'NEXT',C.White,11*CellWidth+GridX+18,3*CellHeight+GridY,next_font)
                Next.display()
                time=pygame.time.get_ticks()-start_time-pause_end_time+pause_start_time
                time=(time-(time)%100)/1000
                DisplayText(screen,str(time),C.Gold,11*CellWidth+GridX,CellHeight+GridY+10,time_font)
                DisplayText(screen,str(score),C.Green,11*CellWidth+GridX-8,7*CellHeight+GridY+15,score_font)
        if game_over:
            screen.fill(C.Black)
            DisplayText(screen,str(time),C.White,11*CellWidth+GridX,CellHeight+GridY+10,time_2_font)
            DisplayText(screen,str(score),C.Green if display_high!=2 else C.Red,11*CellWidth+GridX-8,7*CellHeight+GridY+15,score_2_font)
            if display_high:
                DisplayText(screen,str(high_score),C.Green if display_high==2 else C.Red,11*CellWidth+GridX-8,9*CellHeight+GridY+15,score_2_font)
            end=False
            for c in fallen:
                if not end:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            running=False
                            end=True
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_h:
                                file=open('Assets/Tetris/high_score.txt','r')
                                high_score=int(file.read())
                                display_high=1
                                if high_score>score:display_high=2
                                DisplayText(screen,str(high_score),C.Green if display_high==2 else C.Red,11*CellWidth+GridX-8,9*CellHeight+GridY+15,score_2_font)
                                file.close()
                            else:
                                game_over=False
                                screen.fill(C.Black)
                                file=open('Assets/Tetris/high_score.txt','r')
                                high_score=int(file.read())
                                file.close()
                                if score>high_score:
                                    file=open('Assets/Tetris/high_score.txt','w')
                                    file.write(str(score))
                                    file.close()
                                new_game()
                                running=False
                    while True:
                        color=random.choice(C.color_list)
                        if color!=C.Black:break
                    pygame.draw.rect(screen,color,(c[0]*CellWidth+GridX+1,GridY+CellHeight*c[1]+1,CellWidth-2,CellHeight-2))
                    pygame.display.update()
                    pygame.time.delay(100)           
        pygame.display.update()
new_game()
pygame.display.quit()
pygame.quit()
