import pygame as pygame
import random
from Assets.Colors import*
from Assets.Z import RectButtons

pygame.init()

play=[]
turn=0

Cell=45
GridX=30
GridY=30
ScreenWidth=225
ScreenHeight=225
screen=pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption('Z_XnO')
pygame.display.set_icon(pygame.image.load('Assets/Z.ico'))
main_font=pygame.font.SysFont('Berlin Sans FB',30)
game_over_font=pygame.font.SysFont('AGENCY FB',40)

class Cursor:
    def __init__(self):
        self.x=0
        self.y=0
    
    def notValid(self):
        if self.x<0 or self.x>2 or self.y<0 or self.y>2:
            return True
        else: return False

    def display(self):
        pygame.draw.rect(screen,Green,(self.x*(Cell)+GridX-2,self.y*(Cell)+GridY+3,Cell,Cell),4)
    
def Display():
    pygame.draw.line(screen,White,(GridX+Cell-2,GridY+3),(GridX+Cell-2,GridY+3*Cell+3),3)
    pygame.draw.line(screen,White,(GridX+2*Cell-2,GridY+3),(GridX+2*Cell-2,GridY+3*Cell+3),3)
    pygame.draw.line(screen,White,(GridX-2,GridY+Cell+3),(GridX+3*Cell-2,GridY+Cell+3),3)
    pygame.draw.line(screen,White,(GridX-2,GridY+2*Cell+3),(GridX+3*Cell-2,GridY+2*Cell+3),3)
    for pos in range(9):
        if play[pos]=='X':color=Cyan
        elif play[pos]=='O':color=Orange
        if play[pos]:
            text=main_font.render(str(play[pos]),1,color)
            screen.blit(text,((pos%3)*(Cell-20)+GridX+10*(2*(pos%3)+1),(pos//3)*(Cell-20)+GridY+10*(2*(pos//3)+1)))

def random_move():
    available_pos=[]
    for pos in range(9):
        if not play[pos]:available_pos.append(pos)
    position=random.choice(available_pos)
    play[position]='O'

def win_lose_check(player):
    for var in range(3):
        if play[3*var]==play[3*var+1] and play[3*var]==play[3*var+2] and play[3*var]==player:return True
        elif play[var]==play[var+3] and play[var]==play[var+6] and play[var]==player:return True
    for var in [0,2]:
        if play[var]==play[4] and play[4]==play[8-var] and play[var]==player:return True

def check_row(row,player):
    var=None
    if play[row[0]]==play[row[1]] and play[row[0]]==player:var=row[2]
    elif play[row[0]]==play[row[2]] and play[row[0]]==player:var=row[1]
    elif play[row[1]]==play[row[2]] and play[row[2]]==player:var=row[0]
    if var!=None and not play[var]:return var
    else: return None
    
def make_stop_win(what_to_do):
    if what_to_do=='make':
        player='O'
    elif what_to_do=='stop':
        player='X'
    for var in range(3):
        position=check_row([3*var,3*var+1,3*var+2],player)
        if position!=None:break
        position=check_row([var,var+3,var+6],player)
        if position!=None:break
    if position==None:
        for var in [0,2]:
            position=check_row([var,4,8-var],player)
            if position!=None:break
    if position!=None:
        play[position]='O'
        return True

def computed_move(turn):
    has_played=False
    corners=[0,2,6,8]
    edges=[1,3,5,7]
    if turn==1:
        if play[4]=='X':position=random.choice(corners)
        elif play.index('X')in corners:position=4
        elif play.index('X') in edges:
            position=random.choice([4,0])
            if not position:position=8-play.index('X')
        play[position]='O'
        has_played=True
      
    elif turn==2:
        isposition=True
        if play[4]=='X' and (play[0]=='X' or play[2]=='X' or play[6]=='X' or play[8]=='X'):
            num=random.choice([0,1])
            if num:
                for pos in range(3):
                    if corners[pos]==play.index('O'):position=corners[pos+1]
                if corners[3]==play.index('O'):position=corners[0]
            else:
                for pos in range(3,0,-1):
                    if corners[pos]==play.index('O'):position=coners[pos-1]
                if corners[0]==play.index('O'):position=corners[3]
        elif play[4]=='O' and ((play[0]=='X' and play[8]=='X') or (play[2]=='X' and play[6]=='X')):position=random.choice(edges)
        elif play[4]=='O' and ((play[0]=='X' and (play[5]=='X' or play[7]=='X')) or (play[2]=='X' and (play[3]=='X' or play[7]=='X')) or (play[6]=='X' and (play[1]=='X' or play[5]=='X')) or (play[8]=='X' and (play[1]=='X' or play[3]=='X'))):       
            var=random.choice([0,1])
            if var:
                for pos in range(4):
                    if play[corners[pos]]=='X':position=8-corners[pos]
            else:
                if (play[5]=='X' and play[0]=='X') or (play[2]=='X' and play[3]=='X'):position=1
                elif (play[7]=='X' and play[0]=='X') or (play[6]=='X' and play[1]=='X'):position=3
                elif (play[7]=='X' and play[2]=='X') or (play[8]=='X' and play[1]=='X'):position=5
                elif (play[5]=='X' and play[6]=='X') or (play[8]=='X' and play[3]=='X'):position=7
                    
        elif play[1]=='X' or play[3]=='X' or play[5]=='X' or play[7]=='X':
            if play[4]=='X':position=random.choice(corners)
            elif play[4]!='X' and play[4]!='O':
                if play[1]=='X':position=random.choice([0,2])
                elif play[3]=='X':position=random.choice([0,6])
                elif play[5]=='X':position=random.choice([2,8])
                elif play[7]=='X':position=random.choice([6,8])
            elif play[4]=='O':
                if play[1 and 3]=='X':position=random.choice([0,2,6])
                elif play[3 and 7]=='X':position=random.choice([0,6,8])
                elif play[7 and 5]=='X':position=random.choice([2,6,8])
                elif play[1 and 5]=='X':position=random.choice([0,2,8])
        else:isposition=False
        if isposition:
            play[position]='O'
            has_played=True
    return has_played

def letter(key):
    if key==pygame.K_a:return 'a'
    elif key==pygame.K_b:return 'b'
    elif key==pygame.K_c:return 'c'
    elif key==pygame.K_e:return 'e'
    elif key==pygame.K_f:return 'f'
    elif key==pygame.K_g:return 'g'
    elif key==pygame.K_h:return 'h'
    elif key==pygame.K_i:return 'i'
    elif key==pygame.K_j:return 'j'
    elif key==pygame.K_k:return 'k'
    elif key==pygame.K_l:return 'l'
    elif key==pygame.K_m:return 'm'
    elif key==pygame.K_n:return 'n'
    elif key==pygame.K_o:return 'o'
    elif key==pygame.K_p:return 'p'
    elif key==pygame.K_q:return 'q'
    elif key==pygame.K_r:return 'r'
    elif key==pygame.K_s:return 's'
    elif key==pygame.K_t:return 't'
    elif key==pygame.K_u:return 'u'
    elif key==pygame.K_v:return 'v'
    elif key==pygame.K_w:return 'w'
    elif key==pygame.K_x:return 'x'
    elif key==pygame.K_y:return 'y'
    elif key==pygame.K_z:return 'z'
    elif key==pygame.K_d:return 'd'
    else:return ''
    
def new_game():
    global play
    play=[ 0 for pos in range(9)]
    turn=1
    running=False
    cursor=Cursor()
    status=''
    game_over=False
    name_font=pygame.font.SysFont('Bradley Hand ITC',25)
    name_display_font=pygame.font.SysFont('Bahnschrift',25)
    name_box=RectButtons(Black,15,50,200,50,border=2,text='Enter Your Name',textX=25,textY=60,text_color=Black,font=name_font)
    word_limit=9
    can_input=False
    global new_player
    global name
    if new_player:
        name=''
    while not running and new_player:
        screen.fill(Green)
        name_box.create(screen)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                running=True
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN and name_box.hit():
                    if can_input:
                        new_player=False
                        running=True
                    can_input=True
                if e.key==pygame.K_RETURN and not name_box.hit():
                    can_input=False
                if can_input:
                    if e.key==pygame.K_BACKSPACE:
                        new_name=''
                        for pos in range(len(name)-1):
                            new_name+=name[pos]
                        name=new_name
                    else:
                        if len(name)<word_limit:
                            name+=letter(e.key)
        name_box.text=name           
        if can_input:
            if name_box.text=='Enter Your Name':
                name_box.text=''
            name_box.change(bg_color=Blue)
        else:
            if name_box.text=='':
                name_box.text='Enter Your Name'
            name_box.change(bg_color=Black)
        pygame.display.update()
    running=True
    while running:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                running=False
            if e.type==pygame.KEYDOWN:
                saveX,saveY=cursor.x,cursor.y
                if e.key in [pygame.K_a,pygame.K_LEFT]:cursor.x-=1
                elif e.key in[pygame.K_d,pygame.K_RIGHT]:cursor.x+=1
                elif e.key in [pygame.K_s,pygame.K_DOWN]:cursor.y+=1
                elif e.key in [pygame.K_w,pygame.K_UP]:cursor.y-=1
                elif e.key==pygame.K_RETURN:
                    if not play[cursor.y*3+cursor.x]:
                        play[cursor.y*3+cursor.x]='X'
                        if win_lose_check('X'):
                            status='Won'
                            game_over=True
                        if not game_over:
                            if not make_stop_win('make'):
                                if not make_stop_win('stop'):
                                    if not computed_move(turn):
                                        random_move()
                            if win_lose_check('O'):
                                status='Lost'
                                game_over=True
                            turn+=1
                if cursor.notValid():
                    cursor.x,cursor.y=saveX,saveY                    
        screen.fill(Black)
        screen.blit(name_display_font.render(name,1,Gold),(25,2))
        Display()
        cursor.display()
        pygame.display.update()
        if turn==5:
            game_over=True
        if game_over:
            if status=='Won':
                file=open('Assets/beaten_by.txt','a')
                file.write(name+'\n')
                file.close()
                color=Green
            elif status=='Lost':
                color=Red
            else:color=White
            
        while game_over:
            screen.blit(game_over_font.render('Draw' if not status else 'You '+status,1,color),(GridX,3*Cell+GridY))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=False
                    running=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_n:
                        new_player=True
                    if event.key==pygame.K_RETURN:
                        new_game()
                        game_over=False
                        running=False
name=''
new_player=True
new_game()
pygame.quit()

            
            
