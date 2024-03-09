import time
import os
from subprocess  import call
def Say(msg, no=''):
    for lettre in msg :
        print(lettre,end='',flush=True)
        time.sleep(0.06)
    for lettre in no :
        print(lettre , end='', flush = True)
        time.sleep(0.09)
    print("\n")

def clear():
    os.system("cls")


def SayR(msg):
    for lettre in msg :
        print(lettre,end='',flush=True)
        time.sleep(0.04)
    print("\n")

def SayS(msg):
    for lettre in msg :
        print(lettre,end='',flush=True)
        time.sleep(0.13)
    print("\n")

def save() :
   list = [
       name,
       str(hp),
       str(Lv)
   ]

   f = open("save.txt","w+")
   for item in list :
       f.write(item + "\n")
   f.close()

def prendre_potion():
    global hp, Lv
    hp = 1
    Say(".......")
    clear()
    print(name, "\n")
    time.sleep(0.3)
    print("hp = \n", hp)
    time.sleep(0.3)
    print("Level : \n", Lv)
    Say("...")

def refuser_potion():
    global hp
    Say("fluffy : on t'as pas appris la politesse quand on t'offre quelque chose TU ACCEPTE")
    input("> \n")
    rep = input("1 : prendre \n2 : Refuser \n")
    if rep == '1':
      prendre_potion()
    elif rep == '2':
        Say("fluffy : d'accord ... tu as raison de pas prendre....je vois tu connais déjà comment ça se passe ici")
        input("> \n")
        Say("fluffy : ALORS JE VAIS T'ATTAQUER DE MOI MÊME")
        # Insérer la suite du code pour l'attaque

def print_list_steps(art_list, delay):
    for row in art_list:
        print(row)
        time.sleep(delay)

ascii_art = [
    " ____             ___    _          _ ",
    "|  _ \\  _____   _|_ _|__| | ___  __| |",
    "| | | |/ _ \\ \\ / /| |/ _` |/ _ \\/ _` |",
    "| |_| |  __/\\ V / | | (_| |  __/ (_| |",
    "|____/ \\___| \\_/ |___\\__,_|\\___|\\__,_|"
]

