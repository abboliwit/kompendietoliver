import keyboard # ett library som upptäcker när man trycker på en tangent
import time
number = int(input("ange ett nummer att multiplicera>\n"))# tar in ett nummer
x=1
y=0
while True:#en loop som alltid görs
    while y < 3:# en loop som multiplicerar det valda talet 3 gånger 
        print(number*x)
        y+=1
        x+=1
        if y ==3:
            print("fortsätta Y/N")#printas efter alla de andra talen
    time.sleep(0.2)# en liten delay som hindrar att det bara spammar ut nummer        
    if keyboard.is_pressed('Y'):# om man trycker y så kommer y värdet sättas till noll så man kan multiplicera igen
        y=0
    elif keyboard.is_pressed('N'):# om man trycker n så bryter man ur loopen
        break

    
    
    
