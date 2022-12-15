import RPi.GPIO as GPIO
import time
import random
import signal

pins = [11, 12, 16]

def setup():
    global pwmRed, pwmGreen, pwmBlue

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT)
    GPIO.output(pins, GPIO.HIGH)
    pwmRed = GPIO.PWM(pins[0], 2000)
    pwmGreen = GPIO.PWM(pins[1], 2000)
    pwmBlue = GPIO.PWM(pins[2], 2000)
    pwmRed.start(0)
    pwmGreen.start(0)
    pwmBlue.start(0)

def setColor(red, green, blue):
    pwmRed.ChangeDutyCycle(red)
    pwmGreen.ChangeDutyCycle(green)
    pwmBlue.ChangeDutyCycle(blue)

def loop():
    while True:
        red = random.randint(0, 100)
        green = random.randint(0, 100)
        blue = random.randint(0, 100)
        setColor(red, green, blue)
        print('r=%d, g=%d, b=%d' %(red, green, blue))
        time.sleep(1)

def destroy():
    time.sleep(1)
    pwmRed.ChangeDutyCycle(0)
    pwmGreen.ChangeDutyCycle(0)
    pwmBlue.ChangeDutyCycle(0)

    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()

def exit_handler():
    destroy()


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    destroy()

signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGTERM, handler)

if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        loop()
    finally:
        print('exception')
        destroy()

