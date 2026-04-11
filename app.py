# Main flask section 

# use this class for the Json file 

from flask import Flask, render_template, jsonify, request, redirect, url_for
from sensors import get_sensor_data
# from test_sensors import get_sensor_data
from datetime import datetime 
from data_store import load_plant_data, save_plant_data, update_last_watered, delete_plant_data
from plant_controller import pump_for_seconds

app = Flask(__name__)

@app.route("/")
def dashboard():
    sensor_data = get_sensor_data()
    plant = load_plant_data()

   # if no plant is added previously 
    if plant is None:
        return render_template("add_plant.html")
    
    # if there is a plant 
    return render_template("index.html", sensor_data=sensor_data, plant=plant)

@app.route("/add_plant", methods=["POST"])
def add_plant():
    plant_data = {
        "name": request.form["name"],
        "type": request.form["type"],
        "date_planted": request.form["date_planted"],
        "last_watered": request.form["last_watered"]
    }
    # Save plant data and return to the dashboard 
    save_plant_data(plant_data)
    return redirect(url_for("dashboard"))

# Adding the button for watering the plant
# Eddited so that the pump actaully works  
# When the buttone is pressed the last watered time should update with day and date
@app.route("/water_plant", methods=["POST"])
def water_plant():
    update_last_watered(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    try:
        pump_for_seconds(5)
    except Exception as e:
        print("Pump error:", e)

    return redirect(url_for("dashboard"))

# Deltet the plant 
@app.route("/delete_plant", methods=["POST"])
def delete_plant():
    delete_plant_data()
    return redirect(url_for("dashboard"))

@app.route("/api/readings")
def api_readings():
    return jsonify(get_sensor_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)