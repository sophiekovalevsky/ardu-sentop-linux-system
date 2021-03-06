#! /usr/bin/env python2
# ArduLinux
# Kiara Navarro
# sophiekovalevsky@fedoraproject.org
# http://sophiekovalevsky.github.io/

from time import sleep
import serial, psutil
import sys, sensors

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


	
def chipValue():
	chipValue = []
	for chip in sensors.get_detected_chips():
		for feature in chip.get_features():
			for subfeature in chip.get_all_subfeatures(feature):
					chipValue.append(chip.get_value(subfeature.number))
	return chipValue

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
	serialPortPath = '/dev/ttyACM2'
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

	# in GB
	memUsed = str(int(round(mem.used))/2**20)
	memFree = str(int(round(mem.total-mem.used))/2**20)
	# in MB
	#memUsed = str(int(round(mem.used))/2**10)
	#memFree = str(int(round(mem.total-mem.used))/2**10)
	memTotal = str(int(memUsed) + int(memFree))
	perCPU = psutil.cpu_percent(interval=0.25,percpu=True)

	for index in range(len(perCPU)):
		sendData += fillData(str(int(round(perCPU[index]))))

	sendData += fillData(memUsed)
	sendData += fillData(memFree)
	sendData += fillData(memTotal)

	sensorValue = chipValue()
	fan = str(int(round(sensorValue[2])))
	tempPHY = str(int(round(sensorValue[3])))
	tempCORE1 = str(int(round(sensorValue[7])))
	tempCORE2 = str(int(round(sensorValue[11])))

	sendData += fillData(fan)
	sendData += fillData(tempPHY)
	sendData += fillData(tempCORE1)
	sendData += fillData(tempCORE2)

	# Get the total data length 
	sizeData = str(len(sendData))
	print sizeData

	port.write(sendData)

	# Print in console all the data that I'm sending to arduino
	#print "Memory Used " + memUsed + " GB |" + " Free Memory " + memFree + " GB |" + " Total memory " + memTotal + " GB"
	print sendData





	

