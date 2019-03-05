print("hur många barn vill ha ...")
korv2 = int(input(" 2 vanliga korvar>"))
korv3 = int(input(" 3 vanliga korvar>"))
vKorv2 = int(input(" 2 veganskaa korvar>"))
vKorv3 = int(input(" 3 veganska korvar>"))
print("inköp")
antal_korv = round((korv2*2)+(korv3*3)+3)/8#räknar yt mägden korvar
antal_vKorv = round((vKorv2*2)+(vKorv3*3)+1)/4
kf = str(antal_korv)
vkf = str(antal_vKorv) 
Dricka = str(korv2 + korv3 + vKorv2 + vKorv3)#räknar ut mägden drickor
print("Vanlig Korv: "+kf+" förpackningar")
print("Veganska Korvar: "+vkf+" förpackningar")
print( "Drickor:    "+Dricka)
pris =(round(float(Dricka)*13.95)+round(float(antal_korv)*20.95)+round(float(antal_vKorv)*34.95))# räknar ut det totala priset
print(pris)
