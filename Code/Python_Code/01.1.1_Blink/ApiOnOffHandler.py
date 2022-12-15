from http.server import SimpleHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO

ledPin = 11

class ApiOnOffHandler(SimpleHTTPRequestHandler):

    isSetup = False

    # @staticmethod
    # def setup():
    #     GPIO.setmode(GPIO.BOARD)
    #     GPIO.setup(ledPin, GPIO.OUT)
    #     GPIO.output(ledPin, GPIO.LOW)

    def do_GET(self):
        if not ApiOnOffHandler.isSetup:
            print('setting up GPIO')
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(ledPin, GPIO.OUT)
            GPIO.output(ledPin, GPIO.LOW)
            ApiOnOffHandler.isSetup = True
            # ApiOnOffHandler.setup()

        if self.path == '/led/on':
            GPIO.output(ledPin, GPIO.HIGH)
        elif self.path == '/led/off':
            GPIO.output(ledPin, GPIO.LOW)
        else:
            print('invalid path')

        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(("", 8080), ApiOnOffHandler)
httpd.serve_forever()