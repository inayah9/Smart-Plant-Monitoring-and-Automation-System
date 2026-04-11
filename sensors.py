import time
from typing import Any, Dict, Optional

AHT_SENSOR = None
AHT_ERROR: Optional[str] = None

ADS_DEVICE = None
SOIL_SENSOR = None
ADC_ERROR: Optional[str] = None


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


def _init_ads():
    global ADS_DEVICE, SOIL_SENSOR, ADC_ERROR

    if ADS_DEVICE is not None:
        return ADS_DEVICE

    try:
        import board
        import busio
        import adafruit_ads1x15.ads1115 as ADS
        from adafruit_ads1x15.analog_in import AnalogIn

        i2c = busio.I2C(board.SCL, board.SDA)
        ADS_DEVICE = ADS.ADS1115(i2c)

        # Soil sensor connected to A0 on the ADS1115
        SOIL_SENSOR = AnalogIn(ADS_DEVICE, ADS.P0)
        

        ADC_ERROR = None
        return ADS_DEVICE

    except Exception as e:
        ADS_DEVICE = None
        SOIL_SENSOR = None
        ADC_ERROR = str(e)
        return None

# For the temp reader (aht10)
def _read_aht():
    sensor = _init_aht()

    temperature = None
    humidity = None
    error = None

    if sensor is None:
        error = AHT_ERROR or "AHT sensor not available"
    else:
        try:
            temperature = round(float(sensor.temperature), 1)
            humidity = round(float(sensor.relative_humidity), 1)
        except Exception as e:
            error = str(e)

    return temperature, humidity, error

# For the soil moisture reader - connectd to an adc - ads1115
def _read_soil():
    _init_ads()

    if SOIL_SENSOR is None:
        return None, ADC_ERROR

    try:
        voltage = SOIL_SENSOR.voltage

        # Temporary conversion for testing
        # You will calibrate these values later
        # Typically higher voltage means dryer soild, and lower voltage means wetter soil
        dry_voltage = 2.6
        wet_voltage = 1.2

        percent = (dry_voltage - voltage) * 100 / (dry_voltage - wet_voltage)
        percent = max(0, min(100, percent))

        return int(percent), None

    except Exception as e:
        return None, str(e)

#collect the sensor data and send it to be displayed ont he webpage
def get_sensor_data() -> Dict[str, Any]:
    temperature, humidity, aht_error = _read_aht()
    soil_moisture, soil_error = _read_soil()

    sensor_error = None
    if aht_error and soil_error:
        sensor_error = f"AHT: {aht_error} | Soil: {soil_error}"
    elif aht_error:
        sensor_error = f"AHT: {aht_error}"
    elif soil_error:
        sensor_error = f"Soil: {soil_error}"
# Return the data that is collected from the sensors, water level senses is ommited 
    return {
        "temperature": temperature,
        "humidity": humidity,
        "soil_moisture": soil_moisture,
        "water_level": None, # for future 
        "sensor_error": sensor_error,
        "timestamp": int(time.time())
    }