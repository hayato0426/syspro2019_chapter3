import time
import RPi.GPIO as GPIO

count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


while count < 10:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    time.sleep(1)
    count = count+1 

GPIO.cleanup()
