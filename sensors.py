from __future__ import annotations

import random
import time
from typing import Any, Dict, Optional

AHT_SENSOR = None
AHT_ERROR: Optional[str] = None

def _init_aht():
    global AHT_SENSOR, AHT_ERROR

    if AHT_SENSOR is not None:
        return AHT_SENSOR
# imports to be able to read the board and the library for the sensors 
    try:
        import board
        import busio
        import adafruit_ahtx0

        i2c = busio.I2C(board.SCL, board.SDA)
        AHT_SENSOR = adafruit_ahtx0.AHTx0(i2c)
        AHT_ERROR = None
        return AHT_SENSOR
    except Exception as e:
        AHT_SENSOR = None
        AHT_ERROR = str(e)
        return None

def get_sensor_data() -> Dict[str, Any]:
    sensor = _init_aht()

    try:
        if sensor is None:
            raise RuntimeError(AHT_ERROR or "AHT sensor not available")

        temperature = round(float(sensor.temperature), 1)
        humidity = round(float(sensor.relative_humidity), 1)
        aht_source = "real"
        sensor_error = None

    except Exception as e:
        temperature = round(random.uniform(20.0, 28.0), 1)
        humidity = round(random.uniform(45.0, 65.0), 1)
        aht_source = "simulated"
        sensor_error = str(e)

    soil_moisture = random.randint(40, 70)
# retuen the data from the sensors not all added at the moment 
# need to work on the soil sensoe next
    return {
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": soil_moisture,
        "aht_source": aht_source,
        "soil_source": "simulated",
        "sensor_error": sensor_error,
        "timestamp": int(time.time())
    }