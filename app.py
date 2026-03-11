# main flask app


from flask import Flask, render_template, jsonify
from test_sensors import get_sensor_data

app = Flask(__name__)

@app.route("/")
def dashboard():
    sensor_data = get_sensor_data()
    return render_template("index.html", sensor_data=sensor_data)

@app.route("/api/readings")
def api_readings():
    return jsonify(get_sensor_data())

if __name__ == "__main__":
    app.run(debug=True)