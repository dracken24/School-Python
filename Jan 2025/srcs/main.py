from clients import Clients
from reservations import Reservations
from destinations import Destinations
from utility import write_prompt

def main():
    clients: Clients = Clients()
    reservations: Reservations = Reservations()
    destinations: Destinations = Destinations()

    reservations.init(clients, destinations)

    while True:
        write_prompt()
        cmd: str = input("\nEntrez votre choix: ")

        if (cmd == '1'):
            print("Ajouter un client")
            cli_name: str = input("Entrez le nom du client: ")
            cli_email: str = input("Entrez le email du client: ")
            cli_phone: str = input("Entrez le numero de telephone du client: ")
            clients.add_client(cli_name, cli_email, cli_phone)
        elif (cmd == '2'):
            print("Rechercher un client par email")
            cli_email: str = input("Entrez le email du client: ")
            client = clients.find_client(cli_email)
            if (not client):
                print("\nClient inexistant")
            else:
                print(f"\nClient Name      : {client["Name"]}")
                print(f"Client email     : {client["email"]}")
                print(f"Client telephone : {client["phone"]}\n")
        elif (cmd == '3'):
            print("Ajouter une destination")
            dest_place: str = input("Entrez une destination: ")
            dest_price: str = input("Entrez un prix: ")
            dest_dispo: str = input("Entrez une date format (dd/mm/yyyy): ")
            destinations.add_destination(dest_place, dest_price, dest_dispo)
        elif (cmd == '4'):
            print("Mettre a jour une destination")
            dest_place: str = input("Entrez une destination: ")
            dest_price: str = input("Entrez un prix: ")
            dest_dispo: str = input("Entrez une date format (dd/mm/yyyy): ")
            if (destinations.updates_destination(dest_place, dest_price, dest_dispo) == False):
                print("\nDestination inexistante.")
        elif (cmd == '5'):
            print("Rechercher une destination par nom")
            dest_place: str = input("Entrez une destination: ")
            dest = destinations.find_destination(dest_place)
            if (not dest):
                print("\nDestination inexistant")
            else:
                print(f"\nDestination Place : {dest["place"]}")
                print(f"Destination Prix  : {dest["price"]}")
                print(f"Destination Date  : {dest["disponibility"]}\n")
        elif (cmd == '6'):
            print("Creer une reservation")
            cli_email: str = input("Entrez le email du client: ")
            reserv_place: str = input("Entrez une destination: ")
            reserv_price: str = input("Entrez un prix: ")
            reserv_date: str = input("Entrez une date format (dd/mm/yyyy): ")
            print(reservations.add_reservation(cli_email, reserv_place, reserv_date, reserv_price))
        elif (cmd == '7'):
            print("Anuler une reservation")
            cli_name: str = input("Entrez le nom du client: ")
            reserv_dest: str = input("Entrez une destination: ")
            reserv_price: str = input("Entrez un prix: ")
            reserv_date: str = input("Entrez une date format (dd/mm/yyyy): ")
            if (reservations.remove_reservation(cli_name, reserv_dest, reserv_date, reserv_price) == False):
                print("\nReservation inexistante")
        elif (cmd == '8'):
            print("Afficher les reservation")
            reservations.show_reservation()
        elif (cmd == 'Q' or cmd == 'q'):
            break

main()
