import random
#numpy pour une belle grille
#lister une range list(range)
#on ne peut pas iterer avec des nested liste
#00 ne pouvant etre créer en int, j'ai testé un float 0.0 mais on peut pas iterer avec un float
#creation d'un 38eme choix qui sera retourner en 00
#cant global raw_input
#iterate throught every possibilities puis choix de bille
#JAI OUBLIER LE QUADRUPLE CHOICE
#on oublie les choix avec chevauchement sur la version cli
    
values = ["00", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24 , 25 , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, "ODD", "EVEN", "1st 12",
       "2nd 12", "3rd 12", "1 to 18", "19 to 36", "BLACK", "RED", "1 - 2 to 1", "2 - 2 to 1", "3 - 2 to 1"]

mise = {}

compte = 1000

possibilite = len(values)

def grid():
    grid1 = [list(range(3,37,3)), "2 to 1"]
    grid2 = [list(range(2,37,3)), "2 to 1"]
    grid3 = [list(range(1,37,3)), "2 to 1"]
    grid4 = "1st 12" + "                 " + "2nd 12" + "                      " + "3rd 12"
    grid5 = ["1 to 18", "EVEN", "RED", "BLACK", "ODD", "19 to 36"]
    
    print(grid1)
    print(grid2)
    print(grid3)
    print(grid4)
    print(grid5)


def selection():
    print("votre compte :",compte)
    grid()
    print("mise actuel", mise)
    run = True
    while run:
        if compte == 0:
            print("vous n'avez plus d'argent")
            run = False
            
        jetons = input("faites vos jeux (0 to quit): ")
        jetons = int(jetons)
		
        if jetons > compte:
            print("fond insuffisant.")
            
        if jetons < 0:
            print("mise impossible.")
            
        if jetons == 0:
            selection()
            
        if jetons in range(compte):
            print("mise ", jetons)
            for elem in range(len(values)):
                print(elem, values(elem))
            selection.choix = raw_input("choix : ")
            if choix in range(len(values)):
                mise[choix] = jetons
            else:
                selection()
        
def gain_plein(n):
    return 36 * n

def gain_simple(n):
     return 2 * n
    #douzaine = simple

def perte(a,b):
    return a - b
    
def probalite():
    simples = ["00", "1st 12", "2nd 12", "3rd 12", "1 to 18", "19 to 36", "BLACK", "RED",
               "1 - 2 to 1", "2 - 2 to 1", "3 - 2 to 1"]
    chiffre = list(range(0,37))
    for num in chiffre:
        for elem in simples:
            for key in mise:
                if key == num:
                    compte = compte + gain_plein(mise[key])
                    
                if key % 2 == 0:
                    if num in range(1,19):
                        odd_r = "RED"
                        compte = compte + gain_simple(mise[key])
                    if num in range(19,37):
                        odd_b = "BLACK"
                        compte = compte + gain_simple(mise[key])
                else:
                    if num in range(1,19):
                        even_b = "BLACK"
                        compte = compte + gain_simple(mise[key])
                    if num in range(19,37):
                        even_r = "RED"
                        compte = compte + gain_simple(mise[key])
                if key == elem:
                    compte = compte + gain_simple(mise[key])
    return compte
            
                

def bille():
    return("le numero ", random.choice(possibilite))

def game():
    while compte > 0:
        selection()
        print("rien ne va plus!")
        b = bille()
        for key in mise:
            if b == key:
                print(key, " gagne!!")
                probabilite()
            else:
                print("la banque gagne")
                perte(compte, mise[key])
        game()
    
if __name__ == "__main__":
    game()
