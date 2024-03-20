from tkinter import *
from Maps import *
from biblio import *
import pygame 
from pygame.locals import *

pygame.init() #initialisation de pygame pour le son

x=5
r=600/13/2

xl=5 #coordonées de lestin dans la matrice
yl=5

xs=600/13 #saut de lestin
ys=600/13

xc=5*600/13+600/13/2#coordonées de lestin dans le canvas
yc=5*600/13+600/13/2

xM=2 #coordonnées de départ

yM=2



MapComplete2=[[A1,A2,A3],
             [B1,B2,B3],
             [C1,C2,C3]]



MapComplete = transpose(MapComplete2)


score=0 #score d'ennemis tués par lestin

M=C3 #map de depart



#============================déplacement Lestin==========
def deplacementLestin(xs,ys):
    global xc,yc,r
    
    xc,yc=xc+xs,yc+ys
    
    can.coords(lestin,xc-r,yc-r)

#============================Coordonnées par rapport à la matrice==========

def coor(xx,yy,xs1,ys1,x3,y3,xc3,yc3,xM1,yM1,M1):
    global M, xs,ys,xl,yl,xc,yc,r,xM,yM,mechant1,mechant2,mob1,fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    if M1==0 or M1==10 or M1==20:#endroit où lestin peut aller
        xl,yl=xx,yy
        xs=xs1
        ys=ys1 
        deplacementLestin(xs,ys)
        

    if M1==4:#emplacement de la fin du jeu
        if score != 0 : #différentes fin suivant le fait que Lestin ait tué des ennemis ou pas 
            fin16=can.create_image(0,0,anchor=NW,image=f16)
            fin15=can.create_image(0,0,anchor=NW,image=f15)
            fin14=can.create_image(0,0,anchor=NW,image=f14)
            fin13=can.create_image(0,0,anchor=NW,image=f13)
            fin12=can.create_image(0,0,anchor=NW,image=f12)
            fin11=can.create_image(0,0,anchor=NW,image=f11)
            fin10=can.create_image(0,0,anchor=NW,image=f10)
            dominique.stop()
            bellaciao.play()

        if score == 0: #différentes fin suivant le fait que Lestin ait tué des ennemis ou pas 
            fin16=can.create_image(0,0,anchor=NW,image=f16)
            fin25=can.create_image(0,0,anchor=NW,image=f25)
            fin14=can.create_image(0,0,anchor=NW,image=f14)
            fin23=can.create_image(0,0,anchor=NW,image=f23)
            fin22=can.create_image(0,0,anchor=NW,image=f22)
            fin11=can.create_image(0,0,anchor=NW,image=f11)
            fin10=can.create_image(0,0,anchor=NW,image=f10)
            dominique.stop()
            evilmorty.play()

            
    if  M1==3: #changement de map
        xl,yl=x3,y3
        xc,yc=xc3,yc3
        can.coords(lestin,xc-r,yc-r)
        xM,yM=xM1,yM1
        M=MapComplete[xM][yM]
        
        if MapComplete[xM][yM]==A1:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-20,-20)
            mechant1=can.create_image(20,380,anchor=NW, image=mob1)
            mechant2=can.create_image(300,490,anchor=NW, image=mob1)

        
        if MapComplete[xM][yM]==A2:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-620,-10)
            mechant1=can.create_image(300,20,anchor=NW, image=mob1)
            mechant2=can.create_image(490,20,anchor=NW, image=mob1)


    
        if MapComplete[xM][yM]==A3:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-1180,-20)
            mechant1=can.create_image(250,150,anchor=NW, image=mob1)
            mechant2=can.create_image(420,150,anchor=NW, image=mob1)
            



        if MapComplete[xM][yM]==B1:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-20,-620)
            mechant1=can.create_image(20,20,anchor=NW, image=mob1)
            mechant2=can.create_image(500,50,anchor=NW, image=mob1)
            

        
        if MapComplete[xM][yM]==B2:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-580,-620)
            mechant1=can.create_image(300,260,anchor=NW, image=mob1)

        	
            
        if MapComplete[xM][yM]==B3:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-1170,-600)
            mechant1=can.create_image(440,120,anchor=NW, image=mob1)


        if MapComplete[xM][yM]==C1:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-20,-1200)
            mechant1=can.create_image(20,30,anchor=NW, image=mob1)
            mechant2=can.create_image(20,490,anchor=NW, image=mob1)

        if MapComplete[xM][yM]==C2:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-620,-1230) 
            mechant1=can.create_image(20,460,anchor=NW, image=mob1)
        
        if MapComplete[xM][yM]==C3:
            can.delete(mechant1,mechant2)
            can.coords(fondB35,-1200,-1170)
            mechant1=can.create_image(20,490,anchor=NW, image=mob1)       

