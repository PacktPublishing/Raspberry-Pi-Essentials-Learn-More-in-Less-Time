import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

@app.route("/")
def hello():
    page = """<script type='text/javascript'>
    function submit(x) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                alert(xhr.response);
            }
        }
        xhr.open('GET', 'http://192.168.1.100:80/'+x, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
        xhr.send();
    }</script>"""

    return page + "<button onclick=submit(1)>ON</button><button onclick=submit(0)>OFF</button>"

@app.route("/<key>")
def led(key):
	if key == "1":
		GPIO.output(21, GPIO.HIGH)
		return "LED ON \n"
	elif key == "0":
		GPIO.output(21, GPIO.LOW)
		return "LED OFF \n"
	else:
		return "Command Not Found"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
