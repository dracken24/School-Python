import json

class Destinations:
    # Constructor
    def __init__(self):
        self.destination_file = "json_files/destinations.json"   # Path to json file
        self.destination_data: dict = self.load_destinations()   # Store destination.json to a dict

    # Load all destinations from json file
    def load_destinations(self):
        # open destinations file
        with open(self.destination_file, 'r') as file:
            return json.load(file)

# *************************************************************** #
    
    # Add a destination.
    def add_destination(self, place: str, price: str, disponibility: str) -> str:
        new_destination = { "place": place, "price": price, "disponibility": disponibility }
        
        # If not reservation exist, add him.
        if not self.find_destination(place):
            self.destination_data["destination"].append(new_destination)
            self.save_destination()
            return "\nDestination ajoute avec succes"
        
        # distination already exist
        return "\nDestination deja existante"

# *************************************************************** #
    
    # Update a destination
    def updates_destination(self, place: str, price: str, disponibility: str):
        # Check all destinations
        for destination in self.destination_data["destination"]:
            if destination["place"] == place:
                # Update destination price
                if price:
                    destination["price"] = price
                # Update disponibility
                if disponibility:
                    destination["disponibility"] = disponibility
                
                # Save modifications to json
                self.save_destination()
                return "\nDestination modifie avec succes"
        
        # Return fals if reservation not found
        return "\nDestination inexistante"

# *************************************************************** #

    # Find a destination by name
    def find_destination(self, place: str):
        # Return reservation if he exist
        for destination in self.destination_data["destination"]:
            if (destination["place"] == place):
                return destination
            
        # reservation dosen't exist
        return None
    
# *************************************************************** #

    # remove destination if exist
    def remove_destination(self, dest: str):
        dest_to_remove = self.find_destination(dest)
        # Remove destination if not None
        if (dest_to_remove):
            self.destination_data["destination"].remove(dest_to_remove)
            self.save_destination()

# *************************************************************** #

    # Save to JSON.
    def save_destination(self):
        with open(self.destination_file, 'w') as file:
            json.dump(self.destination_data, file, indent=4)

# *************************************************************** #
