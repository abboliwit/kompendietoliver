#den här modulen är själva Hjärnana av detta programm 
#DEn bestämmer t.ex. vart och hur spelarna kan gå
 
import draw# importerar  draw modulen
import keyboard# importerar keyboard librariet som gör så att man kan registrera knapp tryck
import time# ett delay lib
from tkinter import *# det grafiska libet
import info# alla variabler som gäller över moduler
master= Tk()# master blir det som allt som ska ritas läggs in i
prevpress=False# en variable som ändras när en tangent trycks
loop = -1# totala 
C =Canvas(master,bg="#000000",height=info.H,width = info.W)# widgeten som vi kommer rita och lägga på nya generationer av widgetar
C.pack()#skriver ut den
C.propagate(0)# gör att den inte krymper
C.update()# updaterar canvas
draw.startup(C)# se draw modul 
draw.menu()# se draw modul
class position:# en class för alla gående objekts positioner 
    def __init__(self,Entity):# körs engång och sparar värden på objektens postitioner
        self.player = Entity[0]
        self.ghost = Entity[1]
        self.start = Entity[0]

    def change(self,entity, value):# change är en funktion som kan kallas på för att ändra spelarens eller spökets positioner
        if entity == True:#entity true är spelaren
            self.player=value
        if entity == False:#entity false blir då spöket
            self.ghost = value

def radar(middle,attack,Entity):
    print(middle)
    # en attack har en range på ett block från spelaren åt varje håll
    # radarn har samma range
    for col in range(middle[0]-1,middle[0]+2):# två nestlade for loopar som går igenom ett 9x9 område runt entity:t
        for row in  range(middle[1]-1,middle[1]+2):
            if attack==False:# om vi inte attackerar så kollar vi bara efter dörrar
                if info.Map[col][row]== 4:
                    # om en rutan i området är en dörr så genererar vi ett nytt område 
                    global loop
                    loop = -1# resetar loop till start värdet
                    if info.difficulty==2 and info.Exit !=100:# om svårigheten är hard så ökar chansen för vägen ut med 5 procent
                        info.Exit+=5
                    elif info.Exit!= 100:# annars ökar den med 10 % men den kan inte bli över hundra
                        info.Exit+=10
                    print(info.Exit)
                    return True
                elif info.Map[col][row]==5:# 5 är värdet på utgången
                    info.Exit=0#resetar de viktigaste värdena innan credits
                    info.loadroom=True# gör så ett nytt rum kan genereras
                    info.game=False
                    loop = -1
                    draw.Credits()# se draw modul
            else:# annars om det är en attack
                if info.Map[col][row]!= 2 and [col,row]!=middle:# om positionen inte har ett vägg värde eller är attackerarens postition
                    print(col,row)
                    #draw.Attack([col,row],Entity)# ska rita ut en attack animation men det är lite buggat  
                if Entity==True and [col,row]==pos.ghost:# gör skada om spöket är inom attack cirkeln och spelaren attackerar
                    print("HIT!")
                    info.g_Hp-=1# tar bort ett hp från spöket
                    draw.UpdateHp(False,[col,row])#SE draw modulen
                elif Entity==False and [col,row]==pos.player:# om spöket attackerar och spelaren är i attack cirkeln så skadas spelaren
                    info.p_Hp-=1#spelarens hp går ned med ett 
                    draw.UpdateHp(True,[col,row])# Se draw modulen
            print(str(col)+" , "+str(row))
    else:
        return False
            
def moveghost():
    step=[0,0]
    powerMove = True# variabeln ändras endast när spöket rör på sig vilket gör inte kan gå och attackera samtidigt
    if pos.ghost[0]>pos.player[0]and pos.ghost[0] !=(pos.player[0]+1):
        pos.ghost[0]-=1# ändrar steg och spökets position beroendes på spökets koordinater jämfört med spelaren
        step[0]-=1
        powerMove=False
    if pos.ghost[0]<pos.player[0]and pos.ghost[0] !=(pos.player[0]-1):
        pos.ghost[0]+=1
        step[0]+=1
        powerMove=False
    if pos.ghost[1]>pos.player[1]and pos.ghost[1] !=(pos.player[1]+1):
        pos.ghost[1]-=1
        step[1]-=1
        powerMove=False
    if pos.ghost[1]<pos.player[1]and pos.ghost[1] !=(pos.player[1]-1):
        pos.ghost[1]+=1
        step[1]+=1
        powerMove=False
    draw.move(step,False)# se draw modulen
    if powerMove==TRUE:
        radar(pos.ghost,True,False)# om den inte rörde på sig så betyder det att spelaren är tillräckligt nära föra att attackera

