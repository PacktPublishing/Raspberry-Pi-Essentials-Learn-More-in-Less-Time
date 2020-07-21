from flask import Flask
#import json
import RPi.GPIO as GPIO

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Lets Have a Party"

@app.route("/<key>")
def led(key):
    if key == "1":
        GPIO.output(21, GPIO.HIGH)
        return "LED ON \n"
    elif key == "0":
        GPIO.output(21, GPIO.LOW)
        return "LED OFF \n"
    else:
        return "Command Not Found \n"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
