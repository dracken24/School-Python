# 3. Module reservations.py

# Gère les réservations : création, affichage, annulation.

# Fonctionnalités :

# - Créer une réservation pour un client et une destination.
# - Annuler une réservation.
# - Afficher toutes les réservations.
# - Sauvegarder et charger les réservations depuis un fichier JSON.

from clients import Clients
from destinations import Destinations

import json

class Reservations:

    def __init__(self):
        self.reservation_file = "json_files/reservations.json"   # Path to json file
        self.reservation_data: dict = self.load_reservations()   # Store reservations.json to a dict
        self.clients = None
        self.destinations = None

    def init(self, clients, destination):
        self.clients = clients
        self.destinations = destination

    # Load all reservations from json file
    def load_reservations(self):
        # open reservations file
        with open(self.reservation_file, 'r') as file:
            return json.load(file)
    
# *************************************************************** #
    
    # Create a reservation
    def add_reservation(self, client_mail: str, destination: str, date: str, price: str):
        # check if client exist
        cli = self.clients.find_client(client_mail)
        if not cli:
            return "\nClient inexistant"
        # print(f"destination: {destination} date: {date} price: {price}")
        
        # Check if destination exist
        destination_obj = self.destinations.find_destination(destination)
        if not destination_obj:
            return "\nDestination inexistante"
        
        # Chec the price
        if destination_obj["price"] != price:
            return f"\nPrix incorrect. Le prix pour {destination} est de {destination_obj['price']}$"
        
        # Check the disponibility
        if destination_obj["disponibility"] != date:
            return "\nDate non disponible pour cette destination"
        
        # Create a new reservation object
        new_reservation = {
            "client": cli["Name"],
            "destination": destination,
            "price": price,
            "date": date,
        }
        
        # Check if destination exist and add to dict and json file
        if not self.find_reservation(cli["Name"], destination, date):
            self.reservation_data["reservation"].append(new_reservation)
            self.destinations.remove_destination(destination)
            self.destinations.save_destination()
            self.save_reservation()
            return "\nRéservation créée avec succès"
        
        # Reservation already exist
        return "\nRéservation déjà existante"
    
# *************************************************************** #

    # Try to find a reservation
    def find_reservation(self, client: str, destination: str, date: str):
        
        # Return reservation if he exist
        for reservation in self.reservation_data["reservation"]:
            if (reservation["client"] == client and 
                reservation["destination"] == destination and 
                reservation["date"] == date):
                return reservation
            
        # reservation dosen't exist
        return None

# *************************************************************** #

    # Remove a reservation
    def remove_reservation(self, client: str, destination: str, date: str, price: str):
        # Return reservation if he exist
        for reservation in self.reservation_data["reservation"]:
            if (reservation["client"] == client and 
                reservation["destination"] == destination and 
                reservation["date"] == date and
                reservation["price"] == price):

                # Add the cancelled reservation to destinations avaliable
                self.destinations.add_destination(destination, price, date)

                # Delete reservation
                self.reservation_data["reservation"].remove(reservation)
                self.save_reservation()
                return True
        
        # Reservation not exist
        return False

# *************************************************************** #

    # Print all reservations
    def show_reservation(self):
        for reservation in self.reservation_data["reservation"]:
            print(f"\n********** Réservation **********")
            print(f"Client: {reservation['client']}")
            print(f"Destination: {reservation['destination']}")
            print(f"Date: {reservation['date']}")
            print("----------------------------------")

# *************************************************************** #

    # Save to JSON.
    def save_reservation(self):
        with open(self.reservation_file, 'w') as file:
            json.dump(self.reservation_data, file, indent=4)

# *************************************************************** #
