import time
import RPI.GPIO as GPIO

count = 0
GPIO.setmpode(GPIO.BCM)
GPIO.setup(14, GPIO.out)

while count < 10:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.Low)
    time.sleep(1)
    count = count+1

GPIO.cleanup()
