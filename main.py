print('je hebt 5 beurten om het juiste woord te raden')
import random
WoordLijst = ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk']
GeheimWoord = WoordLijst[random.randrange(0, len(WoordLijst))]
GeradenLetters = []
beurten = 5

def checkWin():
    for i in range(len(GeheimWoord)):
        if not GeheimWoord[i] in GeradenLetters:
            return(False)
    return(True)

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('? ', end='')
        print('')
        print('-' * len(GeheimWoord))

renderWoord()

while True:
    letter = input('raad een letter of het woord  ')
    if len(letter) == 1:
        if letter in GeradenLetters:
            print('Die letter had je al geraden')
            renderWoord()
        else:
            GeradenLetters += letter
            if letter in GeheimWoord:
                print('Die letter zit wel in het woord')
                renderWoord()
                if checkWin():
                    print('Je hebt alle letters geraden')
                    print('Het woord was: ' + GeheimWoord)
                    break
            else:
                print('Die letter zit niet in het woord')
                print('-1')
                beurten -= 1
                renderWoord()
    elif letter == GeheimWoord:
        print('Je hebt het woord geraden')
        break
    else:
        print('Fout woord!')
        print('-2')
        beurten -= 2
        renderWoord()
    if beurten <= 0:
        print('Je hebt verloren! Het woord was ' + GeheimWoord)
        break
    print('Je hebt nog', beurten, 'beurten over.')
