from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.messagebox import showwarning
from random import randint
from tkinter import simpledialog

def Generationmot(fichiermots):
    global Lmot,Ljoueur,chances,ldonnees,svj,svc,mot
    fichier=open(fichiermots,'r')    #recuperation des mots du fichier
    lignes=fichier.readlines()
    fichier.close()  
    
    mot=randint(0,len(lignes)-1)     #choix aléatoire du mot
    mot=lignes[mot]            
    Lmot=[]                         #création de la liste contenant chaque lettre du mot
    for i in mot:
        Lmot.append(i)              
    Lmot=Lmot[:-1]                  #enleve le /n
    
    Ljoueur=[Lmot[0]]               #création de la liste que l'on veut afficher pour le jeu
    for i in range (1,len(Lmot)):
        Ljoueur.append('_')
    motjoueur=""
    for i in Ljoueur:
        motjoueur=motjoueur+i+" "
        
    ldonnees=[]                     #création de la liste des lettres déjà sasies par le joueur

    chances=8
      
    svj.set(motjoueur)          #redonne un mot pour une nouvelle partie
    Canevas.delete("all")       #efface le canevas avant chaque nouvelle partie 
    Champ.delete(0,END)         #efface le champ de saisie avant chaque nouvelle partie

def Pendu(): 
    global Lmot,Ljoueur,chances,ldonnees
    if not saisirlettre(): #appel de la fonction pour saisir la lettre
        showwarning('Attention!','La lettre entrée a déjà été donnée.\nVeuillez recommencez!')    #creation d'une fenetre pop-up qui annonce que la lettre à deja eté donnée
        return
    ldonnees.append(lettre)
    lettreinmot() #appel de la fonction pour tester si la lettre est dans le mot ou non
    testfin() #appel de la fonction pour tester si le jeu est fini ou non
    Affichage()

def saisirlettre():
    global ldonnees,lettre
    lettre=Lettre.get()      
    return lettre not in ldonnees
        
def lettreinmot():
    global Lmot,Ljoueur,chances,lettre
    cpt=0
    for i in range(1,len(Lmot)):  #test pour verifier si la lettre est dans le mot
        if lettre==Lmot[i]:
            cpt=1
            Ljoueur[i]=lettre    #affiche la lettre à la place d'un - du mot
    if cpt==0:
        chances=chances-1

def testfin():
    global Lmot,Ljoueur,chances,mot
    test=True
    if Lmot==Ljoueur:                   #le jeu s'arrete et l'utilisateur a trouvé toutes les lettres du mot
        showinfo(mot,"Vous avez gagné!")  #affiche au joueur qu'il a ggné
        test=False
    if chances==-1:                   #le jeu s'arrete le joueur a utilisé toutes ses chances
        showinfo(mot,"Vous avez perdu!")      #affiche au joueur qu'il a perdu  
        test=False
    if not(test):
        if chances!=-1:
            score()                 #propose au joeur d'entrer son nom d'utilisateur pour sauvegarder son score
        rejouer()                   #propose au joueur de refaire une partie


def Affichage():
    global Ljoueur,chances,strvar
    motjoueur=""
    for i in Ljoueur:
        motjoueur=motjoueur+i+" "
    svj.set(motjoueur)
    if chances<=7:
        Canevas.create_line(20,180,120,180)      #creation du pendu qui augmente plus le nombre de chances diminue
    if chances<=6:
        Canevas.create_line(70,180,70,20)
    if chances<=5:
        Canevas.create_line(70,20,150,20)
    if chances<=4:
        Canevas.create_line(70,60,110,20)
    if chances<=3:
        Canevas.create_line(150,20,150,50)
    if chances<=2:
        Canevas.create_oval(140,50,160,70)
    if chances<=1:
        Canevas.create_line(150,70,150,105)
    if chances<=0:
        Canevas.create_line(150,70,135,85)
        Canevas.create_line(150,70,165,85)
    Canevas.update()                   #rafraichit le canevas
    

def rejouer():
    global svj
    result = messagebox.askyesno("Rejouer", "Voulez-vous rejouer?", icon='info')   #propose au joueur de rejouer
    if result:
        svj.set("")               #recréation du mot avec que la 1ere lettre apparente pour permettre au joueur de rejouer
        Generationmot('mots.txt') #
    else:
        Mafenetre.destroy()       #detruit la fenetre quand l'utilisateur ne veut pas jouer
        
def score():
    global chances
    bestscore=open('scores.txt','a+')
    identifiant=simpledialog.askstring("Meilleurs Scores","Entrez votre identifiant")  #création d'une fenetre pop-up pour que le joueur rentre son identifiant
    score=identifiant+":"+str(chances)+"\n"         #calcul du nb de points
    bestscore.write(score)               #écrit les données sur le fichier
    print('Le meilleur score est :',recuperer('scores.txt'))

def recuperer(fichier):
    fichier=open(fichier,'r')
    lignes=fichier.readlines()
    fichier.close()
    best=0
    for i in range(0,len(lignes)):
        a,b=lignes[i].split(':')
        b=int(b)
        if b>best:
            best=b
    return best
        

#Generationmot('mots.txt')

global Lmot,Ljoueur,chances,ldonnees,lettre

Mafenetre = Tk()           #creation de la fenetre principale
Mafenetre.title("Jeu du pendu")
L=200
H=200
Canevas=Canvas(Mafenetre, width=L, height=H)  #création d'un widget Canvas (zone graphique)
Canevas.pack(padx=5,pady=5)
svj = StringVar()
svj.set("")
Label1=Label(Mafenetre,textvariable=svj)         #creation d'un label pour afficher le mot (sous forme de tiret) du joueur
Label1.pack(padx=10,pady=10)

Proposer=Button(Mafenetre, text="Proposer", command= Pendu)
Proposer.pack(side=LEFT, padx=10, pady=10)         #creation du bouton proposer qui lance le pendu

menubar=Menu(Mafenetre)
menujeu=Menu(menubar,tearoff=0)
menujeu.add_command(label="Recommencer",command= lambda:Generationmot('mots.txt'))
menujeu.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Jeu", menu=menujeu)     #creation du menu qui propose de recommencer ou quitter la partie

Lettre=StringVar()
Champ=Entry(Mafenetre,textvariable=Lettre) #création du champ de saisie pour rentrer les lettres
Champ.focus_set()
Champ.pack(side=LEFT,padx=10,pady=10)

Mafenetre.config(menu=menubar)   #affichage du menu
Generationmot('mots.txt')       
Mafenetre.mainloop()
