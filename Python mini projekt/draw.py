from tkinter import *#importerar det grafisk library 
import time # importerar delay libarary

from playsound import playsound#ett library för att spela upp mp3 filer
import info# importerar alla variabler
import random_room # importerar rum generar modulen
from random import randint# importerar ett random lib
ghostpos=[0,0]# en temporär variabel för ghost position
playerpos=[-1,-1]#asmma fast för player position

class menu:#" det här är en klass som ritar ut menyn
    def __init__(self):# körs när man kallar på klassen
        delete()# rensar skärmen
        info.menu_up= True
        print(info.menu_up)        
        self.C = C# gör så vi kan använda variabeln över classens funktioner
        if info.game!=True:# om spelet inte har startas så leder start till att man får välja svårighets grad
            self.S= Button(C, command = difficulty, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Start game",fg="#ffffff")
        elif info.game == True:# annars blir det en resume knapp
            self.S = Button(C, command= game,height=10,width= 50,bg = "#000000",highlightcolor = "#ffffff",text = "Resume",fg="#ffffff")#C är canvas alltså det som knappen kommer vara på, command är den funktion som görs på knappens tryck, height width bestämmer storleken,fg är textens färg, bg är knappens färg, highlightcolor är färgen vid knapp tryck,text är knappens text
        self.O= Button(C, command = self.opt, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Options",fg="#ffffff")
        self.E= Button(C, command = Exit, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Exit",fg="#ffffff")
        self.S.pack()#packar upp start knappen
        self.O.pack()#packar upp options knappen
        self.E.pack()# packar upp exit knappen
        C.update()# uppdaterar canvas med de nya objekten

    def opt(self):
        delete()# rensar
        text = Text(self.C,height=30,width=info.W,bg="#000000",fg="#00FF00",font="comic")# samma som förklaring till knappen men font är text stilen
        text.place(x=0,y=0)# placerar objektet
        text.propagate(0)# säger till objektet att inte krympa
        R= Button(self.C,command = Return_menu, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Return",fg="#00ff00")
        R.place(x=(info.W/2)-175,y=550)# placerar knappen
        text.insert(INSERT,control_display())#lägger in text i rutan
        C.update()# updaterar de nya ändringarna
# klassen ovan behövs efter som om det enbart skulle vara funktioner så skulle tkinter programmet fastna i en oändlig loop
# tkinter förut ser alla möjliga vägar som knappar kan ta men med en klass så bryts denna funktion
class difficulty:# en class för alla svårighets nivåer
    def __init__(self):
        delete()
        self.E= Button(C, command = self.Easy, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Easy",fg="#ffffff")
        self.M= Button(C, command = self.Medium, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Medium",fg="#ffffff")
        self.H= Button(C, command = self.Hard, height=10,width = 50,bg = "#000000",highlightcolor= "#ffffff",text="Hard",fg="#ffffff")
        self.E.pack()# packar upp den nya knapparna
        self.M.pack()
        self.H.pack()
        C.pack()# den här fungerar som update men bara om man inför nya widgets inte nya t.ex. rektanglar
    def Easy(self):# funktionerna nedan bestämmer svårighets graden och går vidare att rita ut spel planen
        info.difficulty = 0
        game()# börjar rita ut spelplanen
    def Medium(self):
        info.difficulty = 1
        game()
    def Hard(self):
        info.difficulty = 2
        game()

def rs(inputval,sizevalue):# en funktion som ger oss rätt storlek på alla kordinater igenom att ta ett värde och gångrar det med sizevalue
    return inputval*sizevalue

def getcoord(X,Y):# en function som ger oss cordinaterna för objekt 
    sizevalue = info.ratio
    x =rs(X,sizevalue)
    y =rs(Y, sizevalue)
    return x, y, x+sizevalue, y+sizevalue    

def init():# init kallas från main och ger tillbaka de generade positionerna för objekten
    print("taking values")
    print(playerpos)
    print(ghostpos)
    return [playerpos,ghostpos]
def control_display():# en funktion som ger tillbaka en list av controller i ordning som kommer från info
    control_list= "Controls:\nMove forward              "+info.controls["controls"]["Forward"]+"\nMove backward           "+info.controls["controls"]["Backward"]+"\nMove left                     "+info.controls["controls"]["Left"]+"\nMove right                   "+info.controls["controls"]["Right"]+"\nPause game                "+info.controls["controls"]["Pause"]+"\nInteract                     "+info.controls["controls"]["Interact"]
    return control_list 

def Return_menu():# gör precis vad den heter returnar till menyn
    menu()
def delete():# funktionen rensar skärmen
    for Widget in C.winfo_children():# varje objekt blir ett child av canvas och sparas i winfo
        Widget.destroy()# for loopen går igenom alla objekt och tar bort dem
    C.create_rectangle(0,0,info.W,info.H,fill="#000000")# målar över hela spelplanen
def startup(Can):# funktionen importerar canvas från main
    global C
    C =  Can

def game():# en funktion som ritar ut spel planen och bestämmer start positionen för både spöke och spelare
    delete()#gissa vad den rensar fortfarnade
    C.create_rectangle(20,20,info.W-20,info.H-20,fill="#666666")
    if info.game == False or info.loadroom==True:# om spelet precis har startat eller om jag vill ladda om rummet
        info.g_Hp=2# ställer om spökets hp
        x =2 # x koordinaten
        yr = randint(1,info.ry)# y korrdinaten
        global playerpos
        playerpos=[x,yr]#spelarens position 
        Enterydoor=[0,yr]# ingångs dörren
        random_room.generate(Enterydoor,True)# kallar på att ändra Mapen
        info.loadroom = False#gör så att detta ändast sker en gång
        print("hej")
    Spawn =False# spawn håller koll så endast ett spöka genereras
    for col in range(1,info.rx):
        for row in range(1,info.ry):# två nestade for loopar som går igenom varje ruta i Map fältet
            coord= getcoord(col,row)# får coordinaterna för varje ruta
            if info.Map[col][row] ==0:# 0 är en spelbar ruta
                C.create_rectangle(coord,fill="#404040",outline="#404040")# gör en gråare ruta
                if Spawn == False and randint(1,5)==4:#det är en 20% chans att just den rektangen blir spökets position
                    global ghostpos
                    ghostpos=[col,row]
                    Spawn = True
            elif info.Map[col][row]==3:# om rutans värde är 3 så blir det en ingångsdörr 
                C.create_rectangle(coord,fill="672B00")# en dörr recktange skapas
            elif info.Map[col][row]==4:#4 är en vanlig dörr
                C.create_rectangle(coord,fill="#914F22")
            elif info.Map[col][row]==5:# 5 är den myggan i bärnstenen som av slutar spelet
                C.create_rectangle(coord,fill="#FDD317")
    global player
    player = C.create_rectangle(getcoord(playerpos[0],playerpos[1]),fill="#FFB438")# player objektet skapas
    UpdateHp(True, playerpos)# updaterar värdet utifall detn skulle ha tagit skada
    global ghost
    if  info.difficulty!=0 and randint(0,10)>10:# det är en 90% chans att ett spöke generas
        info.spawn=True# info spawn är att ett spöke har genererats
        ghost= C.create_rectangle(getcoord(ghostpos[0],ghostpos[1]),fill="#90D8DA")# ghost objektet skapas
        UpdateHp(False,ghostpos)# updaterar hp
    C.update()# uppdaterar canvas
    info.game = True#uppdaterar info variablarna
    info.menu_up = False

def UpdateHp(Entity,pos):# funktionen ändrar objektens utseende beroendes på hur mycket hp den har
    blood= "#E80E02"# färg på bloodet
    width =1# standar d width
    global player# kallar in player och ghost
    global ghost
    if Entity == True:# true betyder att det är spelaren vilket har en unik färg och hp
        objekt = player
        color = "#FFB438"
        hp =info.p_Hp
        half=2
    else:# annars är det spöke
        objekt = ghost
        color = "#90D8DA"
        hp=info.g_Hp
        half=1
    if hp<=half:# om hp är mindre än objektets halva så kommer den få en liten röd ring 
        bcolor = blood# bcolor är kant färgen, border color
        width =4
    elif hp==0:# om den inte har något hp alls så blir objektet helt röd
        color = blood
    else:
        bcolor=color# om inget av de ovan stämmer så behåller den sin färg
    C.delete(objekt)# tar bort det gamla 
    objekt =C.create_rectangle(getcoord(pos[0],pos[1]),fill=color,outline=bcolor,width=width)# ritar ut det nya
    if Entity == True:
        player = objekt
    else:
        ghost = objekt

def Attack(pos,entity):# attack har några buggar om jag inte hade tid att fixa 
    # ideen är att ett block ska dyka upp för att idikera att någon attackerar där
    global Attack# ttack objektet
    if entity==True:# spelar attacken har en färg
        Color = "#D4E802"
    else:# ghost attack har en annan
        Color = "#8B09CE"
    print("attck")
    Attack=C.create_rectangle(getcoord(pos[0],pos[1]),fill=Color,width = 0)# skapar attack rutan
    C.update()# uppdaterar canvas
    time.sleep(0.2)#väntar så vi ser att rutan dök upp
    print("finished")
    C.delete(Attack)# tar bort rutan
    C.update()# uppdaterar  


def Credits():
    print("you did it")
    info.game=False# uppdaterar några värden
    info.loadroom=True 
    for frame in info.animation:# går igenom varje pic i animation lib
        pic=info.animation[frame]# frame blir namnet av själva bilden så vi måste hämta innehållet av bilden
        Animation(pic[0])# den första är bilden och den skrivs ut
        C.update()# updaterar vad som skrevs ut
        if pic[2] != "none":# kollar å att bilden innehåller en ljud fil
            playsound(pic[2])# spelar up ljud filen
        if pic[1] != "none":# kollar så bilden innehåller en delay
            time.sleep(pic[1])# delay
    menu()# går tillbaka till menyn

def Animation(string):
    delete()
    text = Text(C,height=info.H,width=info.W,bg="#000000",fg="#00FF00",font="Consolas")# fixar text rutan som för
    text.place(x=0,y=0)
    text.propagate(0)
    text.delete("insert linestart", "insert lineend")# rensar textrutan
    text.insert(INSERT,string)# sätter in den stringen som man bad om


def move(position,entity):
    dx = position[0]*info.ratio# cordinaterna för objektets nya grafiska position
    dy = position[1]*info.ratio
    if entity == True:
        C.move(player, dx, dy)# här skrivs spelaren ut
    else:
        C.move(ghost,dx,dy)
    C.update()# uppdatera den grafiska planen
                   
def Exit():
    info.master = False# avslutar whileloopen i main 
    C.destroy()# förstör canvas
    C.update()# updaterar att det hände
    print("exit")