# 1. Module clients.py
# Gère les clients, leur ajout, leur recherche, et leur modification.
# Fonctionnalités :

# - Ajouter un client (nom, email, téléphone).
# - Rechercher un client par email.
# - Charger et sauvegarder les clients dans un fichier JSON.

# from utility import read_from_json, write_to_json
import json

class Clients:
    # Constructor
    def __init__(self):
        self.clients_file = "json_files/clients.json"   # Path to json file
        self.clients_data = self.load_clients()         # Store client.json to a dict

    # Load all clients from json file
    def load_clients(self):
        # open client file
        with open(self.clients_file, 'r') as file:
            return json.load(file)
    
# *************************************************************** #

    # Add a client (nom, email, phone).
    def add_client(self, name: str, email: str, phone: str):

        new_client = { "Name": name, "email": email, "phone": phone }
        
        # If client exist, add him.
        if not self.find_client(email):
            self.clients_data["client"].append(new_client)
            self.save_client()
            return True
        
        # Client already exist
        return False
# *************************************************************** #

    # Try to find a client by email
    def find_client(self, email: str):
        # Return client if he exist
        for client in self.clients_data["client"]:
            if client["email"] == email:
                return client
            
        # Client dosen't exist
        return None
    
# *************************************************************** #
    
    # Save to JSON.
    def save_client(self):
        with open(self.clients_file, 'w') as file:
            json.dump(self.clients_data, file, indent=4)

# *************************************************************** #
