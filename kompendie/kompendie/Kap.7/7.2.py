from random import randint
print('Hello please enter the parameters for the game HIGHER LOWER to start')
low = int(input("Lowest possible number: "))
high = int(input("Highest possible number: "))
print("\nOK now guess wich number between those above that i picked :)")
answer = randint(low,high)# tar en slump värde mellan parametrarna som man har valt
Try = 0# antalet försök
guess = False# variabel för om man har gissat rätt
while(guess == False):# så länge man inte har gissat rätt så körs loopen
    Try+= 1# vi börjar med att lägga till på försöks variabeln eftersom man inte kan göra noll försök
    number = int(input("\ntry number "+str(Try)+": "))#printar hur många gåner man har försökt men tr också in en ny gissning
    if (number==answer):
        print("corect you took "+str(Try)+" tries")# om svaret är rätt så ptitas det ut en grattis rad
        guess = True# stänger av loopen eftersom man gissade rätt
    elif(number<answer):
        print("The answer is HIGHER")# om man gissade på ett längre nummer så talar datorn om att det är högre
    elif(number>answer):
        print("The answer is LOWER")#om man gissad på ett högre tal så säger programmet att svaret är lägre
