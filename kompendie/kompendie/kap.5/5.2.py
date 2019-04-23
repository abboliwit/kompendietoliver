tabell = [[1,14],[2,13],[3,12],[4,11.5],[5,11],[7,10.5],[8,10],[11,9.5],[12,9],[16,8.5],[8]]# en array med de värden som är intressanta  i tabellen 
namn = str(input("Ange ditt namn : "))
ålder = int(input("Ange din ålder : "))

Bignamn = namn.capitalize()
sleeptime = 0
found = False
for sleep in tabell: #en for loop som kollar din ålder jämfört med sov listen
    if ålder ==sleep[0]:
        sleeptime =sleep[1]
        found = True
        break
    elif ålder > tabell[4][0] and ålder < tabell[5][0]:
        sleeptime =tabell[4][-1]
        found = True
        break
    elif ålder > tabell[6][0] and ålder < tabell[7][0] :
        sleeptime = tabell[6][-1]
        found = True
        break
    elif ålder > tabell[-3][0] and ålder < tabell[-2][0] :
        sleeptime = tabell[-3][-1]
        found = True
        break

if found == False and ålder > tabell[-2][0]:# om åldern inte hittas i tabellen så kommer hen att behöva sova i 8 timmar
    sleeptime = tabell[-1][0]
print("Hej "+ Bignamn + "!\n Enligt Vårguidens rekomendationer behöver individer i din ålder("+ str(ålder) +" år)\n  sova minst "+ str(sleeptime)+ " timmar per natt") 
    



    