#======================cinematique de fin=======================

def cine1(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin10)
def cine2(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin11)
def cine3(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin12)
    can.delete(fin22)
def cine4(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin13)
    can.delete(fin23)
def cine5(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin14)
def cine6(event):
    global fin10,fin11,fin12, fin13, fin14, fin15, fin16, fin22, fin23, fin25
    can.delete(fin15)
    can.delete(fin25)


		



#==============fonctions de déplacement=================


def up(event):#fonctionne
    global M, xs,ys,xl,yl,xc,yc,r,xM,yM
    M1=M[xl][yl-1]
    xx,yy=xl,yl-1
    xs1=0
    ys1=-600/13
    x3,y3=xl,12
    xc3,yc3=xc,600-600/13
    xM1,yM1=xM,yM-1
    coor(xx,yy,xs1,ys1,x3,y3,xc3,yc3,xM1,yM1,M1)

       

def down(event):
    global M,xs,ys,xl,yl,xc,yc,r,xM,yM

    M1=M[xl][yl+1]
    xx,yy=xl,yl+1
    xs1=0
    ys1=600/13
    x3,y3=xl,0
    xc3,yc3=xc,600/13
    xM1,yM1=xM,yM+1
    coor(xx,yy,xs1,ys1,x3,y3,xc3,yc3,xM1,yM1,M1)


        
def right(event):#fonctionne
    global M, xs,ys,xl,yl,xc,yc,r,xM,yM

    M1=M[xl+1][yl]
    xx,yy=xl+1,yl
    xs1=600/13
    ys1=0
    x3,y3=0,yl
    xc3,yc3=600/13,yc
    xM1,yM1=xM+1,yM
    coor(xx,yy,xs1,ys1,x3,y3,xc3,yc3,xM1,yM1,M1)

    
    
def left(event):
    global M, xs,ys,xl,yl,xc,yc,r,xM,yM
    M1=M[xl-1][yl]
    xx,yy=xl-1,yl
    xs1=-600/13
    ys1=0
    x3,y3=12,yl
    xc3,yc3=600-600/13,yc
    xM1,yM1=xM-1,yM
    coor(xx,yy,xs1,ys1,x3,y3,xc3,yc3,xM1,yM1,M1)

#=============création d'un menu en appuyant sur echap============

def menu(event):
    global pause
    pause = can.create_image(0,0,anchor=NW,image=imgmorty)

def deletemenu(event):
    can.delete(pause)

#============attaque de lestin============
    
