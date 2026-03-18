# Main flask section 

# use this class for the Json file 

from flask import Flask, render_template, jsonify, request, redirect, url_for
from test_sensors import get_sensor_data
from data_store import load_plant_data, save_plant_data

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

@app.route("/api/readings")
def api_readings():
    return jsonify(get_sensor_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)