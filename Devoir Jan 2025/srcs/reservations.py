from clients import Clients
from destinations import Destinations

import json
import datetime

class Reservations:

    # Constructor
    def __init__(self):
        self.reservation_file = "json_files/reservations.json"   # Path to json file
        self.reservation_data: dict = self.load_reservations()   # Store reservations.json to a dict
        self.clients = None         # Reference to all clients
        self.destinations = None    # Reference to all avaliable destinations

    # Enter reference after init itself for let time to each class
    # to load data from respectif .json
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
    def add_reservation(self, client_mail: str, destination: str, date: datetime, reduction: str) -> str:
        # check if client exist
        cli = self.clients.find_client(client_mail)
        if (not cli):
            return "\nClient inexistant"
        # print(f"destination: {destination} date: {date} price: {price}")
        
        # Check if destination exist
        destination_obj = self.destinations.find_destination(destination)
        if (not destination_obj):
            return "\nDestination inexistante"
        
        # Check the disponibility
        if (int(destination_obj["disponibility"]) <= 0):
            return "\nPlace non disponible pour cette destination"
        
        # Add or not 15% reduction
        if (reduction != 'y' and reduction != 'Y' and reduction != 'n' and reduction != 'N'):
            return "\nChoix invalide pour le credit de 15%"
        
        reduc: bool = False
        if (reduction == 'y' or reduction == 'Y'):
            reduc = True

        # Create a new reservation object
        new_reservation = {
            "client": cli["Name"],
            "destination": destination,
            "reduction": reduc,
            "date": date.strftime('%Y-%m-%d'),
        }
        
        # Check if destination exist and add to dict and json file
        if not self.find_reservation(cli["Name"], destination, date):
            self.reservation_data["reservation"].append(new_reservation)
            # Add one place to destination
            dest = self.destinations.find_destination(destination)
            if dest:
                dest["disponibility"] = str(int(dest["disponibility"]) - 1) # -1 place to destination disponibility
                self.destinations.save_destination()

            self.save_reservation()
            return "\nRéservation cree avec succes"
        
        # Reservation already exist
        return "\nRéservation deja existante"
    
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
    def remove_reservation(self, client: str, destination: str):
        # Return reservation if he exist
        for reservation in self.reservation_data["reservation"]:
            if (reservation["client"] == client and 
                reservation["destination"] == destination):

                # Add one place to destination
                dest = self.destinations.find_destination(destination)
                if dest:
                    dest["disponibility"] = str(int(dest["disponibility"]) + 1)
                    self.destinations.save_destination()

                # Delete reservation
                self.reservation_data["reservation"].remove(reservation)
                self.save_reservation()
                return "\nReservation annuler avec succes"
        
        # Reservation not exist
        return "\nReservation inexistante"

# *************************************************************** #

    # Print all reservations
    def show_reservation(self):
        for reservation in self.reservation_data["reservation"]:
            print(f"\n********** Reservation **********")
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
