# ArduLinux
# Kiara Navarro
# sophiekovalevsky@fedoraproject.org
# http://sophiekovalevsky.github.io/

from time import sleep
import serial, psutil

class memory(object):

	def __init__(self, unit='kB'):

		# Pick up memory info from meminfo file
		memInfoPath = '/proc/meminfo'

		with open(memInfoPath,'r') as memInfo:
			memData = memInfo.readlines()

		# As every line in memData is a string
		# I need to first convert to int to 
		# start work with these values
		self._memTotal = int(memData[0].split()[1])
		self._memFree = int(memData[1].split()[1])

		# Assing unit value as an attribute
		self.unit = unit

	@property
	def total(self):
	    return self._memTotal

	@property
	def used(self):
	    return self._memTotal - self._memFree

def fillData(data):
	dataBuffer = ""
	if int(data) < 10000:
		if int(data) < 1000:
			if int(data) < 100:
				if int(data) < 10:
					dataBuffer += "0000"
				else:
					dataBuffer += "000"
			else:
				dataBuffer += "00"
		else:
			dataBuffer += "0"
	dataBuffer += data
	return dataBuffer


print "Starting..."
isConnected = True

try:
	# Write here the port where Arduino is connected
	serialPortPath = '/dev/ttyACM1'
	# Create a serial port object to start communication
	# with arduino
	port = serial.Serial(serialPortPath,9600)
	print "Arduino connection has been started"
	# Wait 2 secs 
	sleep(2)
except:
	connected = False
	print "The Arduino is not connected. Please check if the serial port is the one the arduino is connected"

while isConnected:
	# Remove any data from output buffer
	port.flushOutput()
	sendData = ""
	mem = memory()

	memUsed = str(mem.used/2**20)
	memFree = str(int(mem.total-mem.used)/2**20)
	memTotal = str(int(memUsed) + int(memFree))
	perCPU = psutil.cpu_percent(interval=0.25,percpu=True)

	for index in range(len(perCPU)):
		sendData += str(round(perCPU[index]))

	sendData += fillData(memUsed)
	sendData += fillData(memFree)
	sendData += fillData(memTotal)

	# Get the total data length 
	sizeData = str(len(sendData))
	print sizeData

	port.write(sendData)

	# Print in console all the data that I'm sending to arduino
	print "Memory Used " + memUsed + " GB |" + " Free Memory " + memFree + " GB |" + " Total memory " + memTotal + " GB"