def wallhit (Entity,Prev,step):# funktionen kollar så att spelaren inte försöker gå in i väggarna 
    Position= [Prev[0]+step[0],Prev[1]+step[1]]#räknar
    print(step)
    print(Prev)
    print(Position)
    if Position[0]<=0:# elif satsen här kollar om spelaren skulle fått för sig att buga sig för långt utanför planen för då räknas det inte som väggar, och då sätter den tillbaka spelaren till start positionen  
        pos.change(Entity,pos.start)
        print(pos.start)
    elif Position[1]<=0:
        print("na boi")
        pos.change(Entity,pos.start)
    elif Position[0]>=info.rx:
        print("no")
        pos.change(Entity,pos.start)
    elif Position[1]>=info.ry:
        print("wat")
        pos.change(Entity,pos.start)
    
    elif (info.Map[Position[0]][Position[1]] == 0):# om den nya positionen inte är i en vägg så updateras objektets position
        print("yes\n \n \n \n")# detta gör det enklarare att se att det inte var en vägg
        pos.change(Entity,Position)
        return True# ger tillbaka true
    elif info.Map[Position[0]][Position[1]]!=0:# annars om den gick in i en vägg så ändras inte värderna
        print("\n \n \n \n VÄGG")
        print(info.Map[Position[0]][Position[1]])
        return False

while (info.master==True):#så länge inte användaren vill avsluta så körs while loopen
    if info.game==True:#om spelet har startas så körs satsen
        if loop <0:#loop är endast mindre än noll när man har genererat ett nytt rum 
            print("refresh")
            pos = position(draw.init())#updaterar pos med nya värden 
        loop+=1#höjer variabeln loop med 1 för varje varv av loopen
        if keyboard.is_pressed(info.controls["controls"]["Pause"]) and info.menu_up== False:#om den pause tangenten trycks och menyn inte är uppen
            draw.menu()#se draw modulen
        step = [0,0]# en steg list med x-kordinater,y-kordinater
        try:  # testar följande kod så att man inte får en emassa error när användaren trycker på en annan knapp
            #de föjade 4 satserna bestämmer i vilken rikning spelren vill gå och ändrar därefter steg kordinaterna
            if keyboard.is_pressed(info.controls["controls"]["Right"]):
                step[0]+=1
                print("d")
                prevpress = True# prevpress ändras

            if keyboard.is_pressed(info.controls["controls"]["Left"]):
                step[0]-=1
                print("a")
                prevpress = True
                
            if keyboard.is_pressed(info.controls["controls"]["Forward"]):
                step[1]-=1
                prevpress = True
                    
            if keyboard.is_pressed(info.controls["controls"]["Backward"]):
                step[1]+=1
                prevpress = True
            if keyboard.is_pressed(info.controls["controls"]["Interact"]):# interact knappen kallar på radar funktionen 
                print("E")
                if radar(pos.player,False,True)== True:# om det fanns en dörr inom range så laddas det in ett nytt rum
                    info.loadroom=True
                    draw.game()
            if keyboard.is_pressed(info.controls["controls"]["Attack"]):# om attak tangenten trycks så attackerar spelaren
                radar(pos.player,True,True)
        except:# om det skulle bli ett error från föregånde satser så printas det ut ett fel medelande
            print("key not assigned")# error för fel tangent är vanligast
        time.sleep(0.1)# programmet väntar för att undvika att man går tusen steg på ett knapp tryck    
        if prevpress == True:# den här satsen körs endast när en tangent har trycks
            #annars skulle dessa funktioner köras i onödan och få programmet att köra lite segare
            prevpress = False# resetar variabeln så attsatsen endast körs en gång efter att man har tryckt
            if wallhit(True, pos.player,step)== True:# kollar så att spelaren inte försöker gå in i väggen
                print("moving")
                draw.move(step,True)# om den inte gjorde det så flyytas den grafiska spelar positionen
        if info.spawn==True and loop ==5:# om svårigheten är högre än easy och loopen har körts fem gånger
            #eftersom denhär endast körs var femte gång så resulterar det i att spöket går fem gånger saktare
            loop = 0#variabeln resetas 
            moveghost()#kallar på moveghost funktionen
    try:# försöker updatera eftersom det blir error om man har stängt ned rutan
        C.update()# updatrar canvas utfifall vi gjorde någon ändring
    except:# om det inte funkar så är rutan nere och då bryts loopen
        print("game over")
        info.master = False
try:# här är det ett try för samma anledning
    master.destroy()#förstör allt som låg på master
    master.mainloop()#mianloop indikerar för programmet att den har ritat färdigt
except:
    print("end")
 
# fix list
# attack sytemet som  är relativt buggatd
