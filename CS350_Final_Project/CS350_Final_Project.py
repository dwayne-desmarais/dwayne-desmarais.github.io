'''
	Dwayne Desmarais
	CS 350 - Emerging Sys Arch & Tech
	Week 7-1 Final Project

	Weather Station sensor project

	Sensor:		Descrption of use:

	Light sensor	Detect light levels (day/night) and take a reading if applicable
			checked every 30 minutes.

	LED bar		Light displays RYG for different temperature/humidity levels
				Red 	= humidity over 80%
				Yellow  = humidity under 80%
				Green   = 1-8 lights showing temperature range
					  Range:
					  1 light = 40 or below
					  2 light = above 40, below 50
					  3 light = above 50, below 60
					  4 light = above 60, below 70
					  5 light = above 70, below 80
					  6 light = above 80, below 90
					  7 light = above 90, below 100
					  8 light = 100 or above

	Button		Manual, unrecorded instant reading

	LCD screen	Last reading taken, time

	Temp/Humid	Take readings for temperature and humidity
'''

# Library inports
import time
import datetime
import math
import json
import grovepi
from grove_rgb_lcd import *

# Sensor and connection port
button = 3
ledbar = 4
temp_sensor = 8
light_sensor = 0

# temp/humid sensor type
blue = 0

# Reading counter
counter_id = 0

# declare json array information
outputData = {}
outputData['readings'] = []

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(light_sensor, "INPUT")
grovepi.pinMode(temp_sensor, "INPUT")
grovepi.pinMode(ledbar, "OUTPUT")

# Initialize ledbar
grovepi.ledBar_init(ledbar, 0)

#set ledbar lights to all off
for i in range(0,11):
    grovepi.ledBar_setLed(ledbar, i, 0)

# set start text for LCD screen
setText("Push the button for a reading")
setRGB(0,128,64)

# Turn on ledbar once sensor exceeds threshold resistance
threshold = 50
day_mode = False

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        # Read humidity/temperature
        [tempC,humidity] = grovepi.dht(temp_sensor,blue)

        if math.isnan(tempC) == False and math.isnan(humidity) == False:

            # Math to convert Celius to Fahrenheit
            tempF = (tempC * 9/5) + 32

	while grovepi.digitalRead(button):

	    # take one time, manual reading using button, not recorded
            # Set LCD text with humidity, temp data
            setText("Humidity:  %.01f%%\nTemp:    %.01fF"%(humidity, tempF))

            # reset screen text after 5 seconds
            time.sleep(3.0)
            setText("Data not saved.")

            # reset to default mesage
            time.sleep(3.0)
	    setText("Push the button for a reading")

        # set current time for reading time check
	take_reading_time = datetime.datetime.now()

	# set day_mode to False once it is too dark outside
	if resistance > threshold:
	    day_mode = False

	# Less resistance = more light
        if resistance < threshold and day_mode == False:
            # Day mode activated
	    day_mode = True
	    time_check = take_reading_time

	    print("It is day time")
            print take_reading_time
            print time_check

	# take a reading during day time only (day_mode = true)
	# take reading if take_reading_time = current_time
	while day_mode and take_reading_time >= time_check:

	    # Check if humidity is at or below 80%
	    # ledbar = |-|Y|-|-|-|-|-|-|-|-|
	    if humidity <= 80:
 	        grovepi.ledBar_setLed(ledbar, 2, 1)

            # Check if humidity is above 80%
            # ledbar = |R|-|-|-|-|-|-|-|-|-|
	    if humidity > 80:
                grovepi.ledBar_setLed(ledbar, 1, 1)

	    # Check if temperature is at or above 60, and below 86
	    # ledbar = |-|-|G|G|-|-|-|-|-|-|
	    if tempF >= 60 and tempF < 85:
                grovepi.ledBar_setLed(ledbar, 3, 1)
                grovepi.ledBar_setLed(ledbar, 4, 1)

            # Check if temperature is at or above 85, and below 95
            # ledbar = |-|-|-|-|-|G|G|-|-|-|
	    if tempF >= 85 and tempF < 95:
                grovepi.ledBar_setLed(ledbar, 6, 1)
                grovepi.ledBar_setLed(ledbar, 7, 1)

            # Check if temperature is at or above 95
            # ledbar = |-|-|-|-|-|-|-|-|G|G|
	    if tempF >= 95:
                grovepi.ledBar_setLed(ledbar, 9, 1)
                grovepi.ledBar_setLed(ledbar, 10, 1)

	    # print data to terminal screen
            print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
            print("humidity = %.02f%% tempF = %.02f F"%(humidity, tempF))

	    # format time
            date_time = take_reading_time.strftime("%H:%M:%S") # formated date and time

            # append data to file after each sensor read
            outputData['readings'].append(
            {
                'id' : counter_id,
                'humidity' : humidity,
                'temperature' : tempF,
	        'time': date_time
            })

            # open file and record last data set reading
            with open('station.json', 'w') as file:
                json.dump(outputData, file)

	    # Increase next check by 30 minutes (30 seconds for now)
	    time_check = time_check + datetime.timedelta(seconds=30)

	    # increment counter_id by 1 record
	    counter_id += 1

    except IOError:
        print ("Main while error")