def attaque(event):
    global M,xl,yl,score,mechant1,mechant2
    ax=int(event.x)/(600/13)
    ay=int(event.y)/(600/13)
    ax=int(ax//1)
    ay=int(ay//1)
    
    if M[ax][ay]==11 and M[xl][yl]==10:
        score+=1
        M[ax][ay]=12
        print(score)
        can.delete(mechant1)
        coup.play()


    if M[ax][ay]==21 and M[xl][yl]==20:
        score+=1
        M[ax][ay]=22
        print(score)
        can.delete(mechant2)
        coup.play()

     
#1= mur
#3=passage à une autre map
#10=autour du mob, d'où on peut le tuer
#11 et 21 =mob vivant
#12et 22 =mob mort

#===============================INTRO==================

x=5
cpt = 0

def deplacement():

	img_coords = [0.0, -600.0]
	img_width = img_2.width()

	if (img_coords[0] + img_width <=  800) :
		can.move(image,0,-x)
	if flag >0: 
	   	fen.after(70,deplacement)

def stop_it():
    global flag    
    flag =0
    fen.after(6000,stop_it)

def start_it():
    "démarrage de l'animation"
    global flag
    dominique.play()
    if flag ==0:            # pour ne lancer qu’une seule boucle 
       flag =1
       deplacement()

flag =0 


#==============================programme principale==================

fen = Tk()
can = Canvas(fen,width=600,height=600,bg="black")
can.pack()

#====================attribution chemins des images ====================== 
#============images principales du jeu==========

imgmorty1= PhotoImage(file='morty1.gif')
imgmorty= PhotoImage(file='menu.gif')
imgfond= PhotoImage(file='fond.gif')
mob1= PhotoImage(file='mechant1.gif')

#============images de la cinematique de fin==========

f10 = PhotoImage(file='fin/f10.gif')
f11 = PhotoImage(file='fin/f11.gif')
f12 = PhotoImage(file='fin/f12.gif')
f13 = PhotoImage(file='fin/f13.gif')
f14 = PhotoImage(file='fin/f14.gif')
f15 = PhotoImage(file='fin/f15.gif')
f16 = PhotoImage(file='fin/f16.gif')
f22 = PhotoImage(file='fin/f22.gif')
f23 = PhotoImage(file='fin/f23.gif')
f25 = PhotoImage(file='fin/f25.gif')

#============Mettre les images dans des variables==========

fin10 = can.create_image(2300, 400,anchor=NW,image=f10)
fin11 = can.create_image(2300, 400,anchor=NW,image=f11)
fin12 = can.create_image(2300, 400,anchor=NW,image=f12)
fin13 = can.create_image(2300, 400,anchor=NW,image=f13)
fin14 = can.create_image(2300, 400,anchor=NW,image=f14)
fin15 = can.create_image(2300, 400,anchor=NW,image=f15)
fin22 = can.create_image(2300, 400,anchor=NW,image=f22)
fin23 = can.create_image(2300, 400,anchor=NW,image=f23)
fin25 = can.create_image(2300, 400,anchor=NW,image=f25)
fin16 = can.create_image(2300, 400,anchor=NW,image=f16)



mechant2 = can.create_image(230, 400,anchor=NW,image=mob1)
pause = can.create_image(-1200,-1200,anchor=NW,image=imgmorty)
fondB35 = can.create_image(-1200,-1200,anchor=NW,image=imgfond)
mechant1=can.create_image(230, 400,anchor=NW,image=mob1)
lestin = can.create_image(xc-r,yc-r,anchor=NW,image=imgmorty1)

#============Musiques du jeu========================

bellaciao = pygame.mixer.Sound("Musiques/Bella Ciao.wav")
evilmorty = pygame.mixer.Sound("Musiques/Evil Morty.wav")
dominique = pygame.mixer.Sound("Musiques/Dominique.wav")
coup = pygame.mixer.Sound("Musiques/coup.wav")



bou2 = Button(fen, text='JOUER', width =8, command=start_it) #bouton pour lancer l'animation du début
bou2.pack()


#============image d'animation du début==========

imgfile = 'intro.gif'
img = PhotoImage(file=imgfile)
img_2 = img.subsample(1,1)
image = can.create_image(0,0,anchor=NW,image=img_2)


#============affectation des touches==========

fen.bind("<Left>", left)          
fen.bind("<Right>", right)        
fen.bind("<Up>", up)              
fen.bind("<Down>", down)
fen.bind('<Button-1>', attaque)
fen.bind("<Escape>", menu)
fen.bind("<KeyPress-p>", deletemenu)
fen.bind("<KeyPress-l>", cine1)
fen.bind("<KeyPress-e>", cine2)
fen.bind("<KeyPress-s>", cine3)
fen.bind("<KeyPress-t>", cine4)
fen.bind("<KeyPress-i>", cine5)
fen.bind("<KeyPress-n>", cine6)




fen.mainloop() # Lancement de la boucle du programme, en attente d'événements (clavier, souris,...)



