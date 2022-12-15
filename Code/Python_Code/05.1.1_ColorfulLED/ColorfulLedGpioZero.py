from gpiozero import LED,RGBLED
from time import sleep
import signal
import random
import time

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    rgbLed.close()

signal.signal(signal.SIGABRT, handler)
signal.signal(signal.SIGTERM, handler)


rgbLed = RGBLED('BOARD11', 'BOARD12', 'BOARD16')

rgbLed.color = (0, 1, 0)
sleep(1)
rgbLed.color = (1, 1, 0)
sleep(1)

while True:
    rgbLed.color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    time.sleep(0.5)

signal.pause()
