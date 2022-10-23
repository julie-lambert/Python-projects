# Demander d'abord si l'utilisateur veut jouer ou voir les scores:
choix = input("Bonjour, souhaites tu jouer ou voir les scores ? ")

# choix des usernames:
if choix == "jouer":
    username1 = input("Username 1 Croix: ")
    username2 = input("Username 2 Rond: ")

# Afficher la grille :

def afficher_grille():
    for i in range(3):
        for i in range(3):
            print("-", end=" ")
        print()

afficher_grille()

tour = input(username1 + " joue ")