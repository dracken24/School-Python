from colorama import init, Fore
init(strip=False, autoreset=True)

pere_noel: tuple[str, str, str] = ()

# retourne les infos de profil du pere noel
def creer_profil_pere_noel() -> tuple[str, str, str]:
    name: str = ""
    first_name: str = ""
    city: str = ""

    print(Fore.BLUE + "\n****************** Creation du profil du Pere Noel ****************")

    name = input(Fore.YELLOW + "Entrez votre nom: " + Fore.RESET)
    while True:
        # Verification du nom
        if (len(name) <= 0):
            print(Fore.RED + "ERROR, Champ vide, nom requis.")
            name = input(Fore.YELLOW + "Entrez votre nom: " + Fore.RESET)
            continue

        # Verification du prenom
        if (len(first_name) <= 0):
            first_name = input(Fore.YELLOW + "Entrez votre prenom: " + Fore.RESET)
        if (len(first_name) <= 0):
            print(Fore.RED + "ERROR, Champ vide, prenom requis.")
            continue
        
        # Verification de la ville
        city = input(Fore.YELLOW + "Entrez votre emplacement actuel : " + Fore.RESET)
        if (len(city) <= 0):
            print(Fore.RED + "ERROR, Champ vide, ville requise.")
            continue

        # retourne les 3 valeurs si les 3 champs sont remplis
        else:
            print(Fore.GREEN + f"\nBienvenue, Pere Noel {first_name} {name} situe a {city} !\n")
            print(Fore.BLUE + "*******************************************************************")
            return name, first_name, city
        
liste_enfants: dict = {}

# Function pour afficher les enfants present dans le dictionnaire
def afficher_liste_enfants():
    print(Fore.BLUE + "\n************************* Liste des enfanst ***********************")

    if len(liste_enfants) == 0:
        print(Fore.YELLOW + "Aucun enfant dans la liste pour le moment.")
    else: #Key child
        i: int = 1
        for child in liste_enfants:
            child_info = liste_enfants[child]
            print(Fore.GREEN + str(i) + ". Nom: " + Fore.YELLOW + child + Fore.GREEN +" Cadeau souhaite: " + Fore.YELLOW + child_info[0]
                  + Fore.GREEN + " Emplacement: " + Fore.YELLOW + child_info[1] + Fore.GREEN + " Sage: " + Fore.YELLOW + str(child_info[2]))
            i += 1

    print(Fore.BLUE + "*******************************************************************")

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
        sage = input("L'enfant a-t-il ete sage? [T] pour true [F] pour false: ")
        if (len(sage) != 1):
            print(Fore.RED + "ERROR, entree invalide.")
            continue
        else:
            if sage[0] == 'T' or sage[0] == 't' or sage == "true" or sage == "True":
                sage = True
                break
            elif sage[0] == 'F' or sage[0] == 'f' or sage == "false" or sage == "False":
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
    print(Fore.GREEN + f"\nNom de l’enfant: {Fore.YELLOW + name}")
    print(Fore.GREEN + f"Cadeau souhaite: {Fore.YELLOW + gift}")
    print(Fore.GREEN + f"Emplacement de l’enfant: {Fore.YELLOW + city}")
    print(Fore.GREEN + f"L’enfant est-il sage ? (True/False): {Fore.YELLOW + str(sage)}")
    print(Fore.GREEN + f"\nL'enfant nome {Fore.YELLOW + name + Fore.GREEN} a ete ajoute avec succes !")
    return True

def print_new_status(name: str, sage: str):
    print(Fore.GREEN + f"\nNom de l’enfant: {Fore.YELLOW + name}")
    print(Fore.GREEN + f"Nouveau statut de sagesse (True/False): {Fore.YELLOW + str(sage)}")
    print(Fore.GREEN + f"\nLe statut de sagesse de {Fore.YELLOW + name + Fore.GREEN} a ete mis a jour\n")

