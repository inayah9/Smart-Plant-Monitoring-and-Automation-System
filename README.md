
--- Smart Plant Monitoring and Automation System ---


-- Overview ---

A system that alows a user to be able to monitor the moisture levels of a plant, the sourounding humdity and the tempreature(when placed in a singleplant green(also know as a tent)). The use will also be allowed to water the plant remotely using a web based dahsboard.

--- Description ---

The System starts with  placing the sensors in a plant pot(or on the side of a green house tent). The user can then start the pi, the pi is installed with tailscale so the systems web dashboard can be accessed outside of the same network. When system is acticated a web page dahsboard will be accessible where a plant can be added. This includes a name, a type of plant, e.g vegtable, flower, succulent ect., the time that the plant was planted and the the last time the plant was watered. This will then go to the main dahsboard where they can view the information of the plant in real time,  a button can be pressed that will water the plant for 5 seconds, this will cuase the page to refresh. And a button that will delete the pant and return the the add pplant page. The information for the plant will be held on a JSon file as well as the readings for the sensors that can be read by searching the url that the dashboard is on with the added api/readings.


---
--- Dependencies ---

Before running the program, ensure the following are available:

- Python 3.10+
- A web browser (e.g., Chrome, Edge)
- Operating System:

  - Windows 10 / 11
  - Linux (Raspberry Pi OS recommended)

--- Python Libraries ---

Installed via `requirements.txt`:

* Flask
* adafruit-circuitpython-ahtx0 - for the humidity and temperature sensor 
* adafruit-circuitpython-ads1x15 - for the ADC(analouge to DC converter)

---

--- Installing ---

Step 1. Download the project

Download the ZIP file or clone the repository:

    bash git clone <your-repo-url> OR extract the provided ZIP file.

Step 2. Navigate to the project folder

    cd Smart-Plant-Monitoring-and-Automation-System

Step 3. Create a virtual environment

    py -m venv venv

Step 4. Install dependencies


    py -m pip install -r requirements.txt

--- Executing the Program ---

-- Step-by-step instructions--

Step 1. Open terminal in the project folder
Step 2. Run the application:

In the terminal run
    py app.py


Step 3. Open a web browser and go to the first link provided in the terminal(typically)


http://127.0.0.1:5000


---

--- Simulation Mode ---

The system runs in simulation mode by default, allowing it to function without physical hardware.

* Sensor values are generated automatically
* Pump actions are simulated via console output

To use real hardwaren in the sensor.py, set:


SIMULATION_MODE = False



---

--- Hardware Implementation ---

The system was developed and tested using:

* Raspberry Pi
* AHT10 temperature and humidity sensor
* ADS1115 ADC with soil moisture sensor
* Relay module and water pump

The full hardware system is demonstrated in the project video submission.

---

## Remote Access (Optional)

The system supports remote access using Tailscale, allowing secure access to the dashboard from external devices without port forwarding.

This feature is optional and demonstrated in the project video. It is not required to run the system locally. ( while connected to the same network)



--- Help ---

--- Common Issues 

**1. Flask not found**

```bash
py -m pip install -r requirements.txt
```

**2. 'pip' not recognised**

```bash
py -m pip install -r requirements.txt
```

**3. Port already in use**

- Close other running Flask apps
- Restart terminal

**4. No sensor data**

- Ensure simulation mode is enabled:


SIMULATION_MODE = True


---

## Authors

* Inayah Yasmin
* GitHub: inayah9

---

--- Version History ---

ver 0.2

* Added simulation mode
* Improved sensor handling
* Added remote access support (Tailscale)

ver 0.1

* Initial release
* Basic dashboard and sensor integration

---
 License

This project is for academic use. No formal license applied.

---
Acknowledgments

* Raspberry Pi Foundation
* Adafruit sensor libraries
* Flask documentation and community
* Inspiration from IoT smart agriculture systems


code found for the ads1115

https://38-3d.co.uk/blogs/blog/using-a-soil-moisture-sensor-with-the-raspberry-pi?srsltid=AfmBOorcJZNjyV5_Qe7FLkvGlxxy7CP98NrG4PAItllXcIQhKVcxm7Or

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C and ADS1115 ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
moisture_sensor = AnalogIn(ads, ADS.P0)



Code for aht10 sensor 
https://38-3d.co.uk/blogs/blog/using-the-aht10-with-the-raspberry-pi?srsltid=AfmBOorPwfNmAdOvElteliPk7iEtzZVvhexSVRlYYP3sWbGHiCd4RBEB

import time
import board
import adafruit_ahtx0

# Initialize I2C and AHT10 sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

try:
    while True:
        temperature = sensor.temperature  # Read temperature in Celsius
        humidity = sensor.relative_humidity  # Read humidity in percentage

        print(f"Temperature: {temperature:.2f} °C")
        print(f"Humidity: {humidity:.2f} %")
        print("------------------------")

        time.sleep(2)  # Wait 2 seconds before the next reading
except KeyboardInterrupt:
    print("Exiting...")
