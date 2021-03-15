# .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
# script to trigger procedure starting from a detected movement
#   Upon detection, the useful procedure is called and the led lights up.
# .-..-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#input pin
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# LED ouput yellow
GPIO.setup(16, GPIO.OUT)

#Callback function to run when motion de
def motionSensor(channel):
    GPIO.output(16, GPIO.LOW)
    if GPIO.input(21):
        global counter
        counter += 1
        print('Motion Detected')
        # here it is possible to call procedures
        # the LED remains ON for the whole procedure
        GPIO.output(16, GPIO.HIGH)
        sleep(5) # simulation of execution time of function

# add event listener on pin 21
# bouncetime ==  minimum time between two callbacks in milliseconds
GPIO.add_event_detect(21, GPIO.BOTH, callback=motionSensor, bouncetime=300)
counter = 0

try:
    while True:
        sleep(1)

finally:
    GPIO.cleanup()
    print ('All cleaned up')
