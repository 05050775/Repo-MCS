# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import time
import httplib, urllib
import json
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while Ture:
	SwitchStatus = GPIO.input(24)
	if( SwitchStatus == 0):
		print('Button pressed')
	else:
		print('Button released')

deviceId = "DoyBQQ7D"
deviceKey = "0E8NFG0rekgfs5be" 
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = httplib.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (httplib.HTTPException, socket.error) as ex: 
			print("Error: %s" % ex)
			time.sleep(10)
			# sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 
 import Adafruit_DHT
 @@ -48,8 +70,17 @@
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
	h0, t0= Adafruit_DHT.read_retry(sensor, pin)
 	if humidity is not None and temperature is not None:
    		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
		payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":h0}},{"dataChnId":"Temperature","values":{"value":t0}},{"dataChnId":"SwutchStatus","values":{"value":SwitchStatus}}]} 
 		post_to_mcs(payload)
		time.sleep(10) 
 	else:
		print('Failed to get reading. Try again!')
		sys.exit(1)
