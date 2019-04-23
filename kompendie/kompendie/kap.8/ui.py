def line(dots =False):# dots är alltid false om inte det kommer in ett annat argument
    if(dots==True):
        print("******************************")# om dots blir true kommer 30st *
    else:
        print("------------------------------")#annars kommer 30st -


def Header(mess):#mess är medalandet som man vill skriva ut
    width = 28# min width är 30 och om man tar bort pipsen från sidorna blir längden 28
    center = ""#en string som bara ska bestå av mellanslag
    length = int((width-len(mess))/2)# en ekvation som beräknar hur långt det kommer vara till varje sida allstå ängden mellanslag
    for space in range(length):# en for loop som gör center stringen tillräckligt lång
        center+=" "
    print("|"+center+mess+center+"|")# printar ut den centrerade texten

def Echo(mess):# mess är medeladet som man vill skriva ut
    print("| "+mess)# skriver ut medelandet med en pipe

def promt(mess):
    answer = input("| "+mess+" >")# tar medeandet och skriver ut det i en input funktion
    return answer# ger tillbaka inputet

def clear():
    empty ="\n"*1000# clear printar 1000 nya rader 
    print(empty)