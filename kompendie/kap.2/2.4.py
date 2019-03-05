print("hur gammal är du")
ålder = int(input(">"))
myndig = 18 - ålder

if ålder < 18:# om du är under 18 så printar den utan hår långt det är kvar till 18
    variabel = str(myndig)
    print(" du är myndig om " +variabel+  " år")
else:
    myndig = myndig * (-1)# om du är över 18 så printar den hur länge du har varit 18
    variabel = str(myndig)
    print("du har varit myndig i "+ variabel+" år")