# Touché Coulé ! Dans cette partie de bataille navale que vous jouerez contre un ordinateur sur un plateau de 9*9 cases,
# vous aurez 5 bateaux : 
# 55555 : bateau de 5 cases de long
# 4444 : bateau de 4 cases de long
# 333 : bateau de 3 cases de long
# 22 : bateau de 2 cases de long
####################################
######## Développé par Paul ########
####################################
import random as rd
import numpy as np
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    print("\n\n\n\n––––––––––––––––––––––––––––––––––––––––")
    plateau_ai = initAI()
    plateau_pl = initPlayer()
    print("\n",plateau_ai)

    game(plateau_ai,plateau_pl)
    return 


def initAI():
    plateau = np.zeros((9,9),dtype=int)
    for i in range(2,6):
        isline = bool(rd.getrandbits(1))
        possibilities = 9 - i
        boat_position = 0
        while boat_position==0:
            number_line_or_col = rd.randint(0,8)
            boat_position = rd.randint(0,possibilities)
            total = 0
            for j in range(i): 
                if isline:
                    total+=plateau[number_line_or_col][boat_position+j]
                else: 
                    total+=plateau[boat_position+j][number_line_or_col]
            if total != 0:
                boat_position=0
        for k in range(i):
            if isline : plateau[number_line_or_col][boat_position+k] = j+1
            else:  plateau[boat_position+k][number_line_or_col] = j+1
    return plateau


def initPlayer():
    plateau = np.zeros((9,9),dtype=int)
    print(F"Merci d'indiquer la case de départ et la case d'arrivée de votre bateau, en séparant les deux cases. \nExemple : A1,C3")
    for i in range(2,6):
        isCorrect = False
        while not isCorrect:
            answer = input((F"Votre choix pour le bateau de taille {i} : "))
            if answer[2]=="," and len(answer)==5 and checkInt(answer[1]) and checkInt(answer[4]) and checkAlpha(answer[0]) and checkAlpha(answer[3]):
                col1_temp = answer[0].upper()
                col2_temp = answer[3].upper()
                line1 = alphabet.index(col1_temp)
                line2 = alphabet.index(col2_temp)             
                col1 = int(answer[1])-1
                col2 = int(answer[4])-1
                coords =[]
                if line1==line2:
                    diff = int(col1)-int(col2)
                    if abs(diff)==i-1:
                        for j in range(i):
                            if col1<col2:
                                coords.append([line1,col1+j])
                            if col1>col2:
                                coords.append([line1,col1-j])    
                        total = 0
                        for k in range(i):
                            total+=plateau[coords[k][0],coords[k][1]]
                        if total==0:
                            for l in range(i):
                                plateau[coords[l][0]][coords[l][1]] = i
                            isCorrect=True
                if col1==col2:
                    diff = int(line1)-int(line2)
                    if abs(diff)==i-1:
                        for j in range(i):
                            if line1<line2:
                                coords.append([line1+j,col1])
                            if line1>line2:
                                coords.append([line1-j,col1]) 
                        total = 0
                        for k in range(i):
                            total+=plateau[coords[k][0],coords[k][1]]
                        if total==0:
                            for l in range(i):
                                plateau[coords[l][0]][coords[l][1]] = i
                            isCorrect=True
    return plateau


def game(p_ai,p_player):
    print("\n\n––––––––––––––––––––\n\n")
    print("L'IA va commencer à jouer. Bonne chance !")
    p_vi = np.zeros((9,9),dtype=int)
    score_ai = 14
    score_pl = 14
    GameFinished = False
    nb = 0
    while not GameFinished:
        if score_ai != 0:
            p_player,score_pl = AI_turn(p_player,score_pl)
            print("\nVotre plateau :          Plateau de l'adversaire :\n")
            for i in range(len(p_player)):
                print(p_player[i], "    ", p_vi[i])
            if score_pl != 0:
                p_ai,score_ai = Pl_turn(p_ai,score_ai,p_vi)
        else:
            GameFinished = True
        nb+=1
    if score_ai==0:
        print("Bravo ! C'est toi qui a a gagné ! Tu l'as échappé belle, mais seul le résultat compte.\n\n\n Développé par Paul.")
        return
    if score_pl==0:
        print("Malheureusement, l'adversaire fut meilleur que toi. Continue de t'entrainer, tu n'as clairement pas le niveau.\n\n\n Développé par Paul.")
        return
    

def Pl_turn(p_ai,score_ai,p_vi):
    print("––––––––––––––––––––\n")
    print(F"Merci d'indiquer la case que tu souhaites viser. \nExemple : A1")
    caseIsGood=False
    while not caseIsGood:
        answer = input(("Choix de ta case: "))
        if len(answer)==2 and checkInt(answer[1]) and checkAlpha(answer[0]):
            lett = answer[0].upper()
            coords = (alphabet.index(lett),int(answer[1])-1)
            print(coords)
            if p_ai[coords[0]][coords[1]]!=9 and p_ai[coords[0]][coords[1]]!=7:
                caseIsGood = True
                if p_ai[coords[0]][coords[1]] == 0:
                    p_ai[coords[0]][coords[1]] = 9 
                    p_vi[coords[0]][coords[1]] = 9 
                    letter = alphabet[coords[0]]
                    print("\n\n––––––––––––––––––––")
                    print(F"Malheureusement, tu as mal visé, en tirant en {letter}{coords[1]+1}. Focus.")
                    print("––––––––––––––––––––\n")
                elif p_ai[coords[0]][coords[1]]>1 and p_ai[coords[0]][coords[1]]<6:
                    p_vi[coords[0]][coords[1]] =  p_ai[coords[0]][coords[1]]
                    p_ai[coords[0]][coords[1]] =  7
                    score_ai-=1
                    letter = alphabet[coords[0]]
                    print("\n\n––––––––––––––––––––")
                    print(F"Appelons le Bob Lee Swagger ! Bravo, tu l'as touché en {letter}{coords[1]+1}. Continue.")
                    print("––––––––––––––––––––\n")
            else: 
                print("\n––––––––––––––––––––")
                print("Vous avez déjà tiré sur cette case. Merci de réessayer.")
                print("––––––––––––––––––––")
    return p_ai,score_ai


def AI_turn(p_player,score_pl):
    caseIsGood = False
    while not caseIsGood:
        coords = (rd.randint(0,8),rd.randint(0,8))
        if p_player[coords[0]][coords[1]]!=9 and p_player[coords[0]][coords[1]]!=7:
            caseIsGood = True
            letter = alphabet[coords[0]]
            if p_player[coords[0]][coords[1]] == 0:
                p_player[coords[0]][coords[1]] = 9 #Dans l'eau
                print("\n\n––––––––––––––––––––")
                print(F"Ouf ! Votre adversaire a tiré en {letter}{coords[1]+1}, mais n'a touché qu'un poisson.")
                print("––––––––––––––––––––\n")
            else:
                p_player[coords[0]][coords[1]] = 7 #Touché !
                score_pl-=1
                print("\n\n––––––––––––––––––––")
                print(F"Aie... Votre adversaire a tiré en {letter}{coords[1]+1}, et a abimé un de vos bateaux.")
                print("––––––––––––––––––––\n")

    return p_player,score_pl
    

def checkInt(number):
    try:
        val = int(number) 
        if val>=1 and val<=9:
            return True
    except ValueError:
        return False
    return False


def checkAlpha(letter):
    letter = letter.upper()
    try:
        if alphabet.index(letter)<9:
            return True
    except ValueError:
        return False
    return False

def checkOdd(number):
    if (number % 2) == 0:
        return True
    else:
        return False
main()