# fonction pour changer la sagesse d'un enfant
def modifier_sagesse_enfant():
    name: str = ""
    name_find: bool = False
    sage: str = ""

    while True:
        # Verification pour le nom de l'enfant
        if name_find == False:
            name = input("Nom de l'enfant: ")
            if (len(name) <= 0):
                print(Fore.RED + "ERROR, Champ vide, nom requis.")
                continue
            name_find = True
        
        # Verifier si l'enfant existe
        child_exist: bool = False
        for child in liste_enfants:
            if child == name:
                child_exist = True
                break
        
        # Quitter la fonction si l'enfant n'existe pass
        if child_exist == False:
            print(Fore.RED + f"Aucun enfant nomme {Fore.YELLOW + name + Fore.RED} n'a ete trouve dans la liste.")
            return

        # Verification de la sagesse de l'enfant
        sage = input("Nouveau statut de sagesse (True [T] / False [F]): ")
        if (len(sage) != 1):
            print(Fore.RED + "ERROR, entree invalide.")
            continue
        else:
            if sage[0] == 'T' or sage[0] == 't' or sage == "true" or sage == "True":
                sage = True
                # Mise à jour du statut dans liste_enfants
                liste_enfants[name] = (liste_enfants[name][0], liste_enfants[name][1], sage)
                print_new_status(name, sage)
                break
            elif sage[0] == 'F' or sage[0] == 'f' or sage == "false" or sage == "False":
                sage = False
                # Mise à jour du statut dans liste_enfants
                liste_enfants[name] = (liste_enfants[name][0], liste_enfants[name][1], sage)
                print_new_status(name, sage)
                break
            print(Fore.RED + "ERROR, entree invalide.")

# inventaire initiale
inventory_gift: tuple = ("Poupee", "Vetements", "Lego", "Voiture telecommandee", "Livre",
                         "Puzzle", "Avion", "Playstation", "Bicyclette")

# Function pour imprimer la liste des cadeaux disponibles restant
def print_gift_list():
    print(Fore.BLUE + "\n****************** Liste des cadeaux disponible ******************")

    if len(inventory_gift) == 0:
        print(Fore.RED + "Aucun Cadeaux n'est disponible.")
    else:
        index: int = 1
        for g in inventory_gift:
            print(Fore.GREEN + f"Cadeau[{index}] : {g}")
            index += 1

    print(Fore.BLUE + "******************************************************************")

def remove_gift_from_list(gift: str, inventory: tuple) -> tuple:
    new_list: list = list(inventory)

    if gift in new_list:
        new_list.remove(gift)

    return tuple(new_list)

# Supprime un cadeau de la liste disponible
def maj_inventaire_cadeau(gift: str) -> bool:
    global inventory_gift # Le mot global est a eviter le plus possible
    for g in inventory_gift:
        if gift == g: # le supprimer si disponible
            inventory_gift = remove_gift_from_list(gift, inventory_gift)
            return True
    return False

rapport_enfant: dict = {}

def maj_rapport_enfant(child_name: str, gift: str, delivery_reason: str, delivery_status: bool):
    if child_name in rapport_enfant:
        rapport_enfant[child_name, gift, delivery_reason, delivery_status] += 1
    else:
        rapport_enfant[child_name, gift, delivery_reason, delivery_status] = 1

# Verifications et attribution d'un cadeau a un enfant
def attribuer_cadeaux(pere_noel: tuple[str, str, str], child_name: str, gift: str) -> bool:
    # Vérifier si l'enfant a déjà reçu un cadeau avec succès
    for (existing_child, _, _, delivery_status) in rapport_enfant.keys():
        if existing_child == child_name and delivery_status == True:
            print(Fore.YELLOW + f"L'enfant {child_name} a déjà reçu un cadeau.")
            return False
    
    # Verifier si l'enfant a ete sage
    if liste_enfants[child_name][2] == False:
        print(Fore.RED + f"Impossible de livrer le cadeau {gift} a {child_name} situé a {liste_enfants[child_name][1]} - Raison : Enfant non sage.")
        # Mettre à jour le rapport si une entrée existe déjà
        for key in list(rapport_enfant.keys()):
            if key[0] == child_name:
                del rapport_enfant[key]
        maj_rapport_enfant(child_name, gift, "Enfant non sage", False)
        return False
    
    # Verifier l'emplacement de l'enfant et du pere noel
    if liste_enfants[child_name][1] != pere_noel[2]:
        print(Fore.RED + f"Impossible de livrer le cadeau {gift} a {child_name} situé a {liste_enfants[child_name][1]} - Raison : Emplacement different.")
        # Mettre à jour le rapport si une entrée existe déjà
        for key in list(rapport_enfant.keys()):
            if key[0] == child_name:
                del rapport_enfant[key]
        maj_rapport_enfant(child_name, gift, "Emplacement different", False)
        return False

    # Verifier la disponibilite du cadeau
    if maj_inventaire_cadeau(gift) == True:
        print(Fore.GREEN + f"{child_name} recevra : {gift}")
        # Mettre à jour le rapport si une entrée existe déjà
        for key in list(rapport_enfant.keys()):
            if key[0] == child_name:
                del rapport_enfant[key]
        maj_rapport_enfant(child_name, gift, "Cadeau Voulue", True)
        return True
    else:
        print(Fore.YELLOW + f"{child_name} recevra : Cadeau générique (car le cadeau souhaité n'est pas disponible).")
        # Mettre à jour le rapport si une entrée existe déjà
        for key in list(rapport_enfant.keys()):
            if key[0] == child_name:
                del rapport_enfant[key]
        maj_rapport_enfant(child_name, "Cadeau générique", "Cadeau non disponible", True)
        return True

