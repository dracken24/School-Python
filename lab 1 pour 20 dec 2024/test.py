# retourne les infos de profil du pere noel
from colorama import init, Fore
init(strip=False, autoreset=True)

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
        
def print_profil(profil: tuple):
    [name, first_name, city] = profil

    print(Fore.BLUE + "******************** Profil du Pere Noel ********************")
    print(Fore.GREEN + "Nom   : ", name)
    print(Fore.GREEN + "Prenom: ", first_name)
    print(Fore.GREEN + "Ville : ", city)
    print(Fore.BLUE + "*************************************************************")

def main():
    # name, first_name, city = creer_profil_pere_noel()
    test = creer_profil_pere_noel()
    print_profil(test)
    print(f"Bienvenue, Pere Noel {test[1]} {test[0]} situe a {test[2]}")

main()