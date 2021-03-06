import configparser
import os
import os.path
import sys
import pathlib
import time
import threading
from ftplib import FTP
from nanpy import Servo

class Turret:
	# see diagrams
	# servo_pan = Servo(10)
	# servo_tilt = Servo(11)
	turret_count = 0
	servo_tilt = Servo(11)
	servo_pan = Servo(10)
	
	def parse_turret_config(self):
		path = pathlib.Path('scanbot.cfg')
		if path.is_file():
			print("Reading turret config file...")
			config = configparser.ConfigParser()
			config.read('scanbot.cfg')
			tilt_servo_min = config['TURRET']['Tilt Servo Min']
			tilt_servo_max = config['TURRET']['Tilt Servo Max']
			tilt_servo_mid = config['TURRET']['Tilt Servo Mid']
			pan_servo_min = config['TURRET']['Pan Servo Min']
			pan_servo_max = config['TURRET']['Pan Servo Max']
			pan_servo_mid = config['TURRET']['Pan Servo Mid']
			
		else:
			print("Couldn't find turret config file. Creating a new one...")
			
			config = configparser.RawConfigParser()
			config['LOGGER'] = {}
			config['LOGGER']['IP'] = '192.168.1.1'
			config['LOGGER']['Username'] = 'Username'
			config['LOGGER']['Password'] = 'Password'
			config['LOGGER']['SSH Run Command'] = './Logger'
			
			config['NAVIO'] = {}
			config['NAVIO']['IP'] = '192.168.1.1'
			config['NAVIO']['Username'] = 'Username'
			config['NAVIO']['Password'] = 'Password'
			config['NAVIO']['SSH Run Command'] = './Logger'
			
			config['TURRET'] = {}
			config['TURRET']['Tilt Servo Min'] = '0'
			config['TURRET']['Tilt Servo Max'] = '255'
			config['TURRET']['Tilt Servo Mid'] = '127'
			config['TURRET']['Pan Servo Min'] = '0'
			config['TURRET']['Pan Servo Max'] = '255'
			config['TURRET']['Pan Servo Mid'] = '127'
			
			
			with open('scanbot.cfg', 'w') as configfile:
				config.write(configfile)
			
			sys.exit("Please edit \"scanbot.cfg\" with correct information. The program will now stop.")
			
		print("Parsed the following data:")
		print("Tilt Servo Min: " + tilt_servo_min)
		print("Tilt Servo Max: " + tilt_servo_max)
		print("Tilt Servo Mid: " + tilt_servo_mid)
		print("Pan Servo Min: " + pan_servo_min)
		print("Pan Servo Max: " + pan_servo_max)
		print("Pan Servo Mid: " + pan_servo_mid)
		
		return [tilt_servo_min, tilt_servo_max, tilt_servo_mid, pan_servo_min, pan_servo_max, pan_servo_mid]
	
	def __init__(self):
                Turret.turret_count += 1
                servo_vars = self.parse_turret_config()
                self.tilt_servo_min = servo_vars[0]
                self.tilt_servo_max = servo_vars[1]
                self.tilt_servo_mid = servo_vars[2]
                self.pan_servo_min = servo_vars[3]
                self.pan_servo_max = servo_vars[4]
                self.pan_servo_max = servo_vars[5]
				
	def left90(self):
		pass
		
	def right90(self):
		pass

	def left180(self):
		# servo_tile.write()
		# servo_left.write()
		pass

	def right180(self):
		# servo_tile.write()
		# servo_left.write()
		pass
	
	def mid(self):
		Turret.servo_tilt.write(self.tilt_servo_mid)
	
	def left(self):
		Turret.servo_pan.write(self.pan_servo_min)

	def right(self):
		Turret.servo_pan.write(self.pan_servo_max)

	def servo_demo(self):
		for move in [0, 90, 180, 90, 0]:
			servo_tilt.write(move)
			time.sleep(1)
		
		for move in [0, 90, 180, 90, 0]:
			servo_rotation.write(move)
			time.sleep(1)

	def write_pwm_pan(self, pwm_input, last_pwm_input):		
		#for input in range 1097-1894, coef is 0.229 and 1097 should be substracted
		if(1090 < pwm_input < 1900):
			if(not((last_pwm_input - 20) <= pwm_input <= (last_pwm_input + 20))):
				Turret.servo_pan.write((pwm_input - 1097) * 0.229)
		else:
			print('Bad radio input')
	
	
	def write_pwm_tilt(self, pwm_input, last_pwm_input):
		# for input in range 1097-1894, coef is 0.229 and 1097 should be substracted
		if(1090 < pwm_input < 1900):
			if(not((last_pwm_input - 20) <= pwm_input <= (last_pwm_input + 20))):
				Turret.servo_tilt.write((pwm_input - 1097) * 0.229)
		else:
			print('Bad radio input')

	def home():
		# go to default pos
		pass


		
		
		
