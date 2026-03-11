# fake senosrs to test the software 
# Fake humidity, tempreatire and soilm moisture 


# Creating the fake data to test the system
import random

def get_sensor_data():
    return {
        "temperature": round(random.uniform(18, 30), 1),
        "humidity": round(random.uniform(40, 80), 1),
        "soil_moisture": round(random.uniform(20, 70), 1),
        "water_level": round(random.uniform(30, 100), 1)
    }