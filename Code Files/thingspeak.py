import http.client, urllib.parse
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def doit():
	x=GPIO.input(21)
	params = urllib.parse.urlencode({'field1': x,'key':'3Q99D70OPQKHK61R'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print(response.status, response.reason)
		data = response.read()
		conn.close()
	except:
		print("connection failed")

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
	while True:
		doit()
		time.sleep(16) 

