gb = ["england","wales",""]
norden = ["sverige","norge","finland","danmark","island"]
land = str(input("vilket land bor du i?"))
found = False
litleland = land.lower()#gör varje bokstav i stringen till små

if litleland in norden:
    print("du bor i Norden")
    found = True
elif litleland in gb:#kollar alla länder i storbritanien
    print("du bor i Strobritanien")
    found = True
if found == False:
    print("Du bor varken i Norden eller Storbritanien:(")#om landet inte hittas så kommer ett fel medelande
