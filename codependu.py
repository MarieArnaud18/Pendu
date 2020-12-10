from random import *

Listemots = [] #initialistation de la liste de mots
Listemots.append("maison")
Listemots.append("table")
Listemots.append("escargot")
Listemots.append("fleur")
Listemots.append("ordinateur")

def ChoixMot(Listemots): #choix random d'un mot dans la liste
    Mot=random.choice(Listemots) 
    return Mot

def AffichageMot(Mot,LettresTrouvees):
    a = ""
    for i, L in enumerate(Mot): 
        if i==0 or L in LettresTrouvees: #afficher la première lettre ainsi que les autres lettres trouvées
            a+=L
        else: #afficher _ pour les lettres non trouvees
            a+=" _"
    x.set(a)
    return a

def Gagne(Mot,LettresTrouvees):
    i=0
    for l in Mot:
        if l in LettresTrouvees: #ajouter 1 au compteur si la lettre du mot est dans la liste de lettres trouvees
            i+=1
    if i==len(Mot): #si le nombre de lettres trouvees est égal à la longueur du mot retourner True
        return True

def AffichagePendu():
    global nbchance
    if nbchance==6:
        item = Canevas.create_image(150,150,image=image2)
    if nbchance==5:
        item = Canevas.create_image(150,150,image=image3)
    if nbchance==4:
        item = Canevas.create_image(150,150,image=image4)
    if nbchance==3:
        item = Canevas.create_image(150,150,image=image5)
    if nbchance==2:
        item = Canevas.create_image(150,150,image=image6)
    if nbchance==1:
        item = Canevas.create_image(150,150,image=image7)
    if nbchance==0:
        item = Canevas.create_image(150,150,image=image8)      


def AffichLettresFausses(LettresFausses):
    A=""
    for i in LettresFausses:
        A+=i
        A+=" "
    List.set("Lettres fausses : "+A)
    return A


def Verif():
    global LettresTrouvees,LettresFausses,Mot,nbchance
    l=Lettre.get()
    Lettre.set('')
    if l in LettresTrouvees or l in LettresFausses: #si la lettre a déja été donnée
        info.set("Vous avez déjà donné cette lettre")
    elif l in Mot: #si la lettre est dans le mot
        LettresTrouvees.append(l)#on ajoute la lettre à la liste de lettres trouvees
        AffichageMot(Mot,LettresTrouvees)#afficher le mot avec la nouvelle lettre trouvee
        info.set("Continuez, il manque encore des lettres")
    else :
        nbchance=nbchance-1 #enlever une chance à l'utilisateur
        LettresFausses.append(l) #ajout de la lettre dans la liste de lettres fausses
        AffichagePendu()
        compt1.set("Nombre de coups restants: "+str(nbchance))
        info.set("Aîe, c'est raté! Fais attention la prochaine fois")
        AffichLettresFausses(LettresFausses) #On actualise la liste de lettres fausses


def Pendu():
    global Mot,LettresTrouvees,LettresFausses,nbchance
    AffichageMot(Mot,LettresTrouvees) #Affichage du mot avec les lettres trouvées
    if nbchance>0:#tant que le joueur n'a pas épuisé ses chances
        Verif()
        if Gagne(Mot,LettresTrouvees)==True: #si l'utilisateur a donné toutes les bonnes lettres
            info.set("Vous avez gagné ;-)")
    if nbchance==0 and Gagne(Mot,LettresTrouvees)!=True : #si il manque des bonnes lettres et que le nombre de chance est épuisé
        info.set("Vous avez perdu :-(")

def Rejouer():
    global Mot,LettresTrouvees,LettresFausses,nbchance
    Mot=ChoixMot(Listemots) #On choisit un nouveau mot
    LettresTrouvees=[Mot[0]]#réinitialistation de la liste de lettres trouvees
    LettresFausses=[]
    nbchance = 7 #On redonne toutes les vies
    Pendu()
    return Mot,LettresTrouvees,LettresFausses,nbchance


#Création de la fenêtre principale
Mafenetre=Tk()
Mafenetre.title('jeu du pendu')

image1=PhotoImage(master=Mafenetre, file='bonhomme1.gif')
image2=PhotoImage(master=Mafenetre, file='bonhomme2.gif')
image3=PhotoImage(master=Mafenetre, file='bonhomme3.gif')
image4=PhotoImage(master=Mafenetre, file='bonhomme4.gif')
image5=PhotoImage(master=Mafenetre, file='bonhomme5.gif')
image6=PhotoImage(master=Mafenetre, file='bonhomme6.gif')
image7=PhotoImage(master=Mafenetre, file='bonhomme7.gif')
image8=PhotoImage(master=Mafenetre, file='bonhomme8.gif')

#Création du Canvas
Largeur=300
Hauteur=300
Canevas=Canvas(Mafenetre, height= Hauteur, width=Largeur,bg='white')
item = Canevas.create_image(150,150,image=image1)

#Création entry
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)

#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer',command = Pendu)

#Création du bouton rejouer
BoutonRejouer=Button(Mafenetre,text='Rejouer',command=Rejouer)

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création label du mot recherché
x=StringVar()
x.set(AffichageMot(Mot,LettresTrouvees))
LabelMotRech=Label(Mafenetre,textvariable=x,fg='black',bg='white')

#Création label nb de coups restants
compt1=StringVar()
compt1.set("Nombre de coups restants: "+str(nbchance))
LabelCoup=Label(Mafenetre,textvariable=compt1,fg='black',bg='white')

#Création label lettres fausses
List=StringVar()
LabelLettresFausses=Label(Mafenetre,textvariable=List,fg='black',bg='white')

info=StringVar()
console=Label(Mafenetre, textvariable=info, fg='black', bg='white')

#Mise en page
LabelCoup.grid(row=1,sticky=NE)
LabelMotRech.grid(row=2)
BoutonEntry.grid(row=3)
BoutonProposer.grid(row=4)
BoutonRejouer.grid(row=5)
BoutonQuitter.grid(row=6)
LabelLettresFausses.grid(row=7)
Canevas.grid(row=1,column=2,rowspan=6)
console.grid(row=7, column=2)

Rejouer()

Mot=Rejouer()[0]
LettresTrouvees=Rejouer()[1]
LettresFausses=Rejouer()[2]
nbchance=Rejouer()[3]

Mafenetre.mainloop()