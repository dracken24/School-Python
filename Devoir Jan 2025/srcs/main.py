from clients import Clients
from reservations import Reservations
from destinations import Destinations

import datetime

# Print the menu after each command
def write_prompt():
    print("\n******************* Menu *******************")
    print("Ajouter un client                  : 1")
    print("Rechercher un client par email     : 2")
    print("\nAjouter une destination            : 3")
    print("Mettre a jour une destination      : 4")
    print("Rechercher une destination par nom : 5")
    print("\nCreer une reservation              : 6")
    print("Anuler une reservation             : 7")
    print("Afficher les reservation           : 8")
    print("\nQuitter                            : Q / q")
    print("--------------------------------------------")

# Add a new cliend with verification by email.
def add_client(clients: Clients):
    print("Ajouter un client")
    # Collect input values
    cli_name: str = input("Entrez le nom du client: ")
    cli_email: str = input("Entrez le email du client: ")
    cli_phone: str = input("Entrez le numero de telephone du client: ")
    print(clients.add_client(cli_name, cli_email, cli_phone))

# find a client by email
def find_client_by_mail(clients: Clients):
    print("Rechercher un client par email")
    # Collect input values
    cli_email: str = input("Entrez le email du client: ")
    client = clients.find_client(cli_email)
    if (not client):# not found
        print("\nClient inexistant")
    else: # Client found
        print(f"\nClient Name      : {client["Name"]}")
        print(f"Client email     : {client["email"]}")
        print(f"Client telephone : {client["phone"]}\n")

# Add an avaliable destination
def add_destination(destinations: Destinations):
    print("Ajouter une destination")
    # Collect input values
    dest_place: str = input("Entrez une destination: ")
    dest_price: str = input("Entrez un prix: ")
    dest_dispo: str = input("Entrez une date format (dd/mm/yyyy): ")
    # Add destination and print return
    print(destinations.add_destination(dest_place, dest_price, dest_dispo))

# Update a destination with new infos
def update_destinations(destinations: Destinations):
    print("Mettre a jour une destination")
    # Collect input values
    dest_place: str = input("Entrez une destination: ")
    dest_price: str = input("Entrez un prix: ")
    dest_dispo: str = input("Entrez un nombre de places disponibles: ")
    # Add destination and print return
    print(destinations.updates_destination(dest_place, dest_price, dest_dispo))

# Find a destination with name
def find_destination_by_name(destinations: Destinations):
    print("Rechercher une destination par nom")
    # Collect input values
    dest_place: str = input("Entrez une destination: ")
    dest = destinations.find_destination(dest_place)
    if (not dest): # destination dont exist
        print("\nDestination inexistant")
    else: # print existing destination
        print(f"\nDestination Place          : {dest["place"]}")
        print(f"Destination Prix           : {dest["price"]}")
        print(f"Destination disponibility  : {dest["disponibility"]}\n")

# Take a new reservation
def add_a_reservation( reservations: Reservations):
    print("Creer une reservation")
    # Collect input values
    cli_email: str = input("Entrez le email du client: ")
    reserv_place: str = input("Entrez une destination: ")
    reduction: str = input("Le client a droit a une reduction de 15% [Y] oui / [N] non: ")
    reserv_date: datetime = datetime.datetime.now()
    # Add destination and print return
    print(reservations.add_reservation(cli_email, reserv_place, reserv_date, reduction))

# Cancel a reservation
def cancel_reservation(reservations: Reservations):
    print("Anuler une reservation")
    # Collect input values
    cli_name: str = input("Entrez le nom du client: ")
    reserv_dest: str = input("Entrez une destination: ")
    # Add destination and print return
    print(reservations.remove_reservation(cli_name, reserv_dest))

def main():
    clients: Clients = Clients()
    reservations: Reservations = Reservations()
    destinations: Destinations = Destinations()

    reservations.init(clients, destinations)

    while True:
        write_prompt()
        cmd: str = input("\nEntrez votre choix: ")

        # User choices
        if (cmd == '1'):
            add_client(clients)
        elif (cmd == '2'):
            find_client_by_mail(clients)
        elif (cmd == '3'):
            add_destination(destinations)
        elif (cmd == '4'):
            update_destinations(destinations)
        elif (cmd == '5'):
            find_destination_by_name(destinations)
        elif (cmd == '6'):
            add_a_reservation(reservations)
        elif (cmd == '7'):
            cancel_reservation(reservations)
        elif (cmd == '8'):
            print("Afficher les reservation")
            reservations.show_reservation()
        elif (cmd == 'Q' or cmd == 'q'):
            break

# Entry point
main()
