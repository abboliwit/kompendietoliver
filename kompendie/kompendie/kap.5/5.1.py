class person:# en klass som sorterar varje kändis utseende
    def __init__(self,name,gender, hair, eye):
        self.name = name
        self.gender = gender
        self.hair = hair
        self.eye = eye
 
kön = str(input("Ange Kön:"))
hår = str(input("Ange Hårfärg:"))
öga = str(input("Ange Ögonfärg:"))

kändis1= person("Daniel Radcliffe","man","brun","brun")# varje kändis utseende
kändis2 = person("Rupert Grint","man","röd","blå")
kändis3 = person("Emma Watson","kvinna","brun","brun")
kändis4 = person("Selena Gomez","kvinna","brun","brun")

plist = [kändis1,kändis2,kändis3,kändis4]# en lista på hur många kändisar det finns

for individ in plist:
    if individ.gender  == kön and individ.hair == hår and individ.eye == öga:# kollar om användarens utssende matchar någon kändis
        print(individ.name)
        match = True

if match == False:
    print("tyvärr ingen matchning")# om utseendet inte gör det så får hen ett medelande




