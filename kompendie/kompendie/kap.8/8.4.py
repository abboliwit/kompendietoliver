import web
import ui
Exit= False# en variabel som håller koll på om man vill fortsätta eller inte
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"# url:en till api:n

def selection():# gjorde en funktion som printar ut valen som man kan göra eftersom dom är samma
    ui.line()
    ui.Echo("L| list of artists")
    ui.Echo("V| view artist profile")
    ui.Echo("E| exit application")
    ui.line(True)
    select = ui.promt("selection")
    return select#funktionen ger tillbaka svaret som användaren ger

def title(mess):# gjorde också en title funktion eftersom den är samma men man kan andra själva headern med ett medelande
    ui.line()
    ui.Header(mess)# en header med valfri titel
    ui.line()

def List():# funktion för att skriva ut listan av artister 
    response = web.get(url)# url en hämtas varje gång eftersom id:et uppdateras
    for artist in response["artists"]:#printar alla artister
        ui.Echo(artist["name"])

def view():# en funktion som hämtar och skriver ut information om artisterna
    response = web.get(url)#url:en hämtas på nytt eftersom id:et uppdateras
    select = ui.promt("Artist to view").capitalize()# tar in vilket artist du vill ha och ger den storbokstav eftersom det är viktigt för api:n
    for artist in response["artists"]:# eb loop som kollar igenom varje artist i informationen och tar det id:et som stämmer överens
        if artist["name"] == select:
            Id = artist["id"]
            found = True
            break# for loopen bryts när id:et har hittats
    info= web.get(url+Id)# tar in ny info om just den artisten
    if (found == True):# om artist som man skrev in hittades så skrivs all information ut
        title(select)# kallar på funktion där medelandet är artisten som man skrev in
        ui.Echo("Members: "+str(info["artist"]["members"]))#information om alla medlemmar
        ui.Echo("Genres: "+str(info["artist"]["genres"]))# information om geners
        ui.Echo("Years Active: " + str(info["artist"]["years_active"]))# information om aktiva år
    else:
        ui.Echo(select+ "is not present in the database or/ misspelled")# om artisten som man begärde inte finns i data basen så får man upp ett error medelande 
    
title("ARTIST DB")# skriver upp titeln
ui.Echo("Welcome to a world of")# skriver ett medelande som bara skrivs en gång
ui.Echo("Music!")
while (Exit ==False):# en while loop som loopar programmet tills användaren stänger av
    answer= selection()# frågar användaren vad hen vill göra
    ui.clear()#rensar det som stod ovan
    title("ARTIST DB")# skriver titeln igen
    if (answer.lower()== "e"):# om man vill avsluta så rensas consolen och programmet stängs av eftersom exit kriteriet inte längre stämmer
        ui.clear()
        Exit= True
    elif (answer.lower()== "l"):# om man vill se listan av artister så kallar programmet på den funktionen
        List()
    elif(answer.lower()=="v"):# om man vill se en speciell artist så kallar programmet på den funktionen
        view()