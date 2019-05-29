#om draw var utseendet så blir random room DNA:t som bestämmer hur Utseedndet blir
from random import randint#importerar random library
import info# importerar variablerna
# dörrar kan endast existera nära en vägg

def generate(Enterydoor,Type):# hela funktionen ändrar Map värdet till spelbara rutor och dörrar
    # funktionen tar in start värdena Ebtery door och type
    # type beskriver vilken grafisk funktion som ska användas
    # entery door  är där grafen skär y axeln
    info.Map[Enterydoor[0]+1][Enterydoor[1]]=3# ger ett värde till entery döörens position
    roomtot=0# totala antalet rum
    vertex_x= randint(1,20)# kordinaterna för vertex blir random genererade
    vertex_y= randint(0,Enterydoor[1])
    last_y = Enterydoor[1]# föra y startar som entery door
    for col in range(0,info.rx):
        for row in range (0,info.ry):# for looparna  ställer om hela kordinat systemet till väggar
            info.Map[col][row]=2            
    for col in range(2,info.rx-2):# for loopen går igenom varje x kordinat
        y = graf(col,vertex_x,vertex_y,Enterydoor[1],Type)# får uy y beroende av x
        if y<info.ry and y>-1:# kollar så atty är inom range för Map
            info.Map[col][y]=0# sätter punkten till gå bar yta
            for width in range(col-randint(2,4),col+randint(2,4)):# for loopen ger en random bredd med punkten imitten
                if width < info.rx and width > 0:# kollar så att det är inom range för Map 
                    info.Map[width][y]=0# gåbar yta
            if y<last_y and last_y>-1:
                # om y är större än förra y så stiger grafen
                # vilket betyder att vi behöver börja från förra y och arbeta nedåt
                for pos in range(y,last_y):# for loopen gör som ovan
                    print(str(pos))
                    info.Map[col][pos]=0# fixar gåbar yta med random bredd
                    for width in range(col-randint(2,4),col+randint(2,4)):
                        info.Map[width][pos]=0
            elif y>last_y and last_y>-1:
                # när y är mindre än förra y så gå grafen ned
                # då behöver vi gå från last y och nedåt
                for pos in range(last_y,y):# pos blir lasty och går sedan ned till y
                    print("-1h"+str(pos))
                    if pos >-1 and pos <info.ry+1:#kollar så att pos är inom Map
                        info.Map[col][pos]=0    
                    for width in range(col-randint(2,4),col+randint(2,4)):# generarar random bredd 
                        if width < info.rx and width > 0: 
                            info.Map[width][pos]=0
                    if pos == (info.ry-1) or col == (info.rx-3)and roomtot <1:# vi behöver endast en dörr i slutet av kurvan
                        info.Map[col][pos]=4# gör rutan till en dör
                        roomtot+=1# ökar totala dörr mängden
        elif y>info.ry:# om y är större än ry så måste vi fixaså att grafen ansluts till väggen
            print(y)
            for pos in range(last_y,info.ry):#vi går från sista y till ry
                print("last"+str(pos))
                if pos >-1 and pos <info.ry+1:#kollar så allt är inom range
                    info.Map[col][pos]=0# gör rutan gåbar
                    if pos == (info.ry-1) or col == (info.rx-2)and roomtot<1:# kollar om rutan är nära en vägg
                        info.Map[col][pos]=4#gör en dörr
                        if info.Exit>0 and randint(0,101)<=info.Exit:# en chans beroende på hur många rum om du har gått igenom kan göra dörren tillen bärnsten
                            info.Map[col][pos]=5# gör dörren till en bärnsten/vägen ut
                        roomtot+=1
                    else:# om det inte blev en dörr så generaras en random bredd    
                        for width in range(col-randint(2,4),col+randint(2,4)):# bredden blir 2-4 rutor åt varje håll
                            if width < info.rx and width > 0: 
                                info.Map[width][pos]=0
        if y < 0:# om y bestämmer sig för att bugga över spelplanen
            info.Map[col][last_y]=4# då sätts en dörr på sista y
            roomtot+=1# totala antlet dörrar ökar 
        last_y=y
    print(roomtot)
    if last_y== graf(2,vertex_x,vertex_y,Enterydoor[1],Type) or roomtot <1:# om linjen har helt plan eller om inte tillräckligt med dörrar skapades så körs funktionen om igen
        generate(Enterydoor,Type)        


def graf(x,vx,vy,C,Type):
    if Type == True:# type true är en andra grand kurva
        sq = vx**2# ekvationerna bestämmer a b och c värde utifrån vertex punkten och skärnings punkten
        top = vy-C
        dev = top/sq
        a=-1*dev
        b = vx*(-2*a)
        
        return int((a*(x**2))+(b*x)+C)# ger tillbaka en andragrads ekvation
    elif Type ==False:# ett exempel på att man skulle kunna ha olika typer av ekvationer
        return int((3*x)+5)# dock bara en rät linje ekvation
