import RPi.GPIO as GPIO
from time import sleep

BUZZER = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER,GPIO.OUT)

try:
    GPIO.output(BUZZER,GPIO.HIGH)
    sleep(0.05)
    GPIO.output(BUZZER,GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