def generer_rapport():
    print(Fore.BLUE + "\n************** Rapport des Cadeaux Livrés **************")
    for child, gift in rapport_enfant:
        if rapport_enfant[child, gift, delivery_reason, delivery_status] == True:
            print(Fore.GREEN + f"{child} recevra : {gift}")
        # else:
        #     print(Fore.RED + f"{child} recevra : {gift}")
        print("\n********************** Livraisons Impossibles *********************")
        for child, gift, delivery_reason, delivery_status in rapport_enfant:
            if delivery_status == False:
                if delivery_reason == "Emplacement different":
                    print(Fore.RED + f"{child} - Raison : Emplacement different")
                elif delivery_reason == "Enfant non sage":
                    print(Fore.RED + f"{child} - Raison : Enfant non sage")
    print(Fore.BLUE + "*******************************************************************")

def print_final_rapport():
    print(Fore.YELLOW + "\n******************* Rapport des Cadeaux Livres ********************")
    print(Fore.BLUE + "\n******************* Cadeaux livres avec succes ********************")
    for (child, gift, delivery_reason, delivery_status) in rapport_enfant:
        if delivery_status == True:
            print(Fore.GREEN + f"{child} recevra : {gift}")

    print(Fore.BLUE + "\n********************* Livraisons Impossibles **********************")
    for (child, gift, delivery_reason, delivery_status) in rapport_enfant:
        if delivery_status == False:
            print(Fore.RED + f"{child} à {liste_enfants[child][1]} - Raison : {delivery_reason}")

    print(Fore.BLUE + "*******************************************************************")

# Afficher un profil enfant
def print_profil(profil: tuple[str, str, str]):
    [name, first_name, city] = profil

    print(Fore.BLUE + "\n***************** Creation du profil du Pere Noel *****************")
    print(Fore.GREEN + "Nom   : ", name)
    print(Fore.GREEN + "Prenom: ", first_name)
    print(Fore.GREEN + "Ville : ", city)
    print(Fore.BLUE + "*******************************************************************")

# Afficher les choix utilisateur
def print_prompt():
    print(Fore.BLUE + "\n************************* Menu Principal **************************")
    print(Fore.GREEN + "1. Afficher la liste des enfants")
    print(Fore.GREEN + "2. Ajouter un enfant")
    print(Fore.GREEN + "3. Modifier le statut de sagesse d’un enfant")
    print(Fore.GREEN + "4. Attribuer les cadeaux")
    print(Fore.GREEN + "5. Quitter (Yes/No) ?")
    print(Fore.BLUE + "*******************************************************************")

def attribuer_cadeaux_menu(pere_noel: tuple[str, str, str]):
    # Supprimer la réinitialisation du rapport ici
    afficher_liste_enfants()
    print_gift_list()

    for child_name, child_value in liste_enfants.items():
        attribuer_cadeaux(pere_noel, child_name, child_value[0])
 
def main():
    # ### Profil ###
    pere_noel = creer_profil_pere_noel()

    # Boucle principale du programme
    while True:
        print_prompt()
        choice = input("Veuillez entrer votre choix: ")
        if choice == "1":
            afficher_liste_enfants()
        elif choice == "2":
            ajouter_enfant()
        elif choice == "3":
            modifier_sagesse_enfant()
        elif choice == "4":
            attribuer_cadeaux_menu(pere_noel)
            print_final_rapport()
        elif choice == "5" or choice == "Yes" or choice == "yes":
            break

main()
