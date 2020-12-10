from random import *

fichier = open('mots.txt','r')
Lmot=(fichier.readlines())
mot=(choice(Lmot)).strip()

chances = 8
affichage = ""
lettres_trouvees = ""

for i in mot:
    affichage = affichage + "_ "

while chances>0:
    print("Mot à deviner : ", affichage)  #affiche le mot à deviner
    proposition = input("proposez une lettre : ")

    if proposition in mot:
        lettres_trouvees = lettres_trouvees + proposition
        print("Oui")
    else:
        chances = chances - 1
        print("Non, il vous reste", chances, "chances")

    affichage=""
    for x in mot:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    if "_" not in affichage:
        print("Gagné!")

print("Perdu!")
