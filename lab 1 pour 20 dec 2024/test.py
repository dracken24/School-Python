# retourne les infos de profil du pere noel
from colorama import init, Fore
init(strip=False, autoreset=True)

# retourne les infos de profil du pere noel.
def creer_profil_pere_noel():
    name: str = ""
    first_name: str = ""
    city: str = ""

    name = input("Veuillez entrer le nom du pere noel: ")
    while True:
        # Verification du nom
        if (len(name) <= 0):
            print(Fore.RED + "ERROR, Champ vide, nom requis.")
            name = input("Veuillez entrer le nom du pere noel: ")
            continue

        # Verification du prenom
        if (len(first_name) <= 0):
            first_name = input("Veuillez entrer le prenom du pere noel: ")
        if (len(first_name) <= 0):
            print(Fore.RED + "ERROR, Champ vide, prenom requis.")
            continue
        
        # Verification de la ville
        city = input("Veuillez entrer la ville du pere noel: ")
        if (len(city) <= 0):
            print(Fore.RED + "ERROR, Champ vide, ville requise.")
            continue

        # retourne les 3 valeurs si les 3 champs sont remplis
        else:
            return name, first_name, city
        
liste_enfants: dict = {}

# Function pour afficher les enfants present dans le dictionnaire
def afficher_liste_enfants():
    print(Fore.BLUE + "********************************* Liste des enfanst *********************************")

    if len(liste_enfants) == 0:
        print(Fore.BLUE + "Aucun enfant dans la liste pour le moment.")
    else: #Key child
        for child in liste_enfants:
            child_info = liste_enfants[child]
            print(Fore.GREEN + f"Nom: {child}, Cadeau souhaite: ́{child_info[0]}, Emplacement: {child_info[1]}, Sage: {child_info[2]}")

    print(Fore.BLUE + "*************************************************************************************")

# Function pour ajouter un enfant dans la liste du pere noel
def ajouter_enfant() -> bool:
    name: str = ""
    name_find: bool = False
    gift: str = ""
    gift_find: bool = False
    city: str = ""
    city_find: bool = False
    sage = ""

    while True:
        # Verification du nom de l'enfant
        if name_find == False:
            name = input("Veuillez entrer le nom de l'enfant: ")
            if (len(name) <= 0):
                print(Fore.RED + "ERROR, Champ vide, nom requis.")
                continue
            name_find = True

        # Verification du cadeau de l'enfant
        if gift_find == False:
            gift = input("Veuillez entrer le cadeau de l'enfant: ")
            if (len(gift) <= 0):
                print(Fore.RED + "ERROR, Champ vide, cadeau requis.")
                continue
            gift_find = True

        # Verification de la ville de l'enfant
        if city_find == False:
            city = input("Veuillez entrer la ville de l'enfant: ")
            if (len(city) <= 0):
                print(Fore.RED + "ERROR, Champ vide, ville requise.")
                continue
            city_find = True

        # Verification de la sagesse de l'enfant
        sage = input("L'enfant a-t-il ete sage? [T] pour oui [F] pour non: ")
        if (len(sage) != 1):
            print(Fore.RED + "ERROR, entree invalide.")
            continue
        else:
            if sage[0] == 'T' or sage[0] == 't':
                sage = True
                break
            elif sage[0] == 'F' or sage[0] == 'f':
                sage = False
                break
            print(Fore.RED + "ERROR, entree invalide.")

    # Verifier si l'enfant existe
    for child in liste_enfants:
        if child == name:
            print(Fore.RED + f"L'enfant nome {name} existe deja dans la liste.")
            return False
    
    # Ajout de l'enfant au dictionnaire
    liste_enfants.update({name: (gift, city, sage)})
    print(Fore.YELLOW + f"L'enfant nome {name}a ete ajoute avec succes !")
    return True

# fonction pour changer la sagesse d'un enfant
def modifier_sagesse_enfant():
    name: str = ""
    name_find: bool = False
    sage: str = ""

    while True:
        # Verification pour le nom de l'enfant
        if name_find == False:
            name = input("Veuillez entrer le nom de l'enfant: ")
            if (len(name) <= 0):
                print(Fore.RED + "ERROR, Champ vide, nom requis.")
                continue
            name_find = True

        # Verification de la sagesse de l'enfant
        sage = input("Nouveau status. L'enfant a-t-il ete sage? [T] pour oui [F] pour non: ")
        if (len(sage) != 1):
            print(Fore.RED + "ERROR, entree invalide.")
            continue
        else:
            if sage[0] == 'T' or sage[0] == 't':
                sage = True
                break
            elif sage[0] == 'F' or sage[0] == 'f':
                sage = False
                break
            print(Fore.RED + "ERROR, entree invalide.")

    # Verifier si l'enfant existe
    child_exist: bool = False
    for child in liste_enfants:
        if child == name:
            child_exist = True
            new_status = liste_enfants[child][0], liste_enfants[child][1], sage
            liste_enfants[child] = new_status # Changer le status pour un nouveau
            break
    
    if child_exist == True:
        print(Fore.YELLOW + f"Le statut de sagesse de {name} a ete mis a jour.")
    else:
        print(Fore.YELLOW + f"Aucun enfant nomme {name} n'a ete trouve dans la liste.")

# inventaire initiale
inventory_gift: tuple = ("Poupee", "Vetements", "Lego", "Voiture telecommandee", "Livre",
                         "Puzzle", "Avion", "Playstation", "Bicyclette")

# Function pour imprimer la liste des cadeaux disponibles restant
def print_gift_list():
    print(Fore.BLUE + "************ Liste des cadeaux disponible ************")

    if len(inventory_gift) == 0:
        print(Fore.RED + "Aucun Cadeaux n'est disponible.")
    else:
        index: int = 1
        for g in inventory_gift:
            print(Fore.GREEN + f"Cadeau[{index}] : {g}")
            index += 1

    print(Fore.BLUE + "******************************************************")

def remove_gift_from_list(gift: str, inventory: tuple) -> tuple:
    new_list: list = list(inventory)

    if gift in new_list:
        new_list.remove(gift)

    return tuple(new_list)

# Supprime un cadeau de la liste disponible
def maj_inventaire_cadeau(gift: str) -> bool:
    global inventory_gift # le seule mot global. A eviter le plus possible
    for g in inventory_gift:
        if gift == g: # le supprimer si disponible
            inventory_gift = remove_gift_from_list(gift, inventory_gift)
            return True
    return False

def attribuer_cadeaux():
    print("")

def generer_rapport():
    print("")

def print_profil(profil: tuple[str, str, str]):
    [name, first_name, city] = profil

    print(Fore.BLUE + "************** Creation du profil du Pere Noel **************")
    print(Fore.GREEN + "Nom   : ", name)
    print(Fore.GREEN + "Prenom: ", first_name)
    print(Fore.GREEN + "Ville : ", city)
    print(Fore.BLUE + "*************************************************************")

def main():
    # ### Profil ###
    # test = creer_profil_pere_noel()
    # print_profil(test)
    # print(f"Bienvenue, Pere Noel {test[1]} {test[0]} situe a {test[2]}")
    ################################################

    # ### Enfants ###
    # ajouter_enfant()
    # afficher_liste_enfants()
    # ajouter_enfant()
    # afficher_liste_enfants()
    # modifier_sagesse_enfant()
    # ajouter_enfant()
    # afficher_liste_enfants()
    # ajouter_enfant()
    # afficher_liste_enfants()
    ################################################

    # ### inventory gift ###
    print_gift_list()
    maj_inventaire_cadeau("Lego")
    print_gift_list()
    ################################################

main()
