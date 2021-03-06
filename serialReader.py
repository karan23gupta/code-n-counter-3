import serial
import time
import way2sms


from_mobile_number = "9555777987"
password = "P7342B"
to_mobile_number = "9555777987"
message = "Help!"

additional_mobile_numbers = []

port_number = input('Enter port number: ')
ser = serial.Serial('/dev/ttyACM' + str(port_number))
ser.flushInput()

additional_mobile_numbers = [x.strip() for x in str(input('Enter comma seperated mobile numbers: ')).split(',')]
print ('Registered numbers: ', additional_mobile_numbers)

while True:
	try:
		time.sleep(0.02)
		ser_bytes = ser.readline()
		decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
		print(decoded_bytes)
		if decoded_bytes == 1:
			q = way2sms.sms(from_mobile_number, password)
			
			print (q.send(to_mobile_number,message))
			for mob in additional_mobile_numbers:
				q.send(mob, message)
			q.logout()
	except:
		pass
		#print(traceback.format_exc())

