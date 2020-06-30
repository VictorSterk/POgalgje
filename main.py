print ('je hebt 5 beurten om het juiste woord te raden')
import random
Woordlijst = ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk' ]
GeheimWoord = Woordlijst[random.randrange(0, len(Woordlijst))]
GeradenLetters = []
beurten = 5

def renderWoord():
        for a in range(len(GeheimWoord)):
            if GeheimWoord[a] in GeradenLetters:
                print(GeheimWoord[a], '', end='')
            else:
                print('?', end='')
        print('')
        print('-' * len(GeheimWoord))

renderWoord()

while True:
    letter = input('raad een letter of het hele woord  ')
    if len(letter) == 1:
            renderWoord()

            GeradenLetters += letter
            if letter in GeheimWoord:
                print('Die letter zit in het woord')
                if checkWin():
                renderWoord()
                if checkWin():
                    print('Je hebt alle letters geraden')
                    print('Het woord was: ' + GeheimWoord)
                    break

 else:
    GeradenLetters += letter
    if letter in GeheimWoord:
                print('Die letter zit in het woord')
                renderWoord()

   else:
      print('Die letter zit niet in het woord')
                print('-1')
                beurten -= 1
                renderWoord()

