import RPi.GPIO as GPIO
import time
def motor():
    pin1= 18
    pin2= 19
    pin3= 20
    pin4= 21
    x=0


    while( x <135):  
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(pin3, GPIO.OUT)
        GPIO.setup(pin4, GPIO.OUT)

        GPIO.output(pin1,GPIO.HIGH)
        GPIO.output(pin4,GPIO.LOW)
        time.sleep(0.01)


        GPIO.output(pin2,GPIO.HIGH)
        GPIO.output(pin1,GPIO.LOW)
        time.sleep(0.01)


        GPIO.output(pin3,GPIO.HIGH)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(0.01)


        GPIO.output(pin4,GPIO.HIGH)
        GPIO.output(pin3,GPIO.LOW)
        time.sleep(0.01)
        x+=1

    time.sleep(10)
    print(x)
    while( 134<x <270):
        # print(x)
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(pin1, GPIO.OUT)
         GPIO.setup(pin2, GPIO.OUT)
         GPIO.setup(pin3, GPIO.OUT)
         GPIO.setup(pin4, GPIO.OUT)

         GPIO.output(pin4,GPIO.HIGH)
         GPIO.output(pin1,GPIO.LOW)
         time.sleep(0.01)


         GPIO.output(pin3,GPIO.HIGH)
         GPIO.output(pin2,GPIO.LOW)
         time.sleep(0.01)


         GPIO.output(pin2,GPIO.HIGH)
         GPIO.output(pin3,GPIO.LOW)
         time.sleep(0.01)


         GPIO.output(pin1,GPIO.HIGH)
         GPIO.output(pin4,GPIO.LOW)
         time.sleep(0.01)
         x+=1

    GPIO.cleanup()

#motor()

