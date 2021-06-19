import pygame
import math

def DisplayText(screen,text,color,x,y,font):
    Text=font.render(text,True,color)
    screen.blit(Text,(x,y))

class RectButtons:
    def __init__(self,bg_color,x,y,width,height,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.border=border
        self.text=text
        self.textX=textX
        self.textY=textY
        self.text_color=text_color
        self.font=font
        self.r_x=x
        self.r_y=y
        self.r_width=width
        self.r_height=height
        self.r_bg_color=bg_color
        self.r_border=border
        self.r_text=text
        self.r_textX=textX
        self.r_textY=textY
        self.r_text_color=text_color
        self.r_font=font
           
    def create(self,screen):
        if self.border==None:
            pygame.draw.rect(screen,self.bg_color,(self.x,self.y,self.width,self.height))
        else:
            pygame.draw.rect(screen,self.bg_color,(self.x,self.y,self.width,self.height),self.border)
        if self.text!=None:
            DisplayText(screen,self.text,self.text_color,self.textX,self.textY,self.font)

    def hit(self):
        cursor=pygame.mouse.get_pos()
        X=math.floor(cursor[0])
        Y=math.floor(cursor[1])
        if X in range(self.x,self.x+self.width+1) and Y in range(self.y,self.y+self.height+1):
            return True
        return False

    def change(self,bg_color=None,x=None,y=None,width=None,height=None,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        if x:self.x=x
        if y:self.y=y
        if width:self.width=width
        if height:self.height=height
        if bg_color:self.bg_color=bg_color
        if border:self.border=border
        if text:self.text=text
        if textX:self.textX=textX
        if textY:self.textY=textY
        if text_color:self.text_color=text_color
        if font:self.font=font

    def restore(self):
        self.x=self.r_x
        self.y=self.r_y
        self.width=self.r_width
        self.height=self.r_height
        self.bg_color=self.r_bg_color
        self.border=self.r_border
        self.text=self.r_text
        self.textX=self.r_textX
        self.textY=self.r_textY
        self.text_color=self.r_text_color
        self.font=self.r_font
        
class SqButtons:
    def __init__(self,bg_color,x,y,side,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        self.x=x
        self.y=y
        self.side=side
        self.bg_color=bg_color
        self.border=border
        self.text=text
        self.textX=textX
        self.textY=textY
        self.text_color=text_color
        self.font=font
        self.r_x=x
        self.r_y=y
        self.r_side=side
        self.r_bg_color=bg_color
        self.r_border=border
        self.r_text=text
        self.r_textX=textX
        self.r_textY=textY
        self.r_text_color=text_color
        self.r_font=font

    def create(self,screen):
        if self.border==None:
            pygame.draw.rect(screen,self.bg_color,(self.x,self.y,self.side,self.side))
        else:
            pygame.draw.rect(screen,self.bg_color,(self.x,self.y,self.side,self.side),self.border)
        if self.text!=None:
            DisplayText(screen,self.text,self.text_color,self.textX,self.textY,self.font)

    def hit(self):
        cursor=pygame.mouse.get_pos()
        X=math.floor(cursor[0])
        Y=math.floor(cursor[1])
        if X in range(self.x,self.x+self.side+1) and Y in range(self.y,self.y+self.side+1):
            return True
        return False

    def change(self,bg_color=None,x=None,y=None,side=None,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        if x:self.x=x
        if y:self.y=y
        if side:self.side=side
        if bg_color:self.bg_color=bg_color
        if border:self.border=border
        if text:self.text=text
        if textX:self.textX=textX
        if textY:self.textY=textY
        if text_color:self.text_color=text_color
        if font:self.font=font

    def restore(self):
        self.x=self.r_x
        self.y=self.r_y
        self.side=self.r_side
        self.bg_color=self.r_bg_color
        self.border=self.r_border
        self.text=self.r_text
        self.textX=self.r_textX
        self.textY=self.r_textY
        self.text_color=self.r_text_color
        self.font=self.r_font

class TriButtons:
    def __init__(self,bg_color,x1,y1,x2,y2,x3,y3,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.bg_color=bg_color
        self.border=border
        self.text=text
        self.textX=textX
        self.textY=textY
        self.text_color=text_color
        self.font=font
        self.r_x1=x1
        self.r_y1=y1
        self.r_x2=x2
        self.r_y2=y2
        self.r_x3=x3
        self.r_y3=y3
        self.r_bg_color=bg_color
        self.r_border=border
        self.r_text=text
        self.r_textX=textX
        self.r_textY=textY
        self.r_text_color=text_color
        self.r_font=font

    def create(self,screen):
        if self.border==None:
            pygame.draw.polygon(screen,self.bg_color,((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)))
        else:
            pygame.draw.polygon(screen,self.bg_color,((self.x1,self.y1),(self.x2,self.y2),(self.x3,self.y3)),self.border)
        if self.text!=None:
            DisplayText(screen,self.text,self.text_color,self.textX,self.textY,self.font)

    def hit(self):
        cursor=pygame.mouse.get_pos()
        X=math.floor(cursor[0])
        Y=math.floor(cursor[1])
        
        total_area=abs(self.x1*(self.y2-self.y3)+self.x2*(self.y3-self.y1)+self.x3*(self.y1-self.y2))*0.5
        a1 = abs(X*(self.y2-self.y3)+self.x2*(self.y3-Y)+self.x3*(Y-self.y2))
        a2 = abs(self.x1*(Y-self.y3)+X*(self.y3-self.y1)+self.x3*(self.y1-Y))
        a3 = abs(self.x1*(self.y2-Y)+self.x2*(Y-self.y1)+X*(self.y1-self.y2))
        if (a1 + a2 + a3)*0.5==total_area:
            return True
        else:return False
    
    def change(self,bg_color=None,x1=None,y1=None,x2=None,y2=None,x3=None,y3=None,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        if x1:self.x1=x1
        if y1:self.y1=y1
        if x2:self.x2=x2
        if y2:self.y2=y2
        if x3:self.x3=x3
        if y3:self.y3=y3
        if bg_color:self.bg_color=bg_color
        if border:self.border=border
        if text:self.text=text
        if textX:self.textX=textX
        if textY:self.textY=textY
        if text_color:self.text_color=text_color
        if font:self.font=font

    def restore(self):
        self.x1=self.r_x1
        self.y1=self.r_y1
        self.x2=self.r_x2
        self.y2=self.r_y2
        self.x3=self.r_x3
        self.y3=self.r_y3
        self.bg_color=self.r_bg_color
        self.border=self.r_border
        self.text=self.r_text
        self.textX=self.r_textX
        self.textY=self.r_textY
        self.text_color=self.r_text_color
        self.font=self.r_font
        
class RoundButtons:
    def __init__(self,bg_color,x,y,radius,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        self.x=x
        self.y=y
        self.radius=radius
        self.bg_color=bg_color
        self.border=border
        self.text=text
        self.textX=textX
        self.textY=textY
        self.text_color=text_color
        self.font=font
        self.r_x=x
        self.r_y=y
        self.r_radius=radius
        self.r_bg_color=bg_color
        self.r_border=border
        self.r_text=text
        self.r_textX=textX
        self.r_textY=textY
        self.r_text_color=text_color
        self.r_font=font

    def create(self,screen):
        if self.border==None:
            pygame.draw.circle(screen,self.bg_color,(self.x,self.y),self.radius)
        else:
            pygame.draw.circle(screen,self.bg_color,(self.x,self.y),self.radius,self.border)
        if self.text!=None:
            DisplayText(screen,self.text,self.text_color,self.textX,self.textY,self.font)

    def hit(self):
        cursor=pygame.mouse.get_pos()
        X=math.floor(cursor[0])
        Y=math.floor(cursor[1])
        if (X-self.x)**2+(Y-self.y)**2<=self.radius**2:
            return True
        else:return False  

    def change(self,bg_color=None,x=None,y=None,radius=None,border=None,text=None,textX=None,textY=None,text_color=None,font=None):
        if x:self.x=x
        if y:self.y=y
        if radius:self.radius=radius
        if bg_color:self.bg_color=bg_color
        if border:self.border=border
        if text:self.text=text
        if textX:self.textX=textX
        if textY:self.textY=textY
        if text_color:self.text_color=text_color
        if font:self.font=font

    def restore(self):
        self.x=self.r_x
        self.y=self.r_y
        self.radius=self.r_radius
        self.bg_color=self.r_bg_color
        self.border=self.r_border
        self.text=self.r_text
        self.textX=self.r_textX
        self.textY=self.r_textY
        self.text_color=self.r_text_color
        self.font=self.r_font
        
class OvalButtons(RectButtons):
    def create(self,screen):
        if self.border==None:
            pygame.draw.ellipse(screen,self.bg_color,(self.x,self.y,self.width,self.height))
        else:
            pygame.draw.ellipse(screen,self.bg_color,(self.x,self.y,self.width,self.height),self.border)
        if self.text!=None:
            DisplayText(screen,self.text,self.text_color,self.textX,self.textY,self.font)

    def hit(self):
        cursor=pygame.mouse.get_pos()
        X=math.floor(cursor[0])
        Y=math.floor(cursor[1])
        a=self.width/2
        b=self.height/2
        if (X-self.x-a)**2*b**2+(Y-self.y-b)**2*a**2<=(a*b)**2:
            return True
        else:return False
        

button_dict={'rectangle':RectButtons, 'triangle':TriButtons, 'square':SqButtons, 'round':RoundButtons, 'oval':OvalButtons}
if __name__=='__main__':
    import pygame
    from Colors import*
    running=True
    screen=pygame.display.set_mode((400,100))
    rectangle=RectButtons(Red,10,10,50,30)
    square=SqButtons(Red,70,10,50)
    circle=RoundButtons(Red,155,35,25)
    triangle=TriButtons(Red,190,60,240,40,220,10)
    oval=OvalButtons(Red,250,10,50,30)
    buttons={rectangle, triangle, square, circle, oval}
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            for button in buttons:
                if button.hit():
                    button.change(bg_color=Green)
                else:button.restore()
                    
        rectangle.create(screen)
        square.create(screen)
        circle.create(screen)
        triangle.create(screen)
        oval.create(screen)
        pygame.display.update()
    pygame.quit()