hp = 20
Lv=1
run = True 
menu = True
play = False 
rules = False
while run :

 
 while menu :
    print_list_steps(ascii_art,0.35)
    print("\n\n")
    SayR(" 1 : new game")
    SayR(" 2 : Load Game")
    SayR(" 3 : rules")
    SayR(" 4 : exit ")
    while True :
        choix = input()
        if(choix == '1' or choix == '2' or choix == '3' or choix == '4') :
           break
    if choix == '1' :
        SayR("enter the name of ur hero")
        name = input() 
        play=True
        menu = False
    if(choix=='2') :
        f=open("save.txt","r")
        load_list=f.readline()
        name = load_list[0][:-1]
        hp = load_list[1][:-1]
        Lv = load_list[2][:-1]
        Say("welcome back ",name)
        input("> ")
        menu = False
        play=True
    if choix == '3' :
        rules=True
    if choix == '4' :
            quit()
    if rules :
        Say("les regle du jeu sont simple finissez le jeu en evitant de mourir sachez que vos choix sont décisif pour la suite de l'aventure")
 while play :
     clear()
     save() #auto save
     Say("Jadis, dans un monde divisé entre deux races - les humains et les monstres - les frontières étaient strictes ")
     Say("les humains ne pouvaient pas entrer dans le royaume des monstres et vice versa.")
     Say("Le royaume des monstres était un endroit sombre, régi par l'injustice et la tyrannie Après des années de tension, une guerre éclata entre les deux camps")
     Say("Finalement, les humains triomphèrent, scellant les monstres sous terre à l'aide d'un sortilège interdit.")
     Say("Des années de paix s'écoulèrent, mais des légendes persistaient, notamment autour d'une mystérieuse forêt.")
     Say("Les habitants du village affirmaient que cette forêt était hantée et que quiconque s'y aventurait n'en revenait jamais")
     time.sleep(1)
     SayS("...")
     clear()
     Say("cam :...",name)
     input()
     input("> ")
     Say("reveille t...")
     input("> ")
     Say("cam : reveille toi ! papa t'attend en bas ")
     print("\n 1 : ohh d'accord je me prépare j'arrive ! \n 2 : ohhhh cam t'abuse je dormais \n")
     rep=input()
     if (rep=='1') :
         Say("d'accord papa est préssé fait vite ")
     elif rep == '2' :
         SayR("cam : EYYY ! père est préssé il va pas arriver en retard a cause de toi")  
         input("> ") 
         Say(" vous : d'accord j'arrive je me prépare")
         input("> ")
         SayS("(ma soeur est très maniaque et déteste quand je suis en retard mais je l'aime)") 
     SayS("......")  
     clear()
     SayS("(après avoir rejoint mon père nous somme partie en expidition dans une foret nommé fort des mort)")
     #on peut ajouter une musique ou un son pour la scène suivante
     SayS("{après de longue heure de marche dans la foret le père et son fils se perdent de vue}")
    #hna ndiro tsawaer ou ndiro tswira ou le personagge principale yezle9 ou ytih f une grotte
     Say(name,"{ se reveille totalment boulversé par la situation}")
     input()
     Say(name," {trouve une porte}")
    #li ma bin { } ta3 narrateur () fi 9elbo le reste dialogue
     print("\n 1 : ouvrir la porte et entrer \n 2 : non trop risqué \n")
     rep=input()
     if(rep=='2'):
        SayS("(je n'ai pas d'autre solution c'est la seul issue posible)")
        #nwro tswira beli tah ml fooo9 ga3 ou la sortie b3ida innacecible 
        SayS("....")
     clear()
     Say("{en entrant dans la salle il trouve une personne}")
     print("\n 1 : lui parler \n 2 : non je ne parle pas au innconu \n")
     rep=input()
     if(rep=='1') :
      Say(name ,":  Bon.... bonjour, vous savez on est ou ?")
     elif (rep=='2') :
         Say("(j'essaie de passer discrétment sans me faire reperer)")
         Say("??? : eyyyy toi la-bas vien ici")
     input("> ")
     Say("??? : ahhh t'es un nouveau ici je ne t'ai jamais vu je me présente moi c'est fluffy")
     input("> ")
     Say("fluffy : quelqu'un doit t'apprendre comment ça marche ici ")
     input("> ")
     Say("fluffy : tu a ce qu'on apelle les Hp eh bah c'est t'as santé il faut prendre soin de toi \n regarde ton nombre d'hp :", " 20")
     input("> ")
     Say("fluffy : il y'as aussi ce qu'on appelle le Level mais aussi ta progression")
     input("> ")
     SayS("...")
     clear()
     Say("fluffy : maintenant que tu en sais beaucoup plus je t'invite a prendre ça c'est une potion ça t'aidera pour la suite")
     rep=input("1 : prendre \n2 : Refuser \n")
     if(rep=='1') :
      prendre_potion()    
     elif (rep=='2') :
         refuser_potion()
        #tswira ou il se fait attaquer
     Say("fluffy : ... HAHAHAHAHAHAHAHAHAHAH imbécile ")
     Say("fluffy : DANS CE MONDE C'EST TUER OU ETRE TUER")
     Say("fluffy : MEURS HAHAHAHAHA")
     #dir son ta3 dahka demoniaque
     Say("{vous tombez dans les vape....}")
     save() #auto save
     SayS("....")
     clear()
     input("> ")
     Say("???? : t'es enfin reveiller ?")
     Say("???? : je comprend t'es perdu un peu , moi c'est jane et toi ?")
     print("1: dire son prénom \n2: refuser de donner son prénom")
     rep=input()
     if(rep=="1"):
         Say("jane : je comprend...")
     elif (rep=='2') : 
         Say("jane : ohhh donc ton prénom c'est",name);
         Say("jane : très joli prénom")
     input("> ")
     clear()
     Say("jane : disons que tu es tombé dans une forêt magique")
     Say("jane : pour sortir il te faut trouver 3 artéfact " )
     Say("jane : 1. La Pierre d'Esprit\n2. Le Collier de Feu\n3. L'Élixir du Temps")
     input("> ")
     Say("jane : la personne malvaillante que  tu a croiser tout a l'heure possedait un artéfact Le collier du feu !")
     input("> ")
     print("\n1: et les autres détenteur d'artéfact tu les connais ?\n2: je veut partir a leurs recherche")
     rep=input()
     if(rep=='1') :
        Say("jane : celui qui détient l'élixir du temp s'apelle Midas")
        Say("et la détenteuse de la pièrre de l'esprit... je ne la connais pas")
        Say("(elle semble mentir elle doit la connaitre)")
     elif(rep=='2') :
         Say("jane : ohhh tu ne perd pas de temp !") 
     Say("jane : je te conseille rester ici récuperer je revien plus tard...")
     Say("{jane qui sors de la pièce}")
     Say("(je dois partir de la )")
     input("> ")
     Say("(j'entend des bruit de pas c'est surement jane qui revient)")
     print("1: me cacher sous le lit \n2: attendre paisiblement jane \n")
     rep = input()
     SayS("...")
     clear()
     if(rep=='1') :
         Say("jane : humain ! ou te cache tu ? je ne te veut aucun Mal")
         Say("{jane qui vérifie sous le lit}")
         Say("jane : ahh tu est la ne t'inquète pas je ne suis pas comme l'autre")
     elif (rep=='2') : 
         Say("jane : ah t'es toujour la ! ")
     Say("jane : je vais te dire un secret")
     Say("jane : je suis ce qu'on apelle une sainte")
     Say("jane : il y'en a plein comme moi tu peut leurs faire confiance elle peuvent réstaurer t'es point de vie")
     hp=20
     Say("jane : regarde.....")
     Say("je me sens beaucoup mieux")
     print("hp=",hp)
     Say(name,": merci beaucoup")
     Say("jane : si tu veut rester ici tu sera toujour le bienvenue")
     print("\n1: non désolé je dois retrouver mon père \n2: ne pas répondre \n")
     rep = input()
     if(rep=='1'): 
         Say("jane : bien alors bonne chance pour ton expidition j'espère que tu arrivera a retrouver ton père")
     elif (rep=='2') :
         Say("jane : je comprend...bon je te souhaite bonne chance !")
     input("> ")
     SayS(".....")
     clear()
     Say("(je vais découvrir ce monde mais je dois chercher les artéfact pour retrouver mon père et ma famille)")
     clear()
     print_list_steps(ascii_art,0.4)
     SayS("...")
     call(["python","game_mid.py"])
