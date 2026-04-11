## The water pumps logic
# will make the water come out for 5 seconds when the pump is pressed
# maybe allow the user to be able to controll the amount of water in seconds????

import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

# pi pin
RELAY_PIN = 17
ACTIVE_LOW = True

GPIO_READY = False


def setup():
    global GPIO_READY

    if GPIO is None or GPIO_READY:
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)

    # Turn off at the begining
    if ACTIVE_LOW:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW)

    GPIO_READY = True


# Turn the pump on
def pump_on():
    if GPIO is None:
        return

    setup()

    if ACTIVE_LOW:
        GPIO.output(RELAY_PIN, GPIO.LOW)
    else:
        GPIO.output(RELAY_PIN, GPIO.HIGH)


def pump_off():
    if GPIO is None:
        return

    setup()

    if ACTIVE_LOW:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW)


def pump_for_seconds(seconds=5):
    setup()

    if GPIO is None:
        print("GPIO not available")
        return False

    try:
        print("Pump ON")
        pump_on()
        time.sleep(seconds)
    finally:
        print("Pump OFF")
        pump_off()

    return True