import json
import os

DATA_FILE = "plant_data.json"

# If there is  previous data, load it 
def load_plant_data():
    if not os.path.exists(DATA_FILE):
        return None

    with open(DATA_FILE, "r") as file:
        return json.load(file)

# no data allow the user to save the data
def save_plant_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


#Recird the last wated time of the plant 
def update_last_watered(new_date):
    plant = load_plant_data()
    if plant:
        plant["last_watered"] = new_date
        save_plant_data(plant)