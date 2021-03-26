import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0.1)

def write_read(brightness):
	arduino.write(bytes(brightness, 'utf-8'))
	time.sleep(1)
	data = arduino.readline()
	status = arduino.readline()
	return data, status

while True:
	arduino.flushInput()
	num = input("Enter a number: ")
	data,status = write_read(num)
	print(data,status)

