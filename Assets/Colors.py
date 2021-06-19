White=(255,255,255)
Red=(255,0,0)
Blue=(0,0,255)
SkyBlue=(135,206,235)
Green=(0,255,0)
Silver=(180,180,180)
Grey=(128,128,128)
Black=(0,0,0)
Cyan=(0,255,255)
Magenta=(255,0,255)
Yellow=(255,255,0)
Orange=(255,165,0)
OrangeRed=(255,69,0)
Gold=(255,215,0)
Purple=(128,0,128)
Violet=(148,0,139)
color_list=[White,Yellow,Gold,Orange,OrangeRed,Red,Green,Cyan,SkyBlue,Blue,Magenta,Violet,Purple,Black,Grey,Silver]

color_dict={'white':White,'gold':Gold,'yellow':Yellow,'orange':Orange,'orangered':OrangeRed,'red':Red,'green':Green,'skyblue':SkyBlue,'magenta':Magenta,'violet':Violet,'purple':Purple,'cyan':Cyan,'blue':Blue,'black':Black,'grey':Grey,'silver':Silver}
def Light(color,value):
    new_color=[color[0]+value,color[1]+value,color[2]+value]
    for pos in range(3):
        if new_color[pos]>255:new_color[pos]=255
        elif new_color[pos]<0:new_color[pos]=0
    return (new_color[0],new_color[1],new_color[2])

def Dark(color,value):
    new_color=[color[0]-value,color[1]-value,color[2]-value]
    for pos in range(3):
        if new_color[pos]>255:new_color[pos]=255
        elif new_color[pos]<0:new_color[pos]=0
    return (new_color[0],new_color[1],new_color[2])

if __name__=='__main__':
    import pygame
    screen=pygame.display.set_mode((1000,100))
    x,y=20,20
    for color in color_list:
        pygame.draw.rect(screen,color,(x,y,50,50))
        x+=50    
    pygame.display.update()
    input()
        
    
