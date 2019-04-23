def miles_to_km(dist):
    return str(dist*1.609344)+"km"# funktionen ger tillbaka km genom en ekvation och talet är hur många km som det går på en mile

def km_to_miles(dist):
    return str(dist/1.609344)+"miles"# den här funktionen bestämmer hur många miles det är
distance = input("Distance to convert: ")
if("miles" in distance):
    length = miles_to_km(float(distance.strip("miles")))# if satsen bestämmer om det är miles som sätts in sedan tar den bort miles ur stringen så att man får ett rent nummer sedan skickas nummret till funktionen som ger till baka allt som en string
if("km" in distance):
    length = km_to_miles(float(distance.strip("km")))# if satsen bestämmer om det är km och tar också bort km ur stringen så att men fär ett rent nummer i stringen och sedan skickas nummret till funktionen som ger till baka allt som en string

print(distance+" är "+length) #printar resultatet    