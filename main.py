print ('je hebt 5 beurten om het juiste woord te raden')
import random
Woordlijst = ['informatica', 'informatiekunde', 'spelletje', 'aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit', 'verzekering', 'universiteit', 'heesterperk' ]
GeheimWoord = Woordlijst[random.randrange(0, len(Woordlijst))]
GeradenLetters = []

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
