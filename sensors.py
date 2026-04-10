

## test the aht10 sensor i=on its own as its BUGGING OUT
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

    temperature = None
    humidity = None
    sensor_error = None

    if sensor is None:
        sensor_error = AHT_ERROR or "AHT sensor not available"
    else:
        try:
            temperature = round(float(sensor.temperature), 1)
            humidity = round(float(sensor.relative_humidity), 1)
        except Exception as e:
            sensor_error = str(e)
# retuen the data from the sensors not all added at the moment 
# need to work on the soil sensoe next
    return {
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": None,   # not connected yet
        "water_level": None,     # not implemented yet
        "sensor_error": sensor_error,
        "timestamp": int(time.time())
    }