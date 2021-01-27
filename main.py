
import random
WoordLijst = ["computer", "python", "stoel", "tafel", "jas", "deur", "gordijn", "tapijt", "bloem"]
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
levens = 10

#dit onderdeel kijkt of een letter al geraden is.
def gewonnen():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

#Dit onderdeel print de goeie letters uit zoals ##a##
def WihWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print("# ", end=" ")
        print(" ")
        print('_ ' * len(GeheimWoord))

WihWoord()
#
while True:
    letter = input("raad een letter of type het woord ")
    #Dit onderdeel checkt of een letter of woord goed is of al geraden is
    if len(letter) == 1:
        if letter in GeradenLetters:
            print("Die letter heb je al geraden")
            WihWoord()
        else:
            GeradenLetters += letter
            #Als het letter in het woord zit dan heeft de speler gewonnen
            if letter in GeheimWoord:
                print("Dat is goed! Die letter zit in het woord.")
                WihWoord()
                #Dit onderdeel checkt of alle letters zijn geraden met behulp van gewonnen() die een true of false aangeeft
                if gewonnen():
                    print("Alle letters zijn geraden! Je hebt gewonnen")
                    print("Het woord was: " + GeheimWoord)
                    break
            else:
                print("Dat is fout. Die letter zit niet in het woord")
                print("-1")
                levens -= 1
                WihWoord()
    #Als de player het goeie woord in typed dan heeft de speler gewonnen, zo niet dan gaan er 2 levens weg.
    elif letter == GeheimWoord:
        print("Het woord is geraden! Je hebt gewonnen")
        break
    else:
        print("Dat is niet het goeie woord")
        print('-2')
        levens -= 2
        WihWoord()
    #Dit checkt of de speler nog levens heeft.
    if levens <= 0:
        print("Jammer, je hebt verloren. Het woord was"+ GeheimWoord)
        break
    print("Je hebt nog" ,levens, "levens over")
print("Bedankt voor het spelen. Gemaakt door Sami Akazim uit 6-1vh3")