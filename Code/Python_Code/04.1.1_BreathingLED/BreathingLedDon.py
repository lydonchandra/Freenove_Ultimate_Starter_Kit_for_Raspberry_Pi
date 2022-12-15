import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)

    pwm = GPIO.PWM(ledPin, 500)
    pwm.start(0)

def loop():
    while True:
        for dutyCycle in range(0, 101, 1):
            pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.01)
        time.sleep(1)

        for dutyCycle in range(100, -1, -1):
            pwm.ChangeDutyCycle(dutyCycle)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    print("Program is starting...")
    setup()
    try:
        loop()
    except:
        destroy()